# Generated by Django 4.2.2 on 2023-06-21 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='slug',
            field=models.SlugField(editable=False, unique=True),
        ),
    ]
