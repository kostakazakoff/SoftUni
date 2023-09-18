# Generated by Django 4.2.2 on 2023-06-24 07:48

import django.core.validators
from django.db import migrations, models
import fruitipedia.core.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, validators=[django.core.validators.MinLengthValidator(2), fruitipedia.core.validators.validate_name_start_with_letter])),
                ('last_name', models.CharField(max_length=35, validators=[django.core.validators.MinLengthValidator(1), fruitipedia.core.validators.validate_name_start_with_letter])),
                ('email', models.EmailField(max_length=40)),
                ('passwords', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(8)])),
                ('image_url', models.URLField(blank=True, null=True)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]