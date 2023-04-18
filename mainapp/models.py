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
