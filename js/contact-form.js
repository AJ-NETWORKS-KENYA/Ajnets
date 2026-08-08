/**
 * AJNETWORKS Contact Form Handler
 * Simple validation for Formspree integration
 */

(function ($) {
  "use strict";

  var $form;
  var $submitBtn;
  var $errorContainer;
  var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  function initContactForm() {
    $form = $("#ajax-form");
    $submitBtn = $("#send");
    $errorContainer = $("#err-form");

    // Hide all error messages initially
    $(".error").hide();

    setupRealTimeValidation();
    setupFormSubmission();
    setupInputClear();
    setupModalClose();
  }

  function setupRealTimeValidation() {
    $('input[name="name"]').on("blur", function () {
      toggleError($(this), "#err-name");
    });

    $('input[name="organization"]').on("blur", function () {
      toggleError($(this), "#err-organization");
    });

    $('input[name="email"]').on("blur", function () {
      var email = $(this).val().trim();
      if (email === "") {
        $("#err-email").show();
        $("#err-emailvld").hide();
      } else if (!emailRegex.test(email)) {
        $("#err-email").hide();
        $("#err-emailvld").show();
      } else {
        $("#err-email").hide();
        $("#err-emailvld").hide();
      }
    });

    $('input[name="phone"]').on("blur", function () {
      toggleError($(this), "#err-phone");
    });
  }

  function toggleError($input, errorSelector) {
    if ($input.val().trim() === "") {
      $(errorSelector).show();
    } else {
      $(errorSelector).hide();
    }
  }

  function setupFormSubmission() {
    $form.on("submit", function (e) {
      e.preventDefault();

      // Hide previous messages
      $(".error").hide();
      $errorContainer.hide();

      if (!validateFormValues()) {
        return false;
      }

      submitFormData();
      return false;
    });
  }

  function validateFormValues() {
    var name = $('input[name="name"]').val().trim();
    var organization = $('input[name="organization"]').val().trim();
    var email = $('input[name="email"]').val().trim();
    var phone = $('input[name="phone"]').val().trim();
    var message = $('textarea[name="message"]').val().trim();
    var region = $('select[name="region"]').val();

    var isValid = true;

    if (name === "") {
      $("#err-name").show();
      isValid = false;
    }

    if (organization === "") {
      $("#err-organization").show();
      isValid = false;
    }

    if (!region) {
      $("#err-region").show();
      isValid = false;
    }

    if (email === "") {
      $("#err-email").show();
      isValid = false;
    } else if (!emailRegex.test(email)) {
      $("#err-emailvld").show();
      isValid = false;
    }

    if (phone === "") {
      $("#err-phone").show();
      isValid = false;
    }

    if (message === "" || message.length < 10) {
      $errorContainer
        .text("Please provide a detailed message (at least 10 characters)")
        .show();
      isValid = false;
    }

    return isValid;
  }

  function submitFormData() {
    // Disable submit button and show loading
    $submitBtn.prop("disabled", true).text("Sending...");

    $.ajax({
      url: $form.attr("action"),
      method: "POST",
      data: $form.serialize(),
      dataType: "json",
      headers: {
        Accept: "application/json",
      },
      success: handleSuccess,
      error: handleError,
    });
  }

  function handleSuccess() {
    // Show the modal
    $("#successModal").fadeIn();
    $form[0].reset();
    $submitBtn.prop("disabled", false).text("Request Strategy Call");
  }

  function handleError(xhr, status, error) {
    var msg = "There was an error sending your message. Please try again.";
    try {
      var response = JSON.parse(xhr.responseText);
      if (response && response.message) {
        msg = "Error: " + response.message;
      }
    } catch (e) {}

    if (xhr.status === 404) {
      msg =
        "Backend API not found. Please ensure you are running the site via Vercel CLI (vercel dev).";
    } else if (xhr.status === 500) {
      msg += " (Server Error: Check your SMTP credentials in .env)";
    }

    $errorContainer.text(msg).show();
    $submitBtn.prop("disabled", false).text("Request Strategy Call");
  }

  function setupInputClear() {
    // Clear error messages on input
    $form.find("input, textarea").on("input", function () {
      $(this).siblings(".error").hide();
      $errorContainer.hide();
    });
  }

  function setupModalClose() {
    // Close modal logic
    $(".close-modal, .modal-overlay").on("click", function (e) {
      if (e.target !== this) return;
      $("#successModal").fadeOut();
    });
  }

  // Form validation
  $(document).ready(initContactForm);
})(jQuery);
