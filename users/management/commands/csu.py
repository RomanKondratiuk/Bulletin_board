from django.contrib.auth import get_user_model
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = get_user_model()
        user = user.objects.create(
            email='roma.kondratiuk@icloud.com',
            first_name='Roman',
            last_name='Kondratiuk',
            is_staff=True,
            is_superuser=True,
            role='admin'
        )

        user.set_password('roma_2001')
        user.save()
        self.stdout.write(self.style.SUCCESS('Successfully created new super user'))
