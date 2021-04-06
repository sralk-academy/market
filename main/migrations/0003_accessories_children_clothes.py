# Generated by Django 3.1.7 on 2021-03-31 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210328_2303'),
    ]

    operations = [
        migrations.CreateModel(
            name='accessories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(max_length=1000, verbose_name='Описание')),
                ('make', models.CharField(max_length=50, verbose_name='Изготовитель')),
                ('priсe', models.CharField(max_length=50, verbose_name='Цена')),
                ('composition', models.CharField(max_length=150, verbose_name='Состав')),
                ('size', models.CharField(max_length=50, verbose_name='Размеры')),
                ('color', models.CharField(max_length=50, verbose_name='Цвет')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Аксессуары',
                'verbose_name_plural': 'Аксессуары',
            },
        ),
        migrations.CreateModel(
            name='children_clothes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(max_length=1000, verbose_name='Описание')),
                ('make', models.CharField(max_length=50, verbose_name='Изготовитель')),
                ('priсe', models.CharField(max_length=50, verbose_name='Цена')),
                ('composition', models.CharField(max_length=150, verbose_name='Состав')),
                ('size', models.CharField(max_length=50, verbose_name='Размеры')),
                ('color', models.CharField(max_length=50, verbose_name='Цвет')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Детская одежда',
                'verbose_name_plural': 'Детская одежда',
            },
        ),
    ]