# Generated by Django 4.1.7 on 2024-01-20 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_urlmodel_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='level',
            field=models.CharField(choices=[('A', 'Для любого пользователя'), ('B', 'Для зарегестрированного'), ('C', 'Для админа')], default='A', max_length=1),
        ),
        migrations.AlterField(
            model_name='instructionmodel',
            name='site',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Сайт'),
        ),
    ]
