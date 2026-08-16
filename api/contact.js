const nodemailer = require("nodemailer");

// Simple in-memory IP rate limiter for serverless instance
const ipRateLimit = new Map();
const RATE_LIMIT_WINDOW_MS = 10 * 60 * 1000; // 10 minutes
const MAX_REQUESTS_PER_WINDOW = 5;

function isRateLimited(ip) {
  if (!ip || ip === "unknown" || ip === "127.0.0.1") return false;
  const now = Date.now();
  const records = ipRateLimit.get(ip) || [];
  const recent = records.filter(timestamp => now - timestamp < RATE_LIMIT_WINDOW_MS);
  if (recent.length >= MAX_REQUESTS_PER_WINDOW) {
    return true;
  }
  recent.push(now);
  ipRateLimit.set(ip, recent);
  return false;
}

module.exports = async function handler(req, res) {
  // CORS Headers
  res.setHeader("Access-Control-Allow-Origin", "https://ajnetworks.co");
  res.setHeader("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");

  if (req.method === "OPTIONS") {
    return res.status(200).end();
  }

  if (req.method !== "POST") {
    return res.status(405).json({ message: "Method not allowed" });
  }

  const { name, organization, region, email, phone, message, bot_field } = req.body || {};

  // Honeypot bot protection: if bot_field is populated, return silent success
  if (bot_field && typeof bot_field === "string" && bot_field.trim() !== "") {
    return res.status(200).json({ success: true, message: "Consultation request recorded successfully." });
  }

  // Rate limiting by client IP
  const clientIp = req.headers ? (req.headers["x-forwarded-for"] || (req.socket && req.socket.remoteAddress) || "unknown") : "unknown";
  if (isRateLimited(clientIp)) {
    return res.status(429).json({ message: "Too many requests. Please try again later." });
  }

  // Validate basic required fields
  if (!name || !email || !region || !message) {
    return res.status(400).json({ message: "Missing required fields (name, email, region, message)" });
  }

  // Simple Email Regex Validation
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
    return res.status(400).json({ message: "Invalid email format" });
  }

  let smtpUser = process.env.SMTP_USER_DEFAULT;
  let smtpPass = process.env.SMTP_PASS_DEFAULT;

  if (region === "Rwanda") {
    smtpUser = process.env.SMTP_USER_RWANDA || smtpUser;
    smtpPass = process.env.SMTP_PASS_RWANDA || smtpPass;
  } else if (region === "Uganda") {
    smtpUser = process.env.SMTP_USER_UGANDA || smtpUser;
    smtpPass = process.env.SMTP_PASS_UGANDA || smtpPass;
  }

  // Fallback mode if SMTP credentials are not configured in local environment
  if (!smtpUser || !smtpPass) {
    return res.status(200).json({ success: true, message: "Consultation request recorded successfully." });
  }

  try {
    const transporter = nodemailer.createTransport({
      host: process.env.SMTP_HOST || "smtp.zoho.com",
      port: process.env.SMTP_PORT || 465,
      secure: true,
      auth: {
        user: smtpUser,
        pass: smtpPass,
      },
    });

    const mailOptions = {
      from: smtpUser,
      to: smtpUser,
      replyTo: email,
      subject: `New Consultation Request from ${name} (${organization || "N/A"}) - Region: ${region}`,
      text: `
        Name: ${name}
        Organization: ${organization || "N/A"}
        Region: ${region}
        Email: ${email}
        Phone: ${phone || "N/A"}
        
        Message:
        ${message}
      `,
    };

    if ((region === "Rwanda" || region === "Uganda") && process.env.SMTP_USER_DEFAULT) {
      mailOptions.cc = process.env.SMTP_USER_DEFAULT;
    }

    await transporter.sendMail(mailOptions);
    return res.status(200).json({ success: true, message: "Message sent successfully." });
  } catch (error) {
    console.error("Error sending email:", error);
    return res.status(500).json({ success: false, message: "Error dispatching email message." });
  }
};
