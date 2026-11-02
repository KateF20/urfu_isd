import unittest

from app import app

client = app.test_client()
response = client.get("/")


class MyTestCase(unittest.TestCase):
    def test_status(self):
        self.assertEqual(response.status_code, 200)

    def test_response(self):
        self.assertEqual(response.data, b'Hello from Heroku!')


if __name__ == '__main__':
    unittest.main()
