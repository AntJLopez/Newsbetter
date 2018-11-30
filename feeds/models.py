from django.db import models, IntegrityError
from django.urls import reverse
from datetime import datetime
import feedparser
import dateparser
import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup
from analysis.models import Company, Section, Segment
from newsletter.models import Newsletter


class Feed(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField()
    companies = models.ManyToManyField(Company, related_name='feeds')

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
                summary=entry.description,
                published=dateparser.parse(entry.published),
                link=entry.link,
                feed=self,
            )
            try:
                a.save()
            except IntegrityError:
                # This article is already in the database
                pass


class Article(models.Model):
    title = models.CharField(max_length=250)
    link = models.URLField(max_length=500)
    published = models.DateTimeField(db_index=True)
    bookmark = models.BooleanField(default=False)
    feed = models.ForeignKey(Feed, null=True, on_delete=models.SET_NULL)
    summary = models.TextField(blank=True)
    implications = models.TextField(blank=True)
    section = models.ForeignKey(
        Section, blank=True, null=True, related_name='articles',
        on_delete=models.SET_NULL)
    segments = models.ManyToManyField(
        Segment, blank=True, related_name='articles')
    companies = models.ManyToManyField(
        Company, blank=True, related_name='articles')
    newsletter = models.ForeignKey(
        Newsletter, blank=True, null=True, related_name='articles',
        on_delete=models.SET_NULL)
    html = models.TextField(blank=True)

    __original_link = None

    def __str__(self):
        return self.title

    def __init__(self, *args, **kwargs):
        super(Article, self).__init__(*args, **kwargs)
        # self.companies.add(self.feed.companies)
        self.__original_link = self.link

    def get_absolute_url(self):
        return reverse('article_edit', kwargs={'article_id': self.pk})

    def main_segments(self):
        return [s for s in self.segments.all() if not s.parent]

    def save(self):
        first_save = not bool(self.pk)
        if first_save or self.link != self.__original_link:
            try:
                response = requests.get(self.link)
                soup = BeautifulSoup(response.content, 'lxml')
                self.html = response.text
                # Try to find a description, based on the first paragraph
                # with 30 words
                for paragraph in soup('p'):
                    text = paragraph.string
                    words = len(text.split()) if text else 0
                    if words >= 30:
                        # We found a paragraph with 30 words
                        text = ' '.join(text.split())  # Collapse spaces
                        self.summary = text
                        break
            except ConnectionError:
                # Could not connect to link
                pass
            self.__original_link = self.link
        super(Article, self).save()
        if first_save:
            for company in self.feed.companies.all():
                self.companies.add(company)
            self.save()

    class Meta:
        unique_together = ('feed', 'title', 'published')
