# Generated by Django 2.2.4 on 2020-05-02 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Listings', '0002_remove_listing_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='des2',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
    ]
