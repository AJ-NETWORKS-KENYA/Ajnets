const test = require('node:test');
const assert = require('node:assert');
const handler = require('./contact');

test('Contact API - Validation, Honeypot & Security', async (t) => {
  // Mock simple res object to capture status and json
  const createMockRes = () => {
    const res = {
      statusCode: null,
      jsonData: null,
      headers: {},
      setHeader: function(k, v) {
        this.headers[k] = v;
      },
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

  await t.test('Returns 400 for invalid email format', async () => {
    const req = { method: 'POST', body: { name: 'John Doe', email: 'invalid-email', region: 'Kenya', message: 'Hello' } };
    const res = createMockRes();

    await handler(req, res);

    assert.strictEqual(res.statusCode, 400);
    assert.deepStrictEqual(res.jsonData, { message: "Invalid email format" });
  });

  await t.test('Honeypot trap: Returns 200 silent success when bot_field is populated', async () => {
    const req = { 
      method: 'POST', 
      body: { 
        name: 'Spam Bot', 
        email: 'spam@bot.com', 
        region: 'Kenya', 
        message: 'Buy cheap watches',
        bot_field: 'http://spam-link.com' 
      } 
    };
    const res = createMockRes();

    await handler(req, res);

    assert.strictEqual(res.statusCode, 200);
    assert.deepStrictEqual(res.jsonData, { success: true, message: "Consultation request recorded successfully." });
  });

  await t.test('OPTIONS method returns 200 with CORS headers', async () => {
    const req = { method: 'OPTIONS' };
    const res = createMockRes();

    await handler(req, res);

    assert.strictEqual(res.headers["Access-Control-Allow-Origin"], "https://ajnetworks.co");
  });

  await t.test('Method not allowed (GET) returns 405', async () => {
    const req = { method: 'GET' };
    const res = createMockRes();

    await handler(req, res);

    assert.strictEqual(res.statusCode, 405);
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
