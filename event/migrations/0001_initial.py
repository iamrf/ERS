# Generated by Django 2.2.1 on 2019-06-09 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام رویداد')),
                ('date', models.DateTimeField(verbose_name='زمان')),
                ('duration', models.IntegerField(default=1, verbose_name='مدت')),
                ('desc', models.TextField(blank=True, verbose_name='توضیحات بیشتر')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
