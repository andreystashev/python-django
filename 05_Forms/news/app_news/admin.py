from django.contrib import admin
from .models import NewsItem, Comment


class CommentInLine(admin.TabularInline):
    model = Comment



class NewsItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_active')
    list_filter = ('is_active',)
    exclude = ('description',)
    inlines = (CommentInLine,)
    actions = ('mark_as_active', 'mark_as_inactive')

    def mark_as_active(self, request, queryset):
        queryset.update(is_active=True)

    def mark_as_inactive(self, request, queryset):
        queryset.update(is_active=False)

    mark_as_active.short_description = 'Cтатус "Активно"'
    mark_as_inactive.short_description = 'Cтатус "Не Активно"'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'short_comment')
    list_filter = ('user',)
    search_fields = ('user',)
    actions = ('deleted_by_admin',)

    def deleted_by_admin(self, request, queryset):
        queryset.update(comment='Удалено администратором')

    def short_comment(self, obj):
        if len(obj.comment) > 15:
            return obj.comment[:15]+'...'
        else:
            return obj.comment

    short_comment.short_description = 'short_comment'
    deleted_by_admin.short_description = 'Перевести в статус "Удалено администратором"'


admin.site.register(NewsItem, NewsItemAdmin)
admin.site.register(Comment, CommentAdmin)

