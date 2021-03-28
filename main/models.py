from django.db import models

class male_clothes(models.Model):
    title = models.CharField('Название',max_length=50)
    description = models.TextField('Описание',max_length=1000)
    make = models.CharField('Изготовитель',max_length=50)
    priсe = models.CharField('Цена',max_length=50)
    composition = models.CharField('Состав',max_length=150)
    size = models.CharField('Размеры',max_length=50)
    color = models.CharField('Цвет',max_length=50)
    image = models.ImageField('Изображение')
    
    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Мужская одежда'
        verbose_name_plural = 'Мужская одежда'

class female_clothes(models.Model):
    title = models.CharField('Название',max_length=50)
    description = models.TextField('Описание',max_length=1000)
    make = models.CharField('Изготовитель',max_length=50)
    priсe = models.CharField('Цена',max_length=50)
    composition = models.CharField('Состав',max_length=150)
    size = models.CharField('Размеры',max_length=50)
    color = models.CharField('Цвет',max_length=50)
    image = models.ImageField('Изображение')
    
    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Женская одежда'
        verbose_name_plural = 'Женская одежда'