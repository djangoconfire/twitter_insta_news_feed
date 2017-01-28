from django.conf.urls import url

from search import views

urlpatterns = [
    url(r'^search/', views.keyword_search, name='keyword_search'),
    url(r'^$', views.index, name='index'),
]