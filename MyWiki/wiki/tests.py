from django.test import TestCase, Client
from .models import Page
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .views import upload_file, delete_confirm

# I have created various tests to check my site for errors and problems.
# Varous tests have been used for this to ensure everything is working correctly.

class IndexPageTest(TestCase):

    def test_index_page(self):
        response = self.client.get(reverse('wiki:index'))  # gets the contents of the page.
        self.assertEqual(response.status_code, 200) # Checks if the page responds with the 200 status code.
        self.assertContains(response, "Index") # Checks if the page contains the string value.

    #
    # Tests the index page for a case that presents the following text upon no pages found.
    #
    def test_no_pages(self):
        response = self.client.get(reverse('wiki:index'))  # gets the contents of the page.
        self.assertEqual(response.status_code, 200) # Checks if the page responds with the 200 status code.
        self.assertContains(
            response, "There are currently no wiki's available.") # Checks if the page contains the string value.


class PageCreationTestCase(TestCase):
    def setUp(self):
        page = Page.objects.create(title="hello_world", content="Hello world") # Creates a page called hello_world and adds content.
        page.save() # Saves the page to the database.

        page = Page.objects.create(title="hello world", content="Hello world again") # Creates a page called hello world and adds content.
        page.save() # Saves the page to the database.

        self.user = User.objects.create_user('TestUser', 'TestUser@mywiki.com', 'TestUserpassword') # Creates a user with the credentials specified.

    def test_page_setup_case_1_content(self):
        response = self.client.get('/hello_world/') # gets the contents of the page.
        self.assertContains(response, "Hello world") # compares the pages contents to the string to see if the page contains the text provided.

    def test_page_setup_case_2_content(self):
        response = self.client.get('/hello world/') # gets the contents of the page.
        self.assertContains(response, "Hello world again") # compares the pages contents to the string to see if the page contains the text provided.

    def test_page_deletion_case_2_content(self):
        self.client.login(username='TestUser', password='TestUserpassword') # logs in the test user with the credentials or page will respond with the login screen.
        response = self.client.get('/hello world/edit/delete', follow=True) # gets the contents of the url and follows it
        self.assertContains(response, 'Are you sure you want to delete the following page:') # compares the pages contents to the string to see if the page contains the text provided.

    def test_page_deletion_confirm_case_2_content(self):
        self.client.login(username='TestUser', password='TestUserpassword') # logs in the test user with the credentials or page will respond with the login screen.
        post_response = self.client.post('/hello world/edit/delete/confirm', follow=True)  # gets the contents of the page.
        self.assertRedirects(post_response,'/', status_code=302) # Expects page permanently moved 

class LoginTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('TestUser', 'TestUser@mywiki.com', 'TestUserpassword') # Creates a user with the credentials specified.

    def testLogin(self):
        self.client.login(username='TestUser', password='TestUserpassword') # logs in the test user with the credentials or page will respond with the login screen.
        response = self.client.get(reverse('wiki:index'))  # gets the contents of the page.
        self.assertEqual(response.status_code, 200) # Checks if the page responds with the 200 status code.
        self.assertContains(response, "logout") #compares the pages contents to the string to see if the page contains the text provided.

    def testLogout(self):
        self.client.logout()
        response = self.client.get(reverse('wiki:logout'), follow=True)  # gets the contents of the page.
        self.assertEqual(response.status_code, 200) # Checks if the page responds with the 200 status code.
        self.assertContains(response, "Username:") #compares the pages contents to the string to see if the page contains the text provided.
        
class PageViewTests(TestCase):

    def test_index_view(self):
        response = self.client.get(reverse('wiki:index'))  # gets the contents of the page.
        self.assertEqual(response.status_code, 200) # Checks if the page responds with the 200 status code.
        self.assertContains(response, "Index") #compares the pages contents to the string to see if the page contains the text provided.

    def test_sign_in_page_view(self):
        response = self.client.get('/accounts/login/')  # gets the contents of the page.
        self.assertContains(response, "Sign In") #compares the pages contents to the string to see if the page contains the text provided.

    def test_sign_up_page_view(self):
        response = self.client.get('/accounts/signup')  # gets the contents of the page.
        self.assertContains(response, "Register") #compares the pages contents to the string to see if the page contains the text provided.

    def setUp(self):
        self.user = User.objects.create_user('TestUser', 'TestUser@mywiki.com', 'TestUserpassword') # Creates a user with the credentials specified.

    def test_upload_page_view(self):
        self.client.login(username='TestUser', password='TestUserpassword') # logs in the test user with the credentials or page will respond with the login screen.
        response = self.client.post('/upload/', follow=True)  # gets the contents of the page.
        self.assertContains(response, "Uploaded Files:") #compares the pages contents to the string to see if the page contains the text provided.

    def test_edit_page_view(self):
        self.client.login(username='TestUser', password='TestUserpassword') # logs in the test user with the credentials or page will respond with the login screen.
        response = self.client.post('/PageNotFound/edit', follow=True)  # gets the contents of the page.
        self.assertContains(response, "Editing") #compares the pages contents to the string to see if the page contains the text provided.