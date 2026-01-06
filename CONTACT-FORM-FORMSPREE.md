# Contact Form - Formspree Integration

## ✅ Setup Complete

The contact form now uses **Formspree** for email submissions. No PHP required!

### Form Details

- **Endpoint:** https://formspree.io/f/mwpevvja
- **Recipient:** jabrahamjohns@gmail.com
- **Method:** POST

### Form Fields

1. **Name** (required)
2. **Organization** (required)
3. **Email** (required)
4. **Phone** (required)
5. **Message** (required, min 10 characters)

## 🚀 How to Use

### Development/Testing

You can now use any simple web server:

```bash
# Python (simple)
python -m http.server 8000

# Or Node.js
npx http-server -p 8000
```

Then visit: `http://localhost:8000/contact.html`

### How It Works

1. User fills out the form
2. Form validates fields (JavaScript)
3. Form submits to Formspree
4. Formspree sends email to jabrahamjohns@gmail.com
5. User sees Formspree's thank you page

## 📧 Email Notifications

You'll receive emails at **jabrahamjohns@gmail.com** with:

- Contact name
- Organization
- Email address
- Phone number
- Message content

## 🎨 Customization

### Change Recipient Email

1. Log into your Formspree account at https://formspree.io/
2. Update the form settings
3. No code changes needed!

### Customize Success Page

Formspree allows you to customize the thank you page in your dashboard.

### Custom Redirect (Optional)

To redirect to your own thank you page after submission, add to the form:

```html
<input type="hidden" name="_next" value="https://yoursite.com/thank-you.html" />
```

## 🔧 Features

- ✅ No server-side code needed
- ✅ No PHP required
- ✅ Works with any web server
- ✅ Spam protection included
- ✅ Email notifications
- ✅ Form validation
- ✅ Mobile responsive

## 📊 Formspree Plan

**Free Plan Includes:**

- 50 submissions per month
- Email notifications
- Spam filtering
- No credit card required

To upgrade for more submissions, visit your Formspree dashboard.

## 🧪 Testing

1. Open `contact.html` in your browser
2. Fill out all fields
3. Click "Request Strategy Call"
4. You'll be redirected to Formspree's confirmation page
5. Check your email inbox for the submission

## 🆘 Troubleshooting

### Form doesn't submit

- Check browser console for JavaScript errors
- Ensure all required fields are filled
- Verify internet connection

### Email not received

- Check spam folder
- Verify Formspree endpoint URL is correct
- Log into Formspree dashboard to see submissions

### Formspree blocked

- Formspree uses cookies and may require acceptance
- Check browser's privacy settings

## 📝 Files Modified

- `contact.html` - Updated form action to Formspree URL
- `js/contact-form.js` - Simplified for Formspree (validation only)

## 🗑️ Files Removed

The following files are no longer needed:

- `contact.php`
- `contact-alternative.php`
- `EMAIL-TROUBLESHOOTING.md`
- `CONTACT-FORM-SETUP.md`
- `CONTACT-FORM-REFERENCE.md`
- `test-email.html`
- `test-contact-form.html`
- `NO-PHP-SERVER-HELP.html`

## 🌐 Deployment

The site can now be deployed to:

- **GitHub Pages** (free)
- **Netlify** (free)
- **Vercel** (free)
- **Any static hosting**
- **Any web server** (no PHP needed)

No special server requirements!

---

**Last Updated:** January 7, 2026  
**Integration:** Formspree  
**Status:** ✅ Ready to Use
