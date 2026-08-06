const test = require('node:test');
const assert = require('node:assert');
const handler = require('./contact');

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

test('Contact API - Method Validation', async (t) => {
  await t.test('Returns 405 when method is GET', async () => {
    const req = { method: 'GET' };
    const res = createMockRes();

    await handler(req, res);

    assert.strictEqual(res.statusCode, 405);
    assert.deepStrictEqual(res.jsonData, { message: "Method not allowed" });
  });

  await t.test('Returns 405 when method is PUT', async () => {
    const req = { method: 'PUT' };
    const res = createMockRes();

    await handler(req, res);

    assert.strictEqual(res.statusCode, 405);
    assert.deepStrictEqual(res.jsonData, { message: "Method not allowed" });
  });

  await t.test('Returns 200 when method is OPTIONS', async () => {
    const req = { method: 'OPTIONS' };
    const res = createMockRes();

    await handler(req, res);

    assert.strictEqual(res.statusCode, 200);
  });
});

test('Contact API - Missing Fields Validation', async (t) => {
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
