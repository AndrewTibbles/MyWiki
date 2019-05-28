from django.test import TestCase, Client
from .models import Page
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect

class RunningTest(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def this_wont_run(self):
        print('Fail')

    def test_this_will(self):
        print('Win')


class PageNoneTest(TestCase):

    #
    # Tests the index page for a case that presents the following text upon no pages found.
    #
    def test_no_pages(self):
        response = self.client.get(reverse('wiki:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response, "There are currently no wiki's available.")


class IndexPageTest(TestCase):

    def test_index_page(self):
        response = self.client.get(reverse('wiki:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Index")


class PageCreationTestCase(TestCase):
    def setUp(self):
        page = Page.objects.create(title="hello_world", content="Hello world")
        page.save()

        page = Page.objects.create(title="hello world", content="Hello world again")
        page.save()

    def test_page_setup_case_1_content(self):
        response = self.client.get('/hello_world/')
        self.assertContains(response, "Hello world")

    def test_page_setup_case_2_content(self):
        response = self.client.get('/hello world/')
        self.assertContains(response, "Hello world again")
        
class PageNavigationTestCase(TestCase):
    client = Client()
    def text_index_page(self):
        response = self.client.get(reverse('wiki:index'))
        response.status_code
        self.assertEqual(response.status_code(), 200)
    
    def test_hello_world_page(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        get_page = Page(title="HelloWorld")
        url = reverse('wiki:detail', args=(Page.title,))
        response = self.client.get(url)
        self.assertContains(response, get_page.content)

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

    #def test_upload_page_view(self):
    #    response = self.client.get('/upload/')
    #    self.assertContains(response, "Uploaded Files:")