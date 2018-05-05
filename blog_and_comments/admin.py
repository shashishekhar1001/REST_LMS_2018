from django.contrib import admin
from .models import *
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('title',)}
    list_display = ["title", "created", "updated", "publish", "draft"]
    list_display_links = ["updated"]
    list_editable = ["title"]
    list_filter = ["updated", "created", "title", "publish", "draft"]
    search_fields = ["title", "content"]
    class Meta:
        model = Blog



admin.site.register(Blog, BlogAdmin)