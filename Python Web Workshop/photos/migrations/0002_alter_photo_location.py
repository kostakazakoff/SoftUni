# Generated by Django 4.2.1 on 2023-06-07 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='location',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
