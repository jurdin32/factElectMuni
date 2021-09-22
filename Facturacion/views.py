import datetime

from django.http import HttpResponse
from django.shortcuts import render


import requests
import xmltodict

from Facturacion.models import Documentos

def index(request):
    documentos=None
    documento={}
    dic_xml={}
    pdf=""
    xml=""
    if request.GET.get('q'):
        archivo="FACTURA_%s"%request.GET.get('q')
        xml = 'http://siim.elguabo.gob.ec:8080/recursos_siim/FE/autorizados/%s.xml'%archivo
        myfile = requests.get(xml)
        dic_xml = xmltodict.parse(myfile.content)
        #print(dic_xml)
        documento=xmltodict.parse(dic_xml['autorizacion']['comprobante'])
        open('./static/'+archivo+'.xml', 'wb').write(myfile.content)
        pdf = 'http://siim.elguabo.gob.ec:8080/recursos_siim/FE/autorizados/%s.pdf' % archivo
        myfile = requests.get(pdf)
        open('./static/'+archivo+'.pdf', 'wb').write(myfile.content)
        try:
            Documentos.objects.get(clave_acceso=documento['factura']['infoTributaria']['claveAcceso'])
        except:
            try:
                fecc=(dic_xml['autorizacion']['fechaAutorizacion']).replace("T"," ").replace("-05:00","")
                Documentos.objects.create(
                estado = dic_xml['autorizacion']['estado'],
                clave_acceso = documento['factura']['infoTributaria']['claveAcceso'],
                numero=request.GET.get('q'),
                fecha = datetime.datetime.strptime(fecc,'%Y-%m-%d %H:%M:%S'),
                ambiente = dic_xml['autorizacion']['ambiente'],
                razon_social = documento['factura']['infoTributaria']['razonSocial'],
                ruc = documento['factura']['infoTributaria']['ruc'],
                cliente = documento['factura']['infoFactura']['razonSocialComprador'],
                cedula_ruc = documento['factura']['infoFactura']['identificacionComprador'],
                total=documento['factura']['infoFactura']['importeTotal'],
                ruta = pdf,
                ruta_xml=xml,
                ).save()
            except:
                pass
        try:
            documentos=Documentos.objects.filter(cedula_ruc=documento['factura']['infoFactura']['identificacionComprador']).order_by('-fecha')
        except:
            pass
    contexto={
        'documentos':documentos
    }
    return render(request,'index.html',contexto)

def fecha(request):
    fecha='2021-09-16T12:26:44-05:00'.replace("T"," ").replace("-05:00","")
    date=datetime.datetime.strptime(fecha,'%Y-%m-%d %H:%M:%S')
    print(date)
    return HttpResponse(date)