# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hashtag', models.CharField(max_length=200)),
                ('tweet_count', models.IntegerField(default=0)),
                ('verified_count', models.IntegerField(default=0)),
                ('unverified_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='NewsFeedConfiguration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('api_type', models.CharField(default=b'TW', max_length=2, choices=[(b'TW', b'Twitter'), (b'IN', b'Instagram')])),
                ('api_name', models.CharField(max_length=200)),
                ('api_client_id', models.CharField(max_length=200, null=True, blank=True)),
                ('api_client_secret', models.CharField(max_length=200)),
                ('api_access_token', models.CharField(max_length=200, null=True, blank=True)),
                ('api_last_id', models.CharField(max_length=200, null=True, blank=True)),
                ('insta_hashtag', models.CharField(max_length=200, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=200)),
                ('display_name', models.CharField(max_length=200, null=True, blank=True)),
                ('known_user', models.BooleanField(default=False)),
                ('source_type', models.CharField(default=b'TW', max_length=2, choices=[(b'TW', b'Twitter'), (b'IN', b'Instagram')])),
                ('content', models.CharField(max_length=200, null=True, blank=True)),
                ('content_id', models.CharField(unique=True, max_length=200)),
                ('content_type', models.CharField(max_length=200, null=True, blank=True)),
                ('thumbnail_link', models.CharField(max_length=200, null=True, blank=True)),
                ('image_link', models.CharField(max_length=200, null=True, blank=True)),
                ('has_location', models.BooleanField(default=False)),
                ('lat', models.DecimalField(null=True, max_digits=20, decimal_places=17, blank=True)),
                ('lon', models.DecimalField(null=True, max_digits=20, decimal_places=17, blank=True)),
                ('link', models.CharField(max_length=200, null=True, blank=True)),
                ('profile_pic', models.CharField(max_length=200, null=True, blank=True)),
                ('content_date', models.CharField(max_length=200, null=True, blank=True)),
            ],
        ),
    ]
