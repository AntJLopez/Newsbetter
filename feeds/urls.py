from django.urls import path
from django.views.generic.base import RedirectView
from . import views


urlpatterns = [
    path('', RedirectView.as_view(url='feeds/')),
    path('feeds/', views.feed_list, name='feed_list'),
    path('articles/', views.article_list, name='article_list'),
]
