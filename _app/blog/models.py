from django.db import models
from src.core import abstract_models


# Create your models here.
class Blog(abstract_models.SoftDeleteModel):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=3000)
    status = models.SmallIntegerField(default=0)
    public_flag = models.BooleanField(default=False)
    created_by = models.IntegerField(null=True)
    updated_by = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(abstract_models.SoftDeleteModel):
    user_id = models.IntegerField()
    message = models.CharField(max_length=3000)
    status = models.BooleanField(default=True)
    public_flag = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
