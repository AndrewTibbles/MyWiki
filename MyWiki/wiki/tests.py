from django.test import TestCase, Client
from .models import Page
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .views import upload_file, delete_confirm

class IndexPageTest(TestCase):

    def test_index_page(self):
        response = self.client.get(reverse('wiki:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Index")

    #
    # Tests the index page for a case that presents the following text upon no pages found.
    #
    def test_no_pages(self):
        response = self.client.get(reverse('wiki:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response, "There are currently no wiki's available.")


class PageCreationTestCase(TestCase):
    def setUp(self):
        page = Page.objects.create(title="hello_world", content="Hello world")
        page.save()

        page = Page.objects.create(title="hello world", content="Hello world again")
        page.save()

        self.user = User.objects.create_user('TestUser', 'TestUser@mywiki.com', 'TestUserpassword')

    def test_page_setup_case_1_content(self):
        response = self.client.get('/hello_world/')
        self.assertContains(response, "Hello world")

    def test_page_setup_case_2_content(self):
        response = self.client.get('/hello world/')
        self.assertContains(response, "Hello world again")

    def test_page_deletion_case_2_content(self):
        self.client.login(username='TestUser', password='TestUserpassword')
        response = self.client.get('/hello world/edit/delete', follow=True)
        self.assertContains(response, 'Are you sure you want to delete the following page:')

    def test_page_deletion_confirm_case_2_content(self):
        self.client.login(username='TestUser', password='TestUserpassword')
        post_response = self.client.post('/hello world', follow=True)
        self.assertRedirects(post_response,'/hello%20world/', status_code=301) #Expects page permanently moved

class LoginTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('TestUser', 'TestUser@mywiki.com', 'TestUserpassword')

    def testLogin(self):
        self.client.login(username='TestUser', password='TestUserpassword')
        response = self.client.get(reverse('wiki:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "logout")

    def testLogout(self):
        self.client.logout()
        response = self.client.get(reverse('wiki:logout'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Username:")
        
class PageViewTests(TestCase):

    def test_index_view(self):
        response = self.client.get(reverse('wiki:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Index")

    def test_sign_in_page_view(self):
        response = self.client.get('/accounts/login/')
        self.assertContains(response, "Sign In")

    def test_sign_up_page_view(self):
        response = self.client.get('/accounts/signup')
        self.assertContains(response, "Register")

    def setUp(self):
        self.user = User.objects.create_user('TestUser', 'TestUser@mywiki.com', 'TestUserpassword')

    def test_upload_page_view(self):
        self.client.login(username='TestUser', password='TestUserpassword')
        response = self.client.post('/upload/', follow=True)
        self.assertContains(response, "Uploaded Files:")

    def test_edit_page_view(self):
        self.client.login(username='TestUser', password='TestUserpassword')
        response = self.client.post('/PageNotFound/edit', follow=True)
        self.assertContains(response, "Editing")