from django.contrib import admin

from .models import Serials, Comments

@admin.action(description='Опубликовать')
def make_published(self, request, queryset):
    queryset.update(is_published=True)


@admin.action(description='Снять с публикации')
def make_unpublished(self, request, queryset):
    queryset.update(is_published=False)

@admin.register(Serials)
class SerialsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', 'subtitle')}
    list_display = ('title', 'genre', 'date_published')
    date_hierarchy = 'date_published'
    list_filter = ('is_published', )
    readonly_fields = ('date_published', )
    actions = (make_published, make_unpublished)
    search_fields = ('title', 'id', 'subtitle')


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('author', 'serial', 'text')
    date_hierarchy = 'date_published'
    list_filter = ('is_published', )
    readonly_fields = ('date_published', )
    actions = (make_published, make_unpublished)
    search_fields = ('author', 'serial', 'text')
