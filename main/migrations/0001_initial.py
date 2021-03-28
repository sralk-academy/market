# Generated by Django 3.1.7 on 2021-03-25 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='male_clothes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(max_length=500, verbose_name='Описание')),
                ('make', models.CharField(max_length=50, verbose_name='Изготовитель')),
                ('priсe', models.CharField(max_length=50, verbose_name='Цена')),
                ('composition', models.CharField(max_length=50, verbose_name='Состав')),
                ('size', models.CharField(max_length=50, verbose_name='Размеры')),
                ('color', models.CharField(max_length=50, verbose_name='Цвет')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Мужская одежда',
                'verbose_name_plural': 'Мужская одежда',
            },
        ),
    ]
