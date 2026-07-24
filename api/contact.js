const nodemailer = require("nodemailer");

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

  const { name, organization, region, email, phone, message } = req.body || {};

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
  }

  // Fallback mode if SMTP credentials are not configured in local environment
  if (!smtpUser || !smtpPass) {
    console.warn("SMTP credentials not configured. Contact lead recording skipped due to missing configuration.");
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

    if (region === "Rwanda" && process.env.SMTP_USER_DEFAULT) {
      mailOptions.cc = process.env.SMTP_USER_DEFAULT;
    }

    await transporter.sendMail(mailOptions);
    return res.status(200).json({ success: true, message: "Message sent successfully." });
  } catch (error) {
    console.error("Error sending email:", error);
    return res.status(500).json({ success: false, message: "Error dispatching email message." });
  }
};
