document.addEventListener('DOMContentLoaded', function() {
    const banner = document.getElementById('cookie-consent-banner');
    const acceptBtn = document.getElementById('btn-accept-cookies');
    const rejectBtn = document.getElementById('btn-reject-cookies');
    
    // Check if user has already made a choice
    const consentChoice = localStorage.getItem('consentChoice');
    
    if (!consentChoice) {
        // Show banner if no choice made
        setTimeout(() => {
            banner.classList.add('show');
        }, 1000);
    }

    function updateConsent(granted) {
        const status = granted ? 'granted' : 'denied';
        
        // Update Google Consent Mode
        if (typeof gtag === 'function') {
            gtag('consent', 'update', {
                'ad_storage': status,
                'ad_user_data': status,
                'ad_personalization': status,
                'analytics_storage': status
            });
            console.log(`Consent updated to: ${status}`);
        }

        // Save to local storage
        localStorage.setItem('consentChoice', status);
        
        // Hide banner
        banner.classList.remove('show');
    }

    if (acceptBtn) {
        acceptBtn.addEventListener('click', () => {
            updateConsent(true);
        });
    }

    if (rejectBtn) {
        rejectBtn.addEventListener('click', () => {
            updateConsent(false);
        });
    }
});
