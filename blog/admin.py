from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


# Now tell admin our text fileds are going to be summer note fields
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    # The variable names tell the django what should be displayed
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')


# Register your models here.
# admin.site.register(Post)
