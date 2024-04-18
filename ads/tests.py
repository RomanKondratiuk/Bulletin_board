from rest_framework import status
from rest_framework.test import APITestCase

from ads.models import Ad, Comment
from users.models import User
from django.urls import reverse


class AdTestCase(APITestCase):
    """ this is tests for Ad model """

    def setUp(self) -> None:
        # creating user
        self.user = User.objects.create_user(email='test@icloud.com', password='testpassword')

    def test_ad_create(self):
        """ ad creation testing"""

        self.client.force_authenticate(user=self.user)
        data = {
            "title": "test",
            "price": 10,
            "author": self.user.id,
            "description": "this is a creation test"
        }

        response = self.client.post(
            reverse('ads:ad-create'),
            data=data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'id': 1, 'title': 'test', 'price': 10, 'description': 'this is a creation test', 'author': 1}
        )

        self.assertTrue(
            Ad.objects.all().exists()

        )

    def test_ad_list(self):
        """ad list testing"""

        response = self.client.get(
            reverse('ads:ad-list'),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'count': 0, 'next': None, 'previous': None, 'results': []}

        )

    def test_ad_update(self):
        """ ad updating testing"""

        self.client.force_authenticate(user=self.user)

        self.ad = Ad.objects.create(
            title="test",
            price=10,
            description="this is a creation test",
            author=self.user
        )

        updated_data = {
            'title': 'test updated',
            'price': 15,
            "description": "this is a updated test"
        }

        response = self.client.put(
            reverse('ads:ad-update', args=[self.ad.id]),
            data=updated_data
        )
        # if response.status_code != status.HTTP_200_OK:
        #     print(response.data)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.ad.refresh_from_db()
        self.assertEqual(
            self.ad.title,
            updated_data['title']
        )

        self.ad.refresh_from_db()
        self.assertEqual(
            self.ad.description,
            updated_data['description']
        )

        self.ad.refresh_from_db()
        self.assertEqual(
            self.ad.price,
            updated_data['price']
        )

    def test_ad_delete(self):
        """ ad deleting test """

        self.client.force_authenticate(user=self.user)

        self.ad = Ad.objects.create(
            title="test",
            price=10,
            description="this is a creation test",
            author=self.user
        )

        response = self.client.delete(
            reverse('ads:ad-delete', args=[self.ad.id]),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        with self.assertRaises(Ad.DoesNotExist):
            self.ad.refresh_from_db()


class CommentTestCase(APITestCase):
    """ this is tests for Comment model """

    def setUp(self) -> None:
        # creating user
        self.user = User.objects.create_user(email='test@icloud.com', password='testpassword')

    def test_comment_create(self):
        """ comment creation testing"""

        self.client.force_authenticate(user=self.user)

        data = {
            "title": "test",
            "price": 10,
            "author": self.user.id,
            "description": "this is a creation test"
        }

        ad_response = self.client.post(
            reverse('ads:ad-create'),
            data=data,
        )

        ad_id = ad_response.json()['id']

        comment_data = {
            "text": "great ad!",
            "author": self.user.id,
            "ad": ad_id
        }

        comment_response = self.client.post(
            reverse('ads:comment-create'),
            data=comment_data,
        )

        self.assertEqual(
            comment_response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            comment_response.json(),
            {'text': 'great ad!', 'author': 5, 'ad': 4}
        )

        self.assertTrue(
            Comment.objects.all().exists()
        )

    def test_comment_list(self):
        """comment list testing"""

        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            reverse('ads:comments-list'),
        )
        # print(response.json())
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            []
        )

    def test_comment_update(self):
        """ comment updating testing"""

        self.client.force_authenticate(user=self.user)

        data = {
            "title": "test",
            "price": 10,
            "author": self.user.id,
            "description": "this is a creation test"
        }

        ad_response = self.client.post(
            reverse('ads:ad-create'),
            data=data,
        )

        ad_id = ad_response.json()['id']
        ad = Ad.objects.get(id=ad_id)

        self.comment = Comment.objects.create(
            text='great ad!',
            author=self.user,
            ad=ad
        )

        updated_data = {
            'text': 'comment updated'
        }

        response = self.client.put(
            reverse('ads:comment-update', args=[self.comment.id]),
            data=updated_data
        )
        # if response.status_code != status.HTTP_200_OK:
        #     print(response.data)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.comment.refresh_from_db()
        self.assertEqual(
            self.comment.text,
            updated_data['text']
        )

    def test_comment_delete(self):
        """ comment deleting test """

        self.client.force_authenticate(user=self.user)

        data = {
            "title": "test",
            "price": 10,
            "author": self.user.id,
            "description": "this is a creation test"
        }

        ad_response = self.client.post(
            reverse('ads:ad-create'),
            data=data,
        )

        ad_id = ad_response.json()['id']
        ad = Ad.objects.get(id=ad_id)

        self.comment = Comment.objects.create(
            text='great ad!',
            author=self.user,
            ad=ad
        )

        comment_data = {
            "text": "great ad!",
            "author": self.user.id,
            "ad": ad_id
        }

        response = self.client.post(
            reverse('ads:comment-create'),
            data=comment_data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED)

        response = self.client.delete(
            reverse('ads:comment-delete', args=[self.comment.id]),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT)

        with self.assertRaises(Comment.DoesNotExist):
            self.comment.refresh_from_db()
