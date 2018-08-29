from django.contrib import admin

from .models import Feed


@admin.register(Feed)
class PostAdmin(admin.ModelAdmin):
    pass
