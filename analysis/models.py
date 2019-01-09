from django.db import models


class Company(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Companies'


class Section(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)


class Segment(models.Model):
    def __str__(self):
        if self.parent:
            return f'{str(self.parent)} | {self.name}'
        return self.name

    name = models.CharField(max_length=50)
    parent = models.ForeignKey(
        'self', blank=True, null=True, related_name='children',
        on_delete=models.CASCADE)
