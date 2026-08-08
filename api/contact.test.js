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

const nodemailer = require('nodemailer');

test('Contact API - Email Dispatch', async (t) => {
  const createMockRes = () => {
    const res = {
      statusCode: null,
      jsonData: null,
      setHeader: () => {},
      status: function(code) {
        this.statusCode = code;
        return this;
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

  await t.test('Returns 500 when email dispatch fails', async () => {
    const req = { method: 'POST', body: { name: 'John Doe', email: 'test@example.com', region: 'US', message: 'Hi' } };
    const res = createMockRes();

    process.env.SMTP_USER_DEFAULT = 'test_user';
    process.env.SMTP_PASS_DEFAULT = 'test_pass';

    t.mock.method(nodemailer, 'createTransport', () => {
      return {
        sendMail: async () => { throw new Error('Mock Dispatch Error'); }
      };
    });

    await handler(req, res);

    assert.strictEqual(res.statusCode, 500);
    assert.deepStrictEqual(res.jsonData, { success: false, message: "Error dispatching email message." });

    delete process.env.SMTP_USER_DEFAULT;
    delete process.env.SMTP_PASS_DEFAULT;
  });
});
