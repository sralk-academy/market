# Generated by Django 3.1.7 on 2021-03-31 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210331_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessories_clothes',
            name='availability',
            field=models.CharField(default='', max_length=50, verbose_name='Наличие'),
        ),
        migrations.AddField(
            model_name='children_clothes',
            name='availability',
            field=models.CharField(default='', max_length=50, verbose_name='Наличие'),
        ),
        migrations.AddField(
            model_name='female_clothes',
            name='availability',
            field=models.CharField(default='', max_length=50, verbose_name='Наличие'),
        ),
        migrations.AddField(
            model_name='male_clothes',
            name='availability',
            field=models.CharField(default='', max_length=50, verbose_name='Наличие'),
        ),
    ]
