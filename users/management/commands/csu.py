from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='roma.kondratiuk00@icloud.com',
            first_name='Roman',
            last_name='Kondratiuk',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('roma_2001')
        user.save()
