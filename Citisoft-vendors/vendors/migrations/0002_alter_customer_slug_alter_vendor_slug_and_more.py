# Generated by Django 5.0.4 on 2024-04-18 00:16

import django_extensions.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='user', unique=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='business_name', unique=True),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='wishlist_name', unique=True),
        ),
        migrations.AlterField(
            model_name='wishlistentry',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='user', unique=True),
        ),
    ]