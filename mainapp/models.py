from django.db import models


class Program(models.Model):
    name = models.CharField('Название', max_length=255)
    code = models.CharField('Код', max_length=255)
    description = models.TextField('Описание', null=True, blank=True)

    created_date = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_date',)


class NewsModel(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    text = models.TextField('Текст')
    image = models.ImageField('Картинка', upload_to='news/', blank=True)
    created_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ('-created_date',)


class InstructionModel(models.Model):
    title = models.CharField('Название', max_length=255)
    site = models.CharField('Сайт', max_length=500)
    file1 = models.CharField('Ссылка на файл №1', max_length=500, blank=True)
    file2 = models.CharField('Ссылка на файл №2', max_length=500, blank=True)
    file3 = models.CharField('Ссылка на файл №3', max_length=500, blank=True)
    file4 = models.CharField('Ссылка на файл №4', max_length=500, blank=True)
    file5 = models.CharField('Ссылка на файл №5', max_length=500, blank=True)
    youtube1 = models.CharField('Ссылка на Youtue №1', max_length=500, blank=True)
    youtube2 = models.CharField('Ссылка на Youtue №2', max_length=500, blank=True)
    youtube3 = models.CharField('Ссылка на Youtue №3', max_length=500, blank=True)
    youtube4 = models.CharField('Ссылка на Youtue №4', max_length=500, blank=True)
    youtube5 = models.CharField('Ссылка на Youtue №5', max_length=500, blank=True)
    created_date = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Инструкция'
        verbose_name_plural = 'Инструкции'
        ordering = ('-created_date',)