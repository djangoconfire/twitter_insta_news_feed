from django.db import models

# Create your models here.
class NewsFeedConfiguration(models.Model):
    TWITTER = 'TW'
    INSTAGRAM = 'IN'
    API_CHOICES = (
        (TWITTER, 'Twitter'),
        (INSTAGRAM, 'Instagram'),
    )

    api_type                = models.CharField(max_length=2,
                                      choices=API_CHOICES,
                                      default=TWITTER)
    api_name                = models.CharField(max_length=200)
    api_client_id           = models.CharField(max_length=200, blank=True, null=True)
    api_client_secret       = models.CharField(max_length=200)
    api_access_token        = models.CharField(max_length=200, blank=True, null=True)
    api_last_id             = models.CharField(max_length=200, blank=True, null=True)
    insta_hashtag           = models.CharField(max_length=200, blank=True, null=True)
    
    def __unicode__(self):
        return self.api_name


class Post(models.Model):
    TWITTER = 'TW'
    INSTAGRAM = 'IN'
    SOURCE_CHOICES = (
        (TWITTER, 'Twitter'),
        (INSTAGRAM, 'Instagram'),
    )
    user_name               = models.CharField(max_length=200)
    display_name            = models.CharField(max_length=200, blank=True, null=True)
    known_user              = models.BooleanField(default=False)
    source_type             = models.CharField(max_length=2,
                                      choices=SOURCE_CHOICES,
                                      default=TWITTER)
    content                 = models.CharField(max_length=200, blank=True, null=True)
    content_id              = models.CharField(max_length=200, unique=True)
    content_type            = models.CharField(max_length=200, blank=True, null=True)
    thumbnail_link          = models.CharField(max_length=200, blank=True, null=True)
    image_link              = models.CharField(max_length=200, blank=True, null=True)
    has_location            = models.BooleanField(default=False)
    lat                     = models.DecimalField(decimal_places=17,max_digits=20, blank=True, null=True)
    lon                     = models.DecimalField(decimal_places=17,max_digits=20, blank=True, null=True)
    link                    = models.CharField(max_length=200, blank=True, null=True)
    profile_pic             = models.CharField(max_length=200, blank=True, null=True)
    content_date            = models.CharField(max_length=200, blank=True, null=True)
    
    def __unicode__(self):
        return self.user_name  


class Hashtag(models.Model):
    hashtag             = models.CharField(max_length=200)
    tweet_count         = models.IntegerField(default=0)
    verified_count      = models.IntegerField(default=0)
    unverified_count    = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.hashtag
