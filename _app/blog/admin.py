from django.contrib import admin
from blog.models import Post
from blog.forms import CustomBlogForm
from django.utils import timezone
from django_summernote.admin import SummernoteModelAdmin

STATUS_CHOICES = (
    (0, 'status 1'),
    (1, 'status 2'),
    (2, 'status 3')
)


# Register your models here.
@admin.action(description='Mark selected stories as published')
def make_published(modelAdmin, request, queryset):
    queryset.update(public_flag=True)


@admin.action(description='Move to Trash')
def make_soft_delete(modelAdmin, request, queryset):
    queryset.update(deleted_at=timezone.now())


# @admin.register(Post)
# class BlogAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'content', 'status', 'public_flag', 'deleted_at']
#     list_filter = ['title', 'content', 'status', 'public_flag']
#     ordering = ['title']
#     actions = [make_published, make_soft_delete]
#     form = CustomBlogForm
#     fields = ['title', 'content', ('status', 'public_flag')]
#
#     def changelist_view(self, request, extra_context=None):
#         extra_context = {'title': 'Danh sach Blog'}
#         return super(BlogAdmin, self).changelist_view(request, extra_context=extra_context)
#
#     def save_form(self, request, form, change):
#         pass


# class BlogAdminArea(admin.AdminSite):
#     site_header = 'Blog Admin Area'
#     login_template = 'blog/admin/login.html'
#
#
# blog_site = BlogAdminArea(name='BlogAdmin')
#
#
@admin.register(Post)
class SummerAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
#
