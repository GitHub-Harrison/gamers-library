from django.test import TestCase


class UrlTest(TestCase):

    def testHomePage(self):
        response = self.client.get('/')
        print(response)

        self.assertEqual(response.status_code, 200)
