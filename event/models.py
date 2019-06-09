from django.db import models
from django.utils import timezone

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=200, verbose_name='نام رویداد')
    location = models.CharField(max_length=200, verbose_name='مکان')
    date = models.DateTimeField(verbose_name='زمان')
    duration = models.IntegerField(verbose_name='مدت', default=1)
    desc = models.TextField(verbose_name='توضیحات بیشتر', blank=True)
    created = models.DateTimeField(auto_now_add=timezone.now, editable=False, verbose_name='زمان ثبت')
    last_modified = models.DateTimeField(auto_now=timezone.now, verbose_name='آخرین تغییر')

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return self.name
