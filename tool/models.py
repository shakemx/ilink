from django.db import models

from base.models import BaseModel
from colorApp.models import Icon


class Utility(BaseModel):
    USER = 'USER'
    COMPANY = 'COMPANY'
    CHOICE_TYPE =[
        (USER, 'Usuario'),
        (COMPANY, 'Empresa'),
    ]
    name = models.CharField('Nombre', max_length=50, blank=False, null=False)
    decription = models.CharField('Descripción', max_length=100)
    logo = models.ImageField('Logo - Icon',blank=True, null=True)
    url = models.URLField('URL', blank=False, null=False)
    type = models.CharField('Tipo', max_length=10, choices=CHOICE_TYPE, default=USER, blank=False)
    icon = models.ForeignKey(Icon, on_delete=models.CASCADE, blank=False, null=True)
    class Meta:
        verbose_name = 'Utileria'
        verbose_name_plural = 'Utilerias'
    
    def __str__(self):
        return self.name
    

