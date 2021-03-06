# Generated by Django 3.2.7 on 2021-09-17 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Facturacion', '0002_documentos_ruta_xml'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentos',
            name='total',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='documentos',
            name='fecha',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='documentos',
            name='ruta_xml',
            field=models.URLField(max_length=300),
        ),
    ]
