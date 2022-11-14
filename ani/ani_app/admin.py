from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Serials, Comments, Series , Categories, User

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

@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('title', 'season')}

    list_display = ('title', 'season', 'serial','date_published','slug')
    date_hierarchy = 'date_published'
    list_filter = ('is_published', )
    readonly_fields = ('date_published', )
    actions = (make_published, make_unpublished)
    search_fields = ('title', 'season', 'serial','date_published','slug')



@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('title','count')}

    list_display = ('title', 'count')
    actions = (make_published, make_unpublished)
    search_fields = ('title', 'count', 'serial')

