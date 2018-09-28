from django.contrib import admin
from django.urls import path, include


admin.site.site_header = 'CI Newsletter Administration Panel'
admin.site.site_title = 'Newsletter Admin'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('feeds.urls')),
]
