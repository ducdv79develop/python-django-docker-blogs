from django import forms
from blog.models import Post

STATUS_CHOICES = (
    (0, 'status 1'),
    (1, 'status 2'),
    (2, 'status 3')
)


class CustomBlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'status',
            'public_flag',
        ]
        widgets = {
            'title': forms.TextInput(),
            'content': forms.Textarea(),
            'status': forms.Select(),
        }

