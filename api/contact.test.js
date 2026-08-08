const test = require('node:test');
const assert = require('node:assert');
const handler = require('./contact');

test('Contact API - Missing Fields Validation', async (t) => {
  // Mock simple res object to capture status and json
  const createMockRes = () => {
    const res = {
      statusCode: null,
      jsonData: null,
      setHeader: () => {}, // Mock setHeader
      status: function(code) {
        this.statusCode = code;
        return this; // For chaining .json()
      },
      json: function(data) {
        this.jsonData = data;
        return this;
      },
      end: function() {
        return this;
      }
    };
    return res;
  };

  await t.test('Returns 400 when missing all required fields', async () => {
    const req = { method: 'POST', body: {} };
    const res = createMockRes();

    await handler(req, res);

    assert.strictEqual(res.statusCode, 400);
    assert.deepStrictEqual(res.jsonData, { message: "Missing required fields (name, email, region, message)" });
  });

  await t.test('Returns 400 when missing name', async () => {
    const req = { method: 'POST', body: { email: 'test@example.com', region: 'US', message: 'Hi' } };
    const res = createMockRes();

    await handler(req, res);

    assert.strictEqual(res.statusCode, 400);
    assert.deepStrictEqual(res.jsonData, { message: "Missing required fields (name, email, region, message)" });
  });

  await t.test('Returns 400 when missing email', async () => {
    const req = { method: 'POST', body: { name: 'John Doe', region: 'US', message: 'Hi' } };
    const res = createMockRes();

    await handler(req, res);

    assert.strictEqual(res.statusCode, 400);
    assert.deepStrictEqual(res.jsonData, { message: "Missing required fields (name, email, region, message)" });
  });

  await t.test('Returns 400 when missing region', async () => {
    const req = { method: 'POST', body: { name: 'John Doe', email: 'test@example.com', message: 'Hi' } };
    const res = createMockRes();

    await handler(req, res);

    assert.strictEqual(res.statusCode, 400);
    assert.deepStrictEqual(res.jsonData, { message: "Missing required fields (name, email, region, message)" });
  });

  await t.test('Returns 400 when missing message', async () => {
    const req = { method: 'POST', body: { name: 'John Doe', email: 'test@example.com', region: 'US' } };
    const res = createMockRes();

    await handler(req, res);

    assert.strictEqual(res.statusCode, 400);
    assert.deepStrictEqual(res.jsonData, { message: "Missing required fields (name, email, region, message)" });
  });
});

test('Contact API - Region Rwanda SMTP Configuration', async (t) => {
  const nodemailer = require('nodemailer');
  const originalEnv = { ...process.env };
  let capturedMailOptions = null;
  let capturedTransportOptions = null;

  t.beforeEach(() => {
    process.env.SMTP_USER_DEFAULT = 'default_user@example.com';
    process.env.SMTP_PASS_DEFAULT = 'default_pass';
    process.env.SMTP_USER_RWANDA = 'rwanda_user@example.com';
    process.env.SMTP_PASS_RWANDA = 'rwanda_pass';

    t.mock.method(nodemailer, 'createTransport', (options) => {
      capturedTransportOptions = options;
      return {
        sendMail: async (mailOptions) => {
          capturedMailOptions = mailOptions;
        }
      };
    });
  });

  t.afterEach(() => {
    process.env = { ...originalEnv };
    t.mock.restoreAll();
    capturedMailOptions = null;
    capturedTransportOptions = null;
  });

  const createMockRes = () => {
    return {
      statusCode: null,
      jsonData: null,
      setHeader: () => {},
      status: function(code) { this.statusCode = code; return this; },
      json: function(data) { this.jsonData = data; return this; },
      end: function() { return this; }
    };
  };

  await t.test('uses Rwanda credentials and sets CC when region is Rwanda', async () => {
    const req = {
      method: 'POST',
      body: {
        name: 'Jane Doe',
        email: 'jane@example.com',
        region: 'Rwanda',
        message: 'Hello'
      }
    };
    const res = createMockRes();

    await handler(req, res);

    assert.strictEqual(res.statusCode, 200);
    assert.deepStrictEqual(res.jsonData, { success: true, message: "Message sent successfully." });

    // Verify transport options
    assert.ok(capturedTransportOptions);
    assert.strictEqual(capturedTransportOptions.auth.user, 'rwanda_user@example.com');
    assert.strictEqual(capturedTransportOptions.auth.pass, 'rwanda_pass');

    // Verify mail options
    assert.ok(capturedMailOptions);
    assert.strictEqual(capturedMailOptions.cc, 'default_user@example.com');
  });

  await t.test('falls back to default credentials when region is not Rwanda', async () => {
    const req = {
      method: 'POST',
      body: {
        name: 'Jane Doe',
        email: 'jane@example.com',
        region: 'Kenya',
        message: 'Hello'
      }
    };
    const res = createMockRes();

    await handler(req, res);

    assert.strictEqual(res.statusCode, 200);
    assert.deepStrictEqual(res.jsonData, { success: true, message: "Message sent successfully." });

    assert.ok(capturedTransportOptions);
    assert.strictEqual(capturedTransportOptions.auth.user, 'default_user@example.com');
    assert.strictEqual(capturedTransportOptions.auth.pass, 'default_pass');
    assert.strictEqual(capturedMailOptions.cc, undefined);
  });
});
