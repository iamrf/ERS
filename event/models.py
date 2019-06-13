from django.db import models
from django.forms import ModelForm
from django.utils import timezone
from . import script

# Create your models here.


class Event(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='نام رویداد',
    )

    location = models.CharField(
        max_length=200,
        verbose_name='مکان',
    )

    date = models.DateTimeField(
        verbose_name='زمان',
    )

    duration = models.IntegerField(
        verbose_name='مدت',
        default=1,
    )

    price = models.CharField(
        max_length=100,
        default='رایگان',
        verbose_name='هزینه ثبت نام',
    )

    desc = models.TextField(
        verbose_name='توضیحات بیشتر',
        blank=True,
    )

    lat = models.FloatField(
        blank=True,
        verbose_name='عرض جغرافیایی',
    )

    lng = models.FloatField(
        blank=True,
        verbose_name='طول جغرافیایی',
    )

    pic = models.ImageField(
        upload_to='event/',
        verbose_name='تصویر',
        max_length=500,
        )
    picv = models.ImageField(
        upload_to='event/',
        verbose_name='تصویر-عمودی',
        max_length=500,
        blank=True,
        null=True,
        )

    created = models.DateTimeField(
        auto_now_add=timezone.now,
        editable=False,
        verbose_name='زمان ثبت',
    )

    last_modified = models.DateTimeField(
        auto_now=timezone.now,
        verbose_name='آخرین تغییر',
    )

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return self.name


class User(models.Model):
    event = models.ManyToManyField(
        Event,
        verbose_name='رویداد ها',
    )

    name = models.CharField(
        max_length=200,
        verbose_name='نام و نام خانوادگی',
    )

    tell = models.CharField(
        max_length=13,
        verbose_name='شماره تلفن همراه',
    )

    email = models.EmailField(
        blank=True,
        verbose_name='پست الکترونیک',
    )

    age = models.IntegerField(
        verbose_name='سن',
        )

    address = models.CharField(
        max_length=300,
        blank=True,
        verbose_name='آدرس',
    )

    desc = models.TextField(
        verbose_name='توضیحات اضافه',
        blank=True,
    )

    created = models.DateTimeField(
        auto_now_add=timezone.now,
        editable=False,
        verbose_name='زمان ثبت',
    )

    last_modified = models.DateTimeField(
        auto_now=timezone.now,
        verbose_name='آخرین تغییر',
    )

    class Meta:
        ordering = ('-last_modified',)

    def __str__(self):
        return self.name
