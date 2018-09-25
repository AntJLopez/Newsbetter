from django.db import models, IntegrityError
from datetime import datetime
import feedparser
import dateparser
import requests


class Feed(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.title

    def new_articles(self):
        entries = feedparser.parse(self.link).entries
        for entry in entries:
            timestamp = datetime(*entry.published_parsed[0:6])
            entry.published_date = timestamp
        sorted_entries = sorted(
            entries, key=lambda k: k.published_date, reverse=True)
        # self.update_articles()
        return sorted_entries

    def update_articles(self):
        entries = feedparser.parse(self.link).entries
        for entry in entries:
            a = Article(
                title=entry.title,
                description=entry.description,
                published=dateparser.parse(entry.published),
                link=entry.link,
                feed=self)
            try:
                a.save()
            except IntegrityError:
                # This article is already in the database
                pass


class Article(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    published = models.DateTimeField(db_index=True)
    link = models.URLField()
    html = models.TextField()
    feed = models.ForeignKey(Feed, null=True, on_delete=models.SET_NULL)

    __original_link = None

    def __str__(self):
        return self.title

    def __init__(self, *args, **kwargs):
        super(Article, self).__init__(*args, **kwargs)
        self.__original_link = self.link

    def save(self):
        if not self.id or self.link != self.__original_link:
            self.html = requests.get(self.link).text
            self.__original_link = self.link
        super(Article, self).save()

    class Meta:
        unique_together = ('feed', 'title', 'published')
