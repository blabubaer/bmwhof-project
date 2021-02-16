from django.contrib import admin
from .models import Blog, Image

class ImageInline(admin.TabularInline):
    model = Image

class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    inlines = [ImageInline]

admin.site.register(Blog, BlogAdmin)