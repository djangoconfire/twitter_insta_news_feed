from django.conf.urls import url

from search import views

urlpatterns = [
    url(r'^search/tweets/', views.search_tweets, name='search_tweets'),
    url(r'^search/insta/', views.search_insta, name='search_insta'),
    url(r'^$', views.index, name='index'),
]