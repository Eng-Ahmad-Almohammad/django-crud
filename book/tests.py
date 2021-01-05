from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Book_shelf
# Create your tests here.
class BookCRUD(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'ahmad',
            email = 'ahmad@gmail.com',
            password = '123ahmad',
        )
        self.book = Book_shelf.objects.create(
            title = 'Thanks',
            author = self.user,
            body = "Thanks Django",
        )

    def test_home_view_status(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
    
    def test_book_details_status(self):
        response = self.client.get(reverse('details', args=['1']))
        self.assertEqual(response.status_code , 200)

    def test_book_details_content(self):
        response = self.client.get(reverse('details', args=['1']))
        self.assertContains(response , 'Thanks')
    
    def test_book_update_content(self):
        response = self.client.post(reverse('update', args=['1']),{
            'title':'Hello'
        })
        self.assertContains(response , 'Hello')

   