from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
# Now tell admin our text fileds are going to be summer note fields
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    # The variable names tell the django what should be displayed
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    # actions will allow admin to perform differnt actions, bt
    # default there is only delete, REMEMBER Comments table have
    # approved that is bydefault false set by us
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
# admin.site.register(Post)
