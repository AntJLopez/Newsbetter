from django.contrib import admin
from django.urls import path, register_converter, include  # noqa
from django.views.generic.base import RedirectView
from feeds import views as f_views
from . import views


admin.site.site_header = 'CI Newsletter Administration Panel'
admin.site.site_title = 'Newsletter Admin'

app_name = 'newsbetter'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('database/', views.database_panel, name='database_panel'),
    path('', RedirectView.as_view(url='articles/')),
    path('feeds/', f_views.feed_list, name='feed_list'),
    path('articles/', f_views.article_list, name='article_list'),
    path('articles/<int:article_id>/', f_views.article_edit,
         name='article_edit'),
    path('newsletters/', include('newsletter.urls')),
]
