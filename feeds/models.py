from django.db import models
import feedparser


class Feed(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.title

    def new_articles(self):
        return feedparser.parse(self.link).entries
