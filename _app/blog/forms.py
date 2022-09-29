from django import forms
from blog.models import Blog


class CustomBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
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

