from django.urls import reverse  # new
from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve  # new
# Create your tests here.
from django.test import SimpleTestCase
from django.urls import reverse
from .forms import UserRegisterForm
from .views import register


class HomepageTests(SimpleTestCase):

    def test_homepage_status_code(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url_name(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)


class SignupPageTests(TestCase):
    def setUp(self):
        url = reverse('login')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'users/login.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.')


class SignupPageTests(TestCase):
    def setUp(self):
        url = reverse('register')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'users/register.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.')

    def test_signup_form(self):  # new
        form = self.response.context.get('form')
        self.assertIsInstance(form, UserRegisterForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_signup_view(self):  # new
        view = resolve('/register/')
        self.assertEqual(
            view.func.__name__,
            register.__name__
        )
