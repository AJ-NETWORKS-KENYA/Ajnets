/**
 * AJNETWORKS Contact Form Handler
 * Simple validation for Formspree integration
 */

(function ($) {
  "use strict";

  // Form validation
  $(document).ready(function () {
    var $form = $("#ajax-form");
    var $submitBtn = $("#send");
    var $errorContainer = $("#err-form");

    // Hide all error messages initially
    $(".error").hide();

    // Email validation regex
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    // Real-time validation
    $('input[name="name"]').on("blur", function () {
      if ($(this).val().trim() === "") {
        $("#err-name").show();
      } else {
        $("#err-name").hide();
      }
    });

    $('input[name="organization"]').on("blur", function () {
      if ($(this).val().trim() === "") {
        $("#err-organization").show();
      } else {
        $("#err-organization").hide();
      }
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
      if ($(this).val().trim() === "") {
        $("#err-phone").show();
      } else {
        $("#err-phone").hide();
      }
    });

    // Form submission validation
    $form.on("submit", function (e) {
      // Hide previous messages
      $(".error").hide();
      $errorContainer.hide();

      // Get form values
      var name = $('input[name="name"]').val().trim();
      var organization = $('input[name="organization"]').val().trim();
      var email = $('input[name="email"]').val().trim();
      var phone = $('input[name="phone"]').val().trim();
      var message = $('textarea[name="message"]').val().trim();

      // Validation
      var isValid = true;

      if (name === "") {
        $("#err-name").show();
        isValid = false;
      }

      if (organization === "") {
        $("#err-organization").show();
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

      if (!isValid) {
        e.preventDefault();
        return false;
      }

      // Disable submit button and show loading
      $submitBtn.prop("disabled", true).text("Sending...");

      // Let the form submit naturally to Formspree
      // Formspree will handle the submission and show their confirmation page
      return true;
    });

    // Clear error messages on input
    $form.find("input, textarea").on("input", function () {
      $(this).siblings(".error").hide();
      $errorContainer.hide();
    });
  });
})(jQuery);
