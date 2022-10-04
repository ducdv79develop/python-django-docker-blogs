from django.contrib import admin
from django.utils import timezone
from blog import models, forms
from blog.services import admin_services


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


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'status', 'public_flag', 'deleted_at')
    list_filter = ('title', 'content', admin_services.PostStatusFilter)
    search_fields = ('title', 'content',)
    actions = (make_published, make_soft_delete)
    form = forms.CustomBlogForm
    fields = ('title', 'content', ('status', 'public_flag'))

    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': 'Danh sach Blog'}
        return super(PostAdmin, self).changelist_view(request, extra_context=extra_context)

    def save_form(self, request, form, change):
        pass

