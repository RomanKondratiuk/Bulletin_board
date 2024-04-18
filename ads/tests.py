from rest_framework import status
from rest_framework.test import APITestCase

from ads.models import Ad
from users.models import User
from django.urls import reverse


class AdTestCase(APITestCase):

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
        if response.status_code != status.HTTP_200_OK:
            print(response.data)

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


