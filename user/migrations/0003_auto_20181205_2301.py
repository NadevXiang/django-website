# Generated by Django 2.1 on 2018-12-05 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20181010_0900'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': '用户资料', 'verbose_name_plural': '用户资料'},
        ),
    ]