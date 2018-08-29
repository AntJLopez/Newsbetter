from django.db import models
from datetime import datetime
import feedparser


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
        return sorted_entries
