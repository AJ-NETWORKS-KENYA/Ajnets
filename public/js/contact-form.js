/**
 * AJNETWORKS — Vanilla ES6+ Contact Form Handler (Zero-jQuery)
 * Validates consultation requests and dispatches JSON payloads to /api/contact.
 */
(function () {
  "use strict";

  document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("ajax-form");
    if (!form) return;

    const submitBtn = document.getElementById("send");
    const errorContainer = document.getElementById("err-form");
    const successModal = document.getElementById("successModal");
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    function setVisible(idOrEl, visible) {
      const el =
        typeof idOrEl === "string" ? document.getElementById(idOrEl) : idOrEl;
      if (el) el.style.display = visible ? "block" : "none";
    }

    form.querySelectorAll(".error").forEach((el) => setVisible(el, false));

    const nameInput = form.querySelector('input[name="name"]');
    const orgInput = form.querySelector('input[name="organization"]');
    const regionSelect = form.querySelector('select[name="region"]');
    const emailInput = form.querySelector('input[name="email"]');
    const phoneInput = form.querySelector('input[name="phone"]');
    const messageInput = form.querySelector('textarea[name="message"]');
    const botInput = form.querySelector('input[name="bot_field"]');

    if (nameInput) {
      nameInput.addEventListener("blur", () =>
        setVisible("err-name", nameInput.value.trim() === "")
      );
    }
    if (orgInput) {
      orgInput.addEventListener("blur", () =>
        setVisible("err-organization", orgInput.value.trim() === "")
      );
    }
    if (emailInput) {
      emailInput.addEventListener("blur", () => {
        const val = emailInput.value.trim();
        if (!val) {
          setVisible("err-email", true);
          setVisible("err-emailvld", false);
        } else if (!emailRegex.test(val)) {
          setVisible("err-email", false);
          setVisible("err-emailvld", true);
        } else {
          setVisible("err-email", false);
          setVisible("err-emailvld", false);
        }
      });
    }
    if (phoneInput) {
      phoneInput.addEventListener("blur", () =>
        setVisible("err-phone", phoneInput.value.trim() === "")
      );
    }

    form.querySelectorAll("input, textarea, select").forEach((field) => {
      field.addEventListener("input", () => {
        const parent = field.parentElement;
        if (parent) {
          parent
            .querySelectorAll(".error")
            .forEach((err) => setVisible(err, false));
        }
        setVisible(errorContainer, false);
      });
    });

    form.addEventListener("submit", async function (e) {
      e.preventDefault();
      form.querySelectorAll(".error").forEach((el) => setVisible(el, false));
      setVisible(errorContainer, false);

      const name = nameInput ? nameInput.value.trim() : "";
      const organization = orgInput ? orgInput.value.trim() : "";
      const region = regionSelect ? regionSelect.value : "";
      const email = emailInput ? emailInput.value.trim() : "";
      const phone = phoneInput ? phoneInput.value.trim() : "";
      const message = messageInput ? messageInput.value.trim() : "";
      const bot_field = botInput ? botInput.value : "";

      if (bot_field && bot_field.trim() !== "") {
        return;
      }

      const lastSubmit = localStorage.getItem("lastContactSubmit");
      const now = Date.now();
      if (lastSubmit && now - parseInt(lastSubmit, 10) < 60000) {
        if (errorContainer) {
          errorContainer.textContent =
            "Please wait a minute before submitting another request.";
          setVisible(errorContainer, true);
        }
        return;
      }

      let isValid = true;
      if (!name) {
        setVisible("err-name", true);
        isValid = false;
      }
      if (!organization) {
        setVisible("err-organization", true);
        isValid = false;
      }
      if (!region) {
        setVisible("err-region", true);
        isValid = false;
      }
      if (!email) {
        setVisible("err-email", true);
        isValid = false;
      } else if (!emailRegex.test(email)) {
        setVisible("err-emailvld", true);
        isValid = false;
      }
      if (!phone) {
        setVisible("err-phone", true);
        isValid = false;
      }
      if (!message || message.length < 10) {
        if (errorContainer) {
          errorContainer.textContent =
            "Please provide a detailed message (at least 10 characters)";
          setVisible(errorContainer, true);
        }
        isValid = false;
      }

      if (!isValid) return;

      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.textContent = "Sending...";
      }

      try {
        const res = await fetch(form.getAttribute("action") || "/api/contact", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Accept: "application/json",
          },
          body: JSON.stringify({
            name,
            organization,
            region,
            email,
            phone,
            message,
            bot_field,
          }),
        });

        const data = await res.json().catch(() => ({}));
        if (res.ok) {
          setVisible(successModal, true);
          form.reset();
          localStorage.setItem("lastContactSubmit", String(Date.now()));
        } else {
          const msg =
            data && data.message
              ? `Error: ${data.message}`
              : "There was an error sending your message. Please try again.";
          if (errorContainer) {
            errorContainer.textContent = msg;
            setVisible(errorContainer, true);
          }
        }
      } catch (_err) {
        if (errorContainer) {
          errorContainer.textContent =
            "Network error while submitting your request. Please try again.";
          setVisible(errorContainer, true);
        }
      } finally {
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.textContent = "Request Strategy Call";
        }
      }
    });

    document.querySelectorAll(".close-modal, .modal-overlay").forEach((el) => {
      el.addEventListener("click", function (e) {
        if (e.target === el || el.classList.contains("close-modal")) {
          setVisible(successModal, false);
        }
      });
    });
  });
})();
