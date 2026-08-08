/**
 * AJNETWORKS Contact Form Handler
 * Simple validation for Formspree integration
 */

(function ($) {
  "use strict";

  var $form, $submitBtn, $errorContainer;
  var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  function setupRealTimeValidation() {
    var simpleFields = ['name', 'organization', 'phone'];

    $.each(simpleFields, function (i, field) {
      $('input[name="' + field + '"]').on("blur", function () {
        if ($(this).val().trim() === "") {
          $("#err-" + field).show();
        } else {
          $("#err-" + field).hide();
        }
      });
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
  }

  function validateForm() {
    var isValid = true;
    var name = $('input[name="name"]').val().trim();
    var organization = $('input[name="organization"]').val().trim();
    var email = $('input[name="email"]').val().trim();
    var phone = $('input[name="phone"]').val().trim();
    var message = $('textarea[name="message"]').val().trim();
    var region = $('select[name="region"]').val();

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

  function handleAjaxSuccess() {
    $("#successModal").fadeIn();
    $form[0].reset();
    $submitBtn.prop("disabled", false).text("Request Strategy Call");
  }

  function handleAjaxError(xhr, status, error) {
    var msg = "There was an error sending your message. Please try again.";
    try {
      var response = JSON.parse(xhr.responseText);
      if (response && response.message) {
        msg = "Error: " + response.message;
      }
    } catch (e) {}

    if (xhr.status === 404) {
      msg = "Backend API not found. Please ensure you are running the site via Vercel CLI (vercel dev).";
    } else if (xhr.status === 500) {
      msg += " (Server Error: Check your SMTP credentials in .env)";
    }

    $errorContainer.text(msg).show();
    $submitBtn.prop("disabled", false).text("Request Strategy Call");
  }

  function submitFormAjax() {
    $.ajax({
      url: $form.attr("action"),
      method: "POST",
      data: $form.serialize(),
      dataType: "json",
      headers: {
        Accept: "application/json",
      },
      success: handleAjaxSuccess,
      error: handleAjaxError,
    });
  }

  function setupFormSubmission() {
    $form.on("submit", function (e) {
      $(".error").hide();
      $errorContainer.hide();

      if (!validateForm()) {
        e.preventDefault();
        return false;
      }

      $submitBtn.prop("disabled", true).text("Sending...");
      submitFormAjax();

      e.preventDefault();
      return false;
    });
  }

  function setupMiscEvents() {
    $form.find("input, textarea").on("input", function () {
      $(this).siblings(".error").hide();
      $errorContainer.hide();
    });

    $(".close-modal, .modal-overlay").on("click", function (e) {
      if (e.target !== this) return;
      $("#successModal").fadeOut();
    });
  }

  function initContactForm() {
    $form = $("#ajax-form");
    $submitBtn = $("#send");
    $errorContainer = $("#err-form");

    $(".error").hide();

    setupRealTimeValidation();
    setupFormSubmission();
    setupMiscEvents();
  }

  // Form validation entry point
  $(document).ready(initContactForm);
})(jQuery);
