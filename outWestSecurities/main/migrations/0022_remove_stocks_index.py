# Generated by Django 3.1.7 on 2021-05-13 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20210513_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stocks',
            name='index',
        ),
    ]
