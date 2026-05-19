const nodemailer = require("nodemailer");

module.exports = async function handler(req, res) {
  if (req.method !== "POST") {
    return res.status(405).json({ message: "Method not allowed" });
  }

  const { name, organization, region, email, phone, message } = req.body;

  // Validate basic fields
  if (!name || !email || !region || !message) {
    return res.status(400).json({ message: "Missing required fields" });
  }

  let smtpUser = process.env.SMTP_USER_DEFAULT;
  let smtpPass = process.env.SMTP_PASS_DEFAULT;

  if (region === "Rwanda") {
    smtpUser = process.env.SMTP_USER_RWANDA || smtpUser;
    smtpPass = process.env.SMTP_PASS_RWANDA || smtpPass;
  }

  try {
    const transporter = nodemailer.createTransport({
      host: process.env.SMTP_HOST || "smtp.zoho.com",
      port: process.env.SMTP_PORT || 465,
      secure: true, // true for 465, false for other ports
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
        Organization: ${organization}
        Region: ${region}
        Email: ${email}
        Phone: ${phone}
        
        Message:
        ${message}
      `,
    };

    if (region === "Rwanda") {
      mailOptions.cc = process.env.SMTP_USER_DEFAULT;
    }

    await transporter.sendMail(mailOptions);
    return res
      .status(200)
      .json({ success: true, message: "Message sent successfully." });
  } catch (error) {
    console.error("Error sending email:", error);
    return res
      .status(500)
      .json({ success: false, message: "Error sending email." });
  }
};
