from django.contrib import admin
from .models import *

def up_raiting(modeladmin, request, queryset):
    queryset.update(rating=10.0)
    up_raiting.short_description = 'Установить рейтинг 10.0'

def up_user_rating(modeladmin, request, queryset):
    queryset.update(user_rating=10.0)
    up_user_rating.short_description = 'Установить рейтинг 10.0'

class PostAdmin(admin.ModelAdmin):
    list_display = ('headline', 'data_time_create', 'position', 'rating')
    list_filter = ('position', 'data_time_create')
    search_fields = ('headline', 'data_time_create')
    actions = [up_raiting]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name_category',)

class AutorAdmin(admin.ModelAdmin):
    list_display = ('author', 'user_rating',)
    list_filter = ('author',)
    search_fields = ('author',)
    actions = [up_user_rating]


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)
admin.site.register(PostCategory)
admin.site.register(Author, AutorAdmin)