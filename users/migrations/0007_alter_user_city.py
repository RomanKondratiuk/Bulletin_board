# Generated by Django 3.2.6 on 2024-04-15 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_is_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=35, verbose_name='city'),
        ),
    ]
