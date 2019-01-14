from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Feed, Article
from .forms import ArticleForm


@login_required
def feed_list(request):
    feeds = Feed.objects.all().order_by('title')
    params = {
        'section': 'Feeds',
        'feeds': feeds
    }
    return render(request, 'feeds/feed_list.html', params)


@login_required
def article_list(request):
    articles = Article.objects.all().order_by('-published')
    params = {
        'section': 'Articles',
        'articles': articles
    }
    return render(request, 'feeds/article_list.html', params)


@login_required
def article_edit(request, article_id):
    instance = get_object_or_404(Article, pk=article_id)
    params = {'section': 'Articles', 'article': instance}
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return render(request, 'feeds/article_edited.html', params)
    else:
        form = ArticleForm(instance=instance)

    params['form'] = form
    return render(request, 'feeds/article_edit.html', params)
