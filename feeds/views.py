from django.shortcuts import render
from .models import Feed, Article


def feed_list(request):
    feeds = Feed.objects.all().order_by('title')
    params = {
        'section': 'Feeds',
        'feeds': feeds
    }
    return render(request, 'feeds/feed_list.html', params)


def article_list(request):
    articles = Article.objects.all().order_by('-published')
    params = {
        'section': 'Articles',
        'articles': articles
    }
    return render(request, 'feeds/article_list.html', params)
