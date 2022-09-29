from django.db import models
from django.utils import timezone


class SoftDeleteModel(models.Model):
    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

    def hard_delete(self):
        super(SoftDeleteModel, self).delete()

    class Meta:
        abstract = True

    deleted_at = models.DateTimeField(null=True)




