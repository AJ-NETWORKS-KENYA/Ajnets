const handler = require('./contact');
const nodemailer = require('nodemailer');

// Mock nodemailer
jest.mock('nodemailer');

describe('Contact API Handler', () => {
  let mockReq;
  let mockRes;
  let mockSendMail;
  let originalEnv;

  beforeEach(() => {
    // Reset mocks before each test
    jest.clearAllMocks();

    // Save original process.env
    originalEnv = { ...process.env };

    mockSendMail = jest.fn().mockResolvedValue(true);
    nodemailer.createTransport.mockReturnValue({
      sendMail: mockSendMail,
    });

    mockReq = {
      method: 'POST',
      body: {},
    };

    mockRes = {
      setHeader: jest.fn(),
      status: jest.fn().mockReturnThis(),
      json: jest.fn(),
      end: jest.fn(),
    };
  });

  afterEach(() => {
    // Restore process.env
    process.env = originalEnv;
  });

  it('should handle CORS Preflight (OPTIONS request)', async () => {
    mockReq.method = 'OPTIONS';
    await handler(mockReq, mockRes);

    expect(mockRes.setHeader).toHaveBeenCalledWith('Access-Control-Allow-Origin', 'https://ajnetworks.co');
    expect(mockRes.setHeader).toHaveBeenCalledWith('Access-Control-Allow-Methods', 'POST, OPTIONS');
    expect(mockRes.setHeader).toHaveBeenCalledWith('Access-Control-Allow-Headers', 'Content-Type');
    expect(mockRes.status).toHaveBeenCalledWith(200);
    expect(mockRes.end).toHaveBeenCalled();
  });

  it('should return 405 Method Not Allowed for GET request', async () => {
    mockReq.method = 'GET';
    await handler(mockReq, mockRes);

    expect(mockRes.status).toHaveBeenCalledWith(405);
    expect(mockRes.json).toHaveBeenCalledWith({ message: 'Method not allowed' });
  });

  it('should return 400 for missing required fields', async () => {
    mockReq.body = {
      name: 'Test',
      // missing email, region, message
    };
    await handler(mockReq, mockRes);

    expect(mockRes.status).toHaveBeenCalledWith(400);
    expect(mockRes.json).toHaveBeenCalledWith({ message: 'Missing required fields (name, email, region, message)' });
  });

  it('should return 400 for invalid email format', async () => {
    mockReq.body = {
      name: 'Test',
      email: 'invalid-email',
      region: 'Kenya',
      message: 'Hello'
    };
    await handler(mockReq, mockRes);

    expect(mockRes.status).toHaveBeenCalledWith(400);
    expect(mockRes.json).toHaveBeenCalledWith({ message: 'Invalid email format' });
  });

  it('should return 200 with fallback message if SMTP is not configured', async () => {
    delete process.env.SMTP_USER_DEFAULT;
    delete process.env.SMTP_PASS_DEFAULT;

    mockReq.body = {
      name: 'Test',
      email: 'test@example.com',
      region: 'Kenya',
      message: 'Hello'
    };
    await handler(mockReq, mockRes);

    expect(mockRes.status).toHaveBeenCalledWith(200);
    expect(mockRes.json).toHaveBeenCalledWith({ success: true, message: 'Consultation request recorded successfully.' });
    expect(nodemailer.createTransport).not.toHaveBeenCalled();
  });

  it('should dispatch email successfully for default region', async () => {
    process.env.SMTP_USER_DEFAULT = 'default@test.com';
    process.env.SMTP_PASS_DEFAULT = 'password';

    mockReq.body = {
      name: 'Test Name',
      organization: 'Test Org',
      email: 'test@example.com',
      region: 'Kenya',
      phone: '1234567890',
      message: 'Hello'
    };
    await handler(mockReq, mockRes);

    expect(nodemailer.createTransport).toHaveBeenCalledWith(expect.objectContaining({
      auth: {
        user: 'default@test.com',
        pass: 'password',
      }
    }));
    expect(mockSendMail).toHaveBeenCalledWith(expect.objectContaining({
      from: 'default@test.com',
      to: 'default@test.com',
      replyTo: 'test@example.com',
      subject: 'New Consultation Request from Test Name (Test Org) - Region: Kenya',
    }));
    expect(mockRes.status).toHaveBeenCalledWith(200);
    expect(mockRes.json).toHaveBeenCalledWith({ success: true, message: 'Message sent successfully.' });
  });

  it('should dispatch email successfully for Rwanda region with CC', async () => {
    process.env.SMTP_USER_DEFAULT = 'default@test.com';
    process.env.SMTP_PASS_DEFAULT = 'password';
    process.env.SMTP_USER_RWANDA = 'rwanda@test.com';
    process.env.SMTP_PASS_RWANDA = 'rwanda-password';

    mockReq.body = {
      name: 'Test Name',
      email: 'test@example.com',
      region: 'Rwanda',
      message: 'Hello'
    };
    await handler(mockReq, mockRes);

    expect(nodemailer.createTransport).toHaveBeenCalledWith(expect.objectContaining({
      auth: {
        user: 'rwanda@test.com',
        pass: 'rwanda-password',
      }
    }));
    expect(mockSendMail).toHaveBeenCalledWith(expect.objectContaining({
      from: 'rwanda@test.com',
      to: 'rwanda@test.com',
      cc: 'default@test.com',
    }));
    expect(mockRes.status).toHaveBeenCalledWith(200);
    expect(mockRes.json).toHaveBeenCalledWith({ success: true, message: 'Message sent successfully.' });
  });

  it('should return 500 if sendMail throws an error', async () => {
    process.env.SMTP_USER_DEFAULT = 'default@test.com';
    process.env.SMTP_PASS_DEFAULT = 'password';

    mockSendMail.mockRejectedValue(new Error('SMTP Error'));

    mockReq.body = {
      name: 'Test Name',
      email: 'test@example.com',
      region: 'Kenya',
      message: 'Hello'
    };
    await handler(mockReq, mockRes);

    expect(mockRes.status).toHaveBeenCalledWith(500);
    expect(mockRes.json).toHaveBeenCalledWith({ success: false, message: 'Error dispatching email message.' });
  });
});
