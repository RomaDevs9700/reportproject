from django.test import TestCase
from django.urls import reverse
from .models import Post

# Create your tests here.

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(title='Mavzu', text='Yangilik matni')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_title = f"{ post.title }"
        expected_object_text = f"{ post.text }"
        self.assertEqual(expected_object_title, 'Mavzu')
        self.assertEqual(expected_object_text, 'Yangilik matni')

class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(title='Mavzu 2', text='boshqa yangilik')

    def test_views_url_exists_at_proper_location(self):
        reps = self.client.get('/')
        self.assertEqual(reps.status_code, 200)

    def test_view_url_by_name(self):
        reps = self.client.get(reverse('home'))
        self.assertEqual(reps.status_code, 200)

    def test_view_uses_correct_template(self):
        reps = self.client.get(reverse('home'))
        self.assertEqual(reps.status_code, 200)
        self.assertTemplateUsed(reps, 'home.html')

