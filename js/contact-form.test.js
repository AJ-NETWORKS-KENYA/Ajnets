const test = require('node:test');
const assert = require('node:assert');
const { JSDOM } = require('jsdom');
const fs = require('fs');
const path = require('path');

const contactFormCode = fs.readFileSync(path.join(__dirname, 'contact-form.js'), 'utf-8');

test('Contact Form Validation', async (t) => {

  const setupDOM = () => {
    const dom = new JSDOM(`
      <html>
        <body>
          <form id="ajax-form" action="/api/contact">
            <span class="error" id="err-name" style="display: none;">please enter name</span>
            <input name="name" type="text" />

            <span class="error" id="err-organization" style="display: none;">please enter organization</span>
            <input name="organization" type="text" />

            <span class="error" id="err-region" style="display: none;">please select your region</span>
            <select name="region" id="region">
              <option value="">Select</option>
              <option value="Kenya">Kenya</option>
            </select>

            <span class="error" id="err-email" style="display: none;">please enter e-mail</span>
            <span class="error" id="err-emailvld" style="display: none;">invalid email</span>
            <input name="email" type="email" />

            <span class="error" id="err-phone" style="display: none;">please enter phone number</span>
            <input name="phone" type="tel" />

            <textarea name="message"></textarea>

            <button id="send" type="submit">Send</button>

            <div id="err-form" class="error" style="display: none;"></div>
            <div id="successModal" style="display: none;"></div>
          </form>
        </body>
      </html>
    `, {
      runScripts: 'dangerously'
    });

    const window = dom.window;
    const document = window.document;

    // Polyfill global window and document
    global.window = window;
    global.document = document;

    // Require jquery fresh for this window
    delete require.cache[require.resolve('jquery')];
    const $ = require('jquery');

    // Provide jQuery to the window
    window.jQuery = window.$ = $;
    global.jQuery = global.$ = $;

    $.fn.ready = function(fn) {
      fn();
    };

    // Evaluate our form script
    window.eval(contactFormCode);

    return { window, document, $ };
  };

  const teardownDOM = () => {
    delete global.window;
    delete global.document;
    delete global.jQuery;
    delete global.$;
  };

  t.afterEach(() => {
    teardownDOM();
  });

  await t.test('Initial state: all error messages should be hidden', () => {
    const { document } = setupDOM();
    assert.strictEqual(document.getElementById('err-name').style.display, 'none');
  });

  await t.test('Blur on empty name shows error', () => {
    const { document, $ } = setupDOM();
    $('input[name="name"]').trigger('blur');
    assert.notStrictEqual(document.getElementById('err-name').style.display, 'none');
  });

  await t.test('Blur on valid name hides error', () => {
    const { document, $ } = setupDOM();
    const nameInput = $('input[name="name"]');
    nameInput.val('John Doe');
    nameInput.trigger('blur');
    assert.strictEqual(document.getElementById('err-name').style.display, 'none');
  });

  await t.test('Blur on empty email shows err-email, hides err-emailvld', () => {
    const { document, $ } = setupDOM();
    $('input[name="email"]').trigger('blur');
    assert.notStrictEqual(document.getElementById('err-email').style.display, 'none');
    assert.strictEqual(document.getElementById('err-emailvld').style.display, 'none');
  });

  await t.test('Blur on invalid email shows err-emailvld, hides err-email', () => {
    const { document, $ } = setupDOM();
    const emailInput = $('input[name="email"]');
    emailInput.val('invalid-email');
    emailInput.trigger('blur');
    assert.notStrictEqual(document.getElementById('err-emailvld').style.display, 'none');
    assert.strictEqual(document.getElementById('err-email').style.display, 'none');
  });

  await t.test('Blur on valid email hides both errors', () => {
    const { document, $ } = setupDOM();
    const emailInput = $('input[name="email"]');
    emailInput.val('test@example.com');
    emailInput.trigger('blur');
    assert.strictEqual(document.getElementById('err-email').style.display, 'none');
    assert.strictEqual(document.getElementById('err-emailvld').style.display, 'none');
  });

  await t.test('Form submission with empty fields prevents default and shows errors', () => {
    const { document, $ } = setupDOM();
    const event = $.Event('submit');
    $('#ajax-form').trigger(event);

    assert.strictEqual(event.isDefaultPrevented(), true);
    assert.notStrictEqual(document.getElementById('err-name').style.display, 'none');
    assert.notStrictEqual(document.getElementById('err-organization').style.display, 'none');
    assert.notStrictEqual(document.getElementById('err-region').style.display, 'none');
    assert.notStrictEqual(document.getElementById('err-email').style.display, 'none');
    assert.notStrictEqual(document.getElementById('err-phone').style.display, 'none');
    assert.strictEqual(document.getElementById('err-form').textContent, 'Please provide a detailed message (at least 10 characters)');
  });

  await t.test('Form submission with invalid email prevents default and shows format error', () => {
    const { document, $ } = setupDOM();
    $('input[name="name"]').val('John Doe');
    $('input[name="organization"]').val('ACME Corp');
    $('select[name="region"]').val('Kenya');
    $('input[name="email"]').val('invalid-email');
    $('input[name="phone"]').val('1234567890');
    $('textarea[name="message"]').val('This is a test message that is long enough.');

    const event = $.Event('submit');
    $('#ajax-form').trigger(event);

    assert.strictEqual(event.isDefaultPrevented(), true);
    assert.strictEqual(document.getElementById('err-email').style.display, 'none');
    assert.notStrictEqual(document.getElementById('err-emailvld').style.display, 'none');
  });

  await t.test('Form submission with valid fields triggers AJAX', () => {
    const { $, document } = setupDOM();
    $('input[name="name"]').val('John Doe');
    $('input[name="organization"]').val('ACME Corp');
    $('select[name="region"]').val('Kenya');
    $('input[name="email"]').val('test@example.com');
    $('input[name="phone"]').val('1234567890');
    $('textarea[name="message"]').val('This is a test message that is long enough.');

    // Mock $.ajax
    let ajaxCalled = false;
    $.ajax = function(options) {
      ajaxCalled = true;
    };

    const event = $.Event('submit');
    $('#ajax-form').trigger(event);

    assert.strictEqual(event.isDefaultPrevented(), true);
    assert.strictEqual(ajaxCalled, true);
    assert.strictEqual($('#send').prop('disabled'), true);
  });

  await t.test('Typing in input clears errors', () => {
    const { document, $ } = setupDOM();
    // Show some errors first
    const event = $.Event('submit');
    $('#ajax-form').trigger(event);

    assert.notStrictEqual(document.getElementById('err-name').style.display, 'none');

    // Type in input
    $('input[name="name"]').trigger('input');

    assert.strictEqual(document.getElementById('err-name').style.display, 'none');
    assert.strictEqual(document.getElementById('err-form').style.display, 'none');
  });
});
