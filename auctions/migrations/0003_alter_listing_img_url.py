# Generated by Django 5.0.6 on 2024-06-06 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_listing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='img_url',
            field=models.URLField(blank=True, max_length=256),
        ),
    ]
