from django.contrib import admin
from .models import Newsletter, Subscriber


@admin.register(Newsletter)
class FeedAdmin(admin.ModelAdmin):
    pass


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    pass
