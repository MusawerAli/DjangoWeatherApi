# Generated by Django 3.0.5 on 2020-05-03 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0003_auto_20200503_2318'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name_plural': 'cities'},
        ),
    ]