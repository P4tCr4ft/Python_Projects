# Generated by Django 3.2.9 on 2022-06-18 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movielist_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='test_active',
            field=models.BooleanField(default=True),
        ),
    ]