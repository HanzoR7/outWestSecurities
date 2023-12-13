# Generated by Django 3.1.7 on 2021-05-10 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_stocks_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_orders', models.IntegerField(default=0)),
                ('closed_orders', models.IntegerField(default=0)),
            ],
        ),
    ]