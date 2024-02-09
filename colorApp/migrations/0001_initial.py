# Generated by Django 4.2.1 on 2024-02-09 05:37

import colorfield.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ColorCompany',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('template', models.CharField(max_length=50, verbose_name='Template')),
                ('description', models.CharField(max_length=100, verbose_name='Descripción')),
                ('bg_main', colorfield.fields.ColorField(blank=True, default='#fffffe', image_field=None, max_length=25, null=True, samples=None, verbose_name='Fondo')),
                ('text_main', colorfield.fields.ColorField(blank=True, default='#2b2c34', image_field=None, max_length=25, null=True, samples=None, verbose_name='Texto Principal')),
                ('text_secondary', colorfield.fields.ColorField(blank=True, default='#fffffe', image_field=None, max_length=25, null=True, samples=None, verbose_name='Texto Secundario')),
                ('company_main', colorfield.fields.ColorField(blank=True, default='#6246ea', image_field=None, max_length=25, null=True, samples=None, verbose_name='Empresa')),
                ('company_secondary', colorfield.fields.ColorField(blank=True, default='#d1d1e9', image_field=None, max_length=25, null=True, samples=None, verbose_name='Empresa Secundario')),
                ('company_icon', colorfield.fields.ColorField(blank=True, default='#fffffe', image_field=None, max_length=25, null=True, samples=None, verbose_name='Icono Empresa')),
                ('icono_main', colorfield.fields.ColorField(blank=True, default='#2B2C34', image_field=None, max_length=25, null=True, samples=None, verbose_name='Icono Principal')),
                ('icono_secondary', colorfield.fields.ColorField(blank=True, default='#6246ea', image_field=None, max_length=25, null=True, samples=None, verbose_name='Icono Secundario')),
                ('icono_services', colorfield.fields.ColorField(blank=True, default='#6246ea', image_field=None, max_length=25, null=True, samples=None, verbose_name='Icono Servicios')),
                ('icono_utilities', colorfield.fields.ColorField(blank=True, default='#fffffe', image_field=None, max_length=25, null=True, samples=None, verbose_name='Icono Utilerias')),
            ],
            options={
                'verbose_name': 'Tema de Empresa',
                'verbose_name_plural': 'Temas de Empresa',
            },
        ),
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('icon', models.CharField(max_length=50, verbose_name='Icono')),
            ],
            options={
                'verbose_name': 'Icono',
                'verbose_name_plural': 'Iconos',
            },
        ),
    ]
