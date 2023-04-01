from uuid import uuid4

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _


class BaseQueryset(models.QuerySet):
    def delete(self):
        self.update(deleted=timezone.now())


class BaseManager(models.Manager):

    def get_queryset(self):
        return BaseQueryset(self.model, using=self._db).filter(deleted__isnull=True)


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = models.DateTimeField(verbose_name=_(u'created date'), auto_now_add=True)
    modified = models.DateTimeField(verbose_name=_(u'modified date'), auto_now=True)
    deleted = models.DateTimeField(verbose_name=_(u'deleted date'), null=True)

    objects = BaseManager()
    all_objects = models.Manager()

    def delete(self, *args, **kwargs):
        self.deleted = timezone.now()
        self.save()

    class Meta:
        abstract = True
