from django.test import TestCase


class UrlTest(TestCase):

    def testLibraryPage(self):
        response = self.client.get('library/')
        print(response)

        self.assertEqual(response.status_code, 200)
