from django.db import models

from base.models import BaseModel
from colorApp.models import Icon


class Service(BaseModel):
    name = models.CharField('Nombre', max_length=50, blank=False, null=False)
    title = models.CharField('Título', max_length=50, blank=False, null=False)
    decription = models.TextField('Descripción', blank=False, null=False, max_length=500)
    logo = models.ImageField('Logo - Servicio', blank=True)
    icon = models.ForeignKey(Icon, on_delete=models.CASCADE, blank=True, null=True) 


    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
    
    def __str__(self):
        return self.name

