from django.shortcuts import render
from .models import Feed


def feed_list(request):
    feeds = Feed.objects.all().order_by('title')
    return render(request, 'feeds/feed_list.html', {'feeds': feeds})


def home(request):
    return render(request, 'newsbetter/home.html')
