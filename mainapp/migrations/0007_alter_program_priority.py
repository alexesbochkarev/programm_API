# Generated by Django 4.1.7 on 2024-02-04 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_alter_program_options_instructionmodel_level_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='priority',
            field=models.IntegerField(verbose_name='Приоритет'),
        ),
    ]