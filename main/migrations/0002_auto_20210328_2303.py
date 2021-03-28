# Generated by Django 3.1.7 on 2021-03-28 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='female_clothes',
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
                'verbose_name': 'Женская одежда',
                'verbose_name_plural': 'Женская одежда',
            },
        ),
        migrations.AlterField(
            model_name='male_clothes',
            name='composition',
            field=models.CharField(max_length=150, verbose_name='Состав'),
        ),
        migrations.AlterField(
            model_name='male_clothes',
            name='description',
            field=models.TextField(max_length=1000, verbose_name='Описание'),
        ),
    ]
