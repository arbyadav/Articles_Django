from django.conf.urls import include, re_path, url
from django.urls import path
from . import views

urlpatterns = [
    re_path(r'^all/$', views.articles_all),
    re_path(r'^get/(?P<article_id>\d+)/$', views.article_get),
    # url(r'^get/article/(?P<article_id>\d+)/$',views.article_get),
    re_path(r'^language/(?P<language>[a-z\-]+)/$', views.language),
    re_path(r'^create_article/$', views.create_article),
    re_path(r'^like/(?P<article_id>\d+)$', views.like_article),
    re_path(r'^search/$', views.search_titles),
    # re_path(r'^add_comment/(?P<article_id>\d+)$', views.add_comment_article),
]
