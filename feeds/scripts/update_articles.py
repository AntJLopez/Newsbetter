from ..models import Feed


def run():
    for feed in Feed.objects.all():
        feed.update_articles()
