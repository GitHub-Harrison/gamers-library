from django.test import TestCase


class UrlTest(TestCase):

    def testAddGamePage(self):
        response = self.client.get('add_game/')
        print(response)

        self.assertEqual(response.status_code, 200)
