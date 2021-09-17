from django.db import models

# Create your models here.
list_documentos=['estado','clave_acceso','fecha','ambiente','razon_social','ruc','cliente','cedula_ruc','ruta']
class Documentos(models.Model):
    estado=models.CharField(max_length=100)
    numero=models.CharField(default="",max_length=100)
    clave_acceso=models.CharField(max_length=100)
    fecha=models.DateTimeField()
    ambiente=models.CharField(max_length=100)
    razon_social=models.CharField(max_length=100)
    ruc=models.CharField(max_length=13)
    cliente=models.CharField(max_length=100)
    cedula_ruc=models.CharField(max_length=13)
    total=models.CharField(default=0, max_length=20)
    ruta=models.URLField(max_length=300)
    ruta_xml=models.URLField(max_length=300)

