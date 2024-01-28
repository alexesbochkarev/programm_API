from django.db import models


LEVEL_CHOICES = (
        ('A', 'Для любого пользователя'),
        ('B', 'Для зарегестрированного'),
        ('C', 'Для админа'),
    )

PRIORITY_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )


class Program(models.Model):
    name = models.CharField('Название', max_length=255)
    code = models.CharField('Код', max_length=255)
    type = models.CharField('Тип программы', max_length=255)
    level = models.CharField(max_length=1, choices=LEVEL_CHOICES, default="A")
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default="1")
    description = models.TextField('Описание', null=True, blank=True)
    visibility = models.BooleanField(default=False)
    created_date = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-priority', '-created_date',)


class NewsModel(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    description = models.TextField('Описание', null=True, blank=True)
    level = models.CharField(max_length=1, choices=LEVEL_CHOICES, default="A")
    text = models.TextField('Текст')
    image = models.ImageField('Картинка', upload_to='news/', blank=True)
    visibility = models.BooleanField(default=False)
    created_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ('-created_date',)


class InstructionModel(models.Model):
    title = models.CharField('Название', max_length=255)
    site = models.CharField('Сайт', max_length=500, null=True, blank=True)
    level = models.CharField(max_length=1, choices=LEVEL_CHOICES, default="A")
    visibility = models.BooleanField(default=False)
    upload = models.FileField(upload_to="uploads/", null=True, blank=True)
    created_date = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Инструкция'
        verbose_name_plural = 'Инструкции'
        ordering = ('-created_date',)


class UrlModel(models.Model):
    youtube = models.CharField('Youtube', max_length=500, null=True, blank=True)
    site = models.CharField('Сайт', max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = 'Ссылки'
        verbose_name_plural = 'Ссылки'

    def __str__(self):
        return f'{self.youtube} {self.site}'