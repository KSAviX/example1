# Generated by Django 2.2.4 on 2019-08-15 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('occupation', '0003_auto_20190815_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occupation',
            name='fireDate',
            field=models.DateField(blank=True, null=True, verbose_name='Дата увольнения'),
        ),
    ]
