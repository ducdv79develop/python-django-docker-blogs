from django.contrib import admin
from blog.models import Blog
from blog.forms import CustomBlogForm
from django.utils import timezone


# Register your models here.
@admin.action(description='Mark selected stories as published')
def make_published(modelAdmin, request, queryset):
    queryset.update(public_flag=True)


@admin.action(description='Move to Trash')
def make_soft_delete(modelAdmin, request, queryset):
    queryset.update(deleted_at=timezone.now())


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'status', 'public_flag', 'deleted_at']
    list_filter = ['title', 'content', 'status', 'public_flag']
    ordering = ['title']
    actions = [make_published, make_soft_delete]
    form = CustomBlogForm

    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': 'Danh sach Blog'}
        return super(BlogAdmin, self).changelist_view(request, extra_context=extra_context)

    def save_form(self, request, form, change):
        pass
