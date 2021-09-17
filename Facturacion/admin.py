from django.contrib import admin

# Register your models here.
from Facturacion.models import Documentos, list_documentos


@admin.register(Documentos)
class modelo(admin.ModelAdmin):
    list_display = list_documentos
    list_display_links = list_documentos