from django.contrib import admin

from .models import Section, Article


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'is_visible')
    list_display_links = ('id', 'name')
    list_editable = ('is_visible',)
    list_filter = ('is_visible',)
    search_fields = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'updated', 'section', 'user', 'is_visible')
    list_display_links = ('id', 'name')
    list_editable = ('is_visible',)
    list_filter = ('is_visible', 'updated')
    search_fields = ('name', 'slug', 'text')
    prepopulated_fields = {"slug": ("name",)}


