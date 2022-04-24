from django.test import TestCase
from .models import Post, Comment


class PostTest(TestCase):

    def test_post_model_str(self):
        title = Post.objects.create(title="Django Testing")
        self.assertEqual(str(title), "Django Testing")


class UrlTest(TestCase):
    def testLibraryPage(self):
        response = self.client.get('library/')
        print(response)

        self.assertEqual(response.status_code, 200)
