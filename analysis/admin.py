from django.contrib import admin
from .models import Company, Section, Segment


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    pass


@admin.register(Segment)
class SegmentAdmin(admin.ModelAdmin):
    pass
