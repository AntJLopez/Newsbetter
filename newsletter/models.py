from django.db import models


class Newsletter(models.Model):
    published = models.DateTimeField(auto_now_add=False)
