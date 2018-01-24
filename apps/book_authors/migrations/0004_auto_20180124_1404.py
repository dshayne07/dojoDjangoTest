# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-24 19:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0003_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='users',
            name='liked_books',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.AddField(
            model_name='book',
            name='liked_users',
            field=models.ManyToManyField(related_name='liked_books', to='book_authors.User'),
        ),
        migrations.AddField(
            model_name='book',
            name='users',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='uploader', to='book_authors.User'),
            preserve_default=False,
        ),
    ]
