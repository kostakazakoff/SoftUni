# Generated by Django 4.2.1 on 2023-06-08 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='tagged_photo',
            new_name='to_photo',
        ),
    ]