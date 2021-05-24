from django.contrib import admin

from .models import Author, Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date")
    list_display = ("title", "date", "author")
    prepopulated_fields = {"slug": ("title", )}


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagsAdmin(admin.ModelAdmin):
    pass
