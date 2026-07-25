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
