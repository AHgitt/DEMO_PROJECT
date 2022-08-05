import unittest
import sys
sys.path.append("..")
from app import flask_app


class MyTest(unittest.TestCase):

    def test_index(self):
        tester = flask_app.test_client(self)
        response = tester.get('index', content_type='html/text')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
