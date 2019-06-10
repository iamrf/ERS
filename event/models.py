from django.db import models
from django.utils import timezone

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=200, verbose_name='نام رویداد')
    location = models.CharField(max_length=200, verbose_name='مکان')
    date = models.DateTimeField(verbose_name='زمان')
    duration = models.IntegerField(verbose_name='مدت', default=1)
    price = models.CharField(max_length=100, default='رایگان', verbose_name='هزینه ثبت نام')
    desc = models.TextField(verbose_name='توضیحات بیشتر', blank=True)
    created = models.DateTimeField(auto_now_add=timezone.now, editable=False, verbose_name='زمان ثبت')
    last_modified = models.DateTimeField(auto_now=timezone.now, verbose_name='آخرین تغییر')

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return self.name


class User(models.Model):
    event = models.ManyToManyField(Event, verbose_name='رویداد مورد نظر')
    name = models.CharField(max_length=200, verbose_name='نام و نام خانوادگی')
    tell = models.CharField(max_length=13, verbose_name='شماره موبایل')
    address = models.CharField(max_length=300, blank=True, verbose_name='آدرس')
    created = models.DateTimeField(auto_now_add=timezone.now, editable=False, verbose_name='زمان ثبت')
    last_modified = models.DateTimeField(auto_now=timezone.now, verbose_name='آخرین تغییر')

    class Meta:
        ordering = ('last_modified',)

    def __str__(self):
        return self.name
