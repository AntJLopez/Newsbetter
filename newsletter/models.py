from django.db import models
from django.urls import reverse  # noqa


class Newsletter(models.Model):
    def __str__(self):
        return f'{self.published:%d %b %Y}'

    def get_absolute_url(self):
        return reverse(
            'newsletter_view',
            kwargs={'date': self.published})

    def title(self):
        return f'Newsletter: {self.published.isoformat()}'

    def sections(self):
        sections = set()
        for article in self.articles.all():
            if article.section:
                sections.add(article.section)
        return sections

    published = models.DateField(auto_now_add=False, db_index=True)


class Subscriber(models.Model):
    def __str__(self):
        return self.email

    email = models.EmailField()
    tester = models.BooleanField(default=False)
