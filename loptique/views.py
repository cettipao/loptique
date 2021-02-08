import os
import time

from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.utils.safestring import mark_safe

from .models import *
from .pdfFiller import ProcessPdf

# Create your views here.
from config.settings import BASE_DIR


def home_view(request):
    pacientes = {}
    for paciente in Paciente.objects.all():
        pacientes[paciente.nombre] = ""

    return render(request, "home.html", {"host": request.get_host(), "pacientes":pacientes})


def pdf_view(request,id):
    time.sleep(2)
    receta = Receta.objects.get(id=id)
    pdf = ProcessPdf(BASE_DIR + "/loptique/static/Receta", "final_pdf.pdf")
    #Esteticas
    minutos = str(receta.fecha_entrega.minute)
    if len(minutos) == 1:
        minutos = "0" + str(receta.fecha_entrega.minute)
    hora = str(receta.fecha_entrega.hour-3)
    if len(hora) == 1:
        hora = "0" + str(receta.fecha_entrega.hour)

    armazon = "-"
    lejos_armazon = "-"
    lejos_armazon_precio = 0
    lejos_color = "-"
    lejos_tipo = "-"
    lejos_tipo_precio = 0
    lejos_tratamientos = "-"
    lejos_tratamientos_precio = 0
    cerca_armazon = "-"
    cerca_armazon_precio = 0
    cerca_color = "-"
    cerca_tipo = "-"
    cerca_tipo_precio = 0
    cerca_tratamientos = "-"
    cerca_tratamientos_precio = 0


    lejos_od_esfera = "-"
    lejos_od_cilindro = "-"
    lejos_od_eje = "-"
    lejos_oi_esfera = "-"
    lejos_oi_cilindro = "-"
    lejos_oi_eje = "-"
    lejos_distancia_interpupilar = ""

    cerca_od_esfera = "-"
    cerca_od_cilindro = "-"
    cerca_od_eje = "-"
    cerca_oi_esfera = "-"
    cerca_oi_cilindro = "-"
    cerca_oi_eje = "-"
    cerca_distancia_interpupilar = ""

    multifocal = "-"
    m_DI_Lejos = "-"
    m_DI_Cerca = "-"
    multifocal_Altura = "-"
    multifocal_Precio = 0


    lejos = AnteojoLejos.objects.filter(receta=receta).first()
    cerca = AnteojoCerca.objects.filter(receta=receta).first()
    multifocal_obj = Multifocal.objects.filter(receta=receta).first()
    if lejos:
        if lejos.armazon:
            lejos_armazon = lejos.armazon.descripcion
        lejos_armazon_precio = lejos.precio_final_armazon
        if lejos.color:
            lejos_color = lejos.color
        if lejos.tipo_lente:
            lejos_tipo = lejos.tipo_lente.nombre
        lejos_tipo_precio = lejos.precio_final_lente
        lejos_tratamientos = ""
        lejos_tratamientos_precio = lejos.precio_final_tratamientos
        lejos_od_esfera = lejos.od_esfera
        lejos_od_cilindro = lejos.od_cilindro
        lejos_od_eje = lejos.od_eje
        lejos_oi_esfera = lejos.oi_esfera
        lejos_oi_cilindro = lejos.oi_cilindro
        lejos_oi_eje = lejos.oi_eje
        if lejos.distancia_interpupilar == 0:
            lejos_distancia_interpupilar = lejos.distancia_interpupilar
        
    if cerca:
        if cerca.armazon:
            cerca_armazon = cerca.armazon.descripcion
        cerca_armazon_precio = cerca.precio_final_armazon
        if cerca.color:
            cerca_color = cerca.color
        if cerca.tipo_lente:
            cerca_tipo = cerca.tipo_lente.nombre
        cerca_tipo_precio = cerca.precio_final_lente
        cerca_tratamientos = ""
        cerca_tratamientos_precio = cerca.precio_final_tratamientos
        cerca_od_esfera = cerca.od_esfera
        cerca_od_cilindro = cerca.od_cilindro
        cerca_od_eje = cerca.od_eje
        cerca_oi_esfera = cerca.oi_esfera
        cerca_oi_cilindro = cerca.oi_cilindro
        cerca_oi_eje = cerca.oi_eje
        if cerca.distancia_interpupilar == 0:
            cerca_distancia_interpupilar = cerca.distancia_interpupilar

    if Multifocal.objects.filter(receta=receta):
        multifocal = multifocal_obj.tipo_multifocal
        m_DI_Lejos = multifocal_obj.di_lejos
        m_DI_Cerca = multifocal_obj.di_cerca
        multifocal_Altura = multifocal_obj.altura
        multifocal_Precio = multifocal_obj.precio_final

    armazon = lejos_armazon + " / " + cerca_armazon
    tipo = lejos_tipo + " / " + lejos_tipo
    obra_social = ""
    if receta.paciente.obra_social:
        obra_social= receta.paciente.obra_social.nombre

    telefono = ""
    if receta.paciente.telefono:
        telefono = receta.paciente.telefono

    doctor = ""
    if receta.doctor:
        doctor = receta.doctor.nombre

    forma_pago = ""
    if receta.forma_de_pago:
        forma_pago = receta.forma_de_pago.descripcion
    pdf.add_data_to_pdf(BASE_DIR + "/loptique/static/Plantilla3.1Lite.pdf", {"Precio_1": "$" + str(receta.sub_total),
                                                                            "Fecha 1": "{}/{}/{}".format(str(receta.fecha_inicio.day), str(receta.fecha_inicio.month), str(receta.fecha_inicio.year)),
                                                                            "Fecha y Hora de Entrega 1": "{}/{}/{} {}:{} aprox.".format(str(receta.fecha_entrega.day), str(receta.fecha_entrega.month), str(receta.fecha_entrega.year),  hora,  minutos),
                                                                            "Neto 1": "$" + str(receta.sub_total - receta.descuento),
                                                                            "Apellido y Nombre 1": str(receta.paciente.nombre),
                                                                            "Entrega 1": "$" + str(receta.seña),
                                                                            "Armazon 1": armazon,
                                                                            "Modelo 1": "",
                                                                            "Saldo1": "$" + str(receta.saldo),
                                                                            "Tipo de Cristal": tipo,
                                                                            "Forma de Pago 1": forma_pago,
                                                                            "Observaciones 1": str(receta.observaciones),
                                                                            "Orden de Trabajo 2": str(receta.id),
                                                                            "DR": doctor,
                                                                            "Fecha 2": "{}/{}/{}".format(str(receta.fecha_inicio.day), str(receta.fecha_inicio.month), str(receta.fecha_inicio.year)),
                                                                            "Apellido y Nombre 2": str(receta.paciente.nombre),
                                                                            "Direccion": str(receta.paciente.domicilio),
                                                                            "Email": str(receta.paciente.email),
                                                                            "Telefono": telefono,
                                                                            "Fecha y Hora de Entrega 2": "{}/{}/{} {}:{} aprox.".format(str(receta.fecha_entrega.day), str(receta.fecha_entrega.month), str(receta.fecha_entrega.year),  hora,  minutos),
                                                                            "OD_ESF_Lejos": lejos_od_esfera,
                                                                            "OD_CIL_Lejos": lejos_od_cilindro,
                                                                            "OD_EJE_Lejos": lejos_od_eje,
                                                                            "OI_ESF_Lejos": lejos_oi_esfera,
                                                                            "OI_CIL_Lejos": lejos_oi_cilindro,
                                                                            "OI_EJE_Lejos": lejos_oi_eje,
                                                                            "OD_ESF_Cerca": cerca_od_esfera,
                                                                            "OD_CIL_Cerca": cerca_od_cilindro,
                                                                            "OD_EJE_Cerca": cerca_od_eje,
                                                                            "OI_ESF_Cerca": cerca_oi_esfera,
                                                                            "OI_CIL_Cerca": cerca_oi_cilindro,
                                                                            "OI_EJE_Cerca": cerca_oi_eje,
                                                                            "Tipo_Lejos": lejos_tipo,
                                                                            "Color_Lejos": lejos_color,
                                                                            "Lente_Precio_Lejos": "$" + str(lejos_tipo_precio),
                                                                            "DI_Lejos": lejos_distancia_interpupilar,
                                                                            "DI_Cerca": cerca_distancia_interpupilar,
                                                                            "Armazon_Precio_Lejos":"$" + str(lejos_armazon_precio),
                                                                            "Armazon_Lejos": lejos_armazon,
                                                                            "Tratamientos_Lejos": lejos_tratamientos,
                                                                            "Tratamientos_Precio_Lejos":"$" + str(lejos_tratamientos_precio),
                                                                            "Lente_Precio_Cerca": "$" + str(cerca_tipo_precio),
                                                                            "Tipo_Cerca": cerca_tipo,
                                                                            "Color_Cerca": cerca_color,
                                                                            "Armazon_Precio_Cerca":"$" + str(cerca_armazon_precio),
                                                                            "Armazon_Cerca": cerca_armazon,
                                                                            "Tratamientos_Precio_Cerca": "$" + str(cerca_tratamientos_precio),
                                                                            "Tratamientos_Cerca": cerca_tratamientos,
                                                                            "Multifocal": multifocal,
                                                                            "M_DI_Lejos": m_DI_Lejos,
                                                                            "M_DI_Cerca": m_DI_Cerca,
                                                                            "Multifocal_Altura": multifocal_Altura,
                                                                            "Multifocal_Precio": "$" + str(multifocal_Precio),
                                                                            "Di": "",
                                                                            "Precio 2": "$" + str(receta.sub_total),
                                                                            "Armazon 2": armazon,
                                                                            "Neto 2": "$" + str(receta.sub_total - receta.descuento),
                                                                            "Laboratorio": str(receta.laboratorio),
                                                                            "Entrega 2":"$" + str(receta.seña),
                                                                            "Observaciones 2": str(receta.observaciones),
                                                                            "Saldo 2": "$" + str(receta.saldo),
                                                                            "Obra Social": obra_social,
                                                                            "Forma de Pago 2": forma_pago,
                                                                            "Dia": "",
                                                                            "Mes": "",
                                                                            "Year": "",
                                                                            "Orden de Trabajo 1": str(receta.id),
                                                                            })

    file_path = BASE_DIR + '/loptique/static/' + 'Receta.pdf'
    response = redirect('/static/Receta.pdf')
    return response
