from django.db import models

class Occupation(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    companyName = models.CharField(max_length=100, verbose_name='Компания')
    positionName = models.CharField(max_length=100, verbose_name='Должность')
    hireDate = models.DateField(verbose_name='Дата приёма')
    fireDate = models.DateField(null=True,blank=True, verbose_name='Дата увольнения')
    salary = models.IntegerField(verbose_name='Ставка, руб.')
    fraction = models.IntegerField(verbose_name='Ставка, %')
    base = models.IntegerField(verbose_name='База, руб.')
    advance = models.IntegerField(verbose_name='Аванс, руб.')
    by_hours = models.BooleanField(verbose_name='Почасовая оплата')

    class Meta:
        verbose_name_plural = 'Работники'
        verbose_name = 'Работника'
        ordering = [ '-name' ] 


# class Occupation(models.Model):
#     name = models.CharField(max_length=200, verbose_name='Имя')
#     company_name = models.CharField(max_length=100, verbose_name='Компания')
#     position_name = models.CharField(max_length=100, verbose_name='Должность')
#     hireDate = models.DateField(verbose_name='Дата приёма')
#     fireDate = models.DateField(null=True, verbose_name='Дата увольнения')
#     salary = models.IntegerField(verbose_name='Ставка, руб.')
#     fraction = models.IntegerField(verbose_name='Ставка, %')
#     base = models.IntegerField(verbose_name='База, руб.')
#     advance = models.IntegerField(verbose_name='Аванс, руб.')
#     by_hours = models.BooleanField(verbose_name='Почасовая оплата')