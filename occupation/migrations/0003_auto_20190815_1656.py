# Generated by Django 2.2.4 on 2019-08-15 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('occupation', '0002_auto_20190815_1613'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='occupation',
            options={'ordering': ['-name'], 'verbose_name': 'Работник', 'verbose_name_plural': 'Работники'},
        ),
    ]
