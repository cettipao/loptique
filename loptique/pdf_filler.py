from django.shortcuts import redirect

from config.settings import BASE_DIR
from loptique.models import *
from loptique.pdfFiller import ProcessPdf


def start_gen(obj):
    receta = obj
    pdf = ProcessPdf(BASE_DIR + "/loptique/static/Receta", "final_pdf.pdf")
    #Esteticas
    minutos = str(receta.fecha_entrega.minute)
    if len(minutos) == 1:
        minutos = "0" + str(receta.fecha_entrega.minute)
    hora = str(receta.fecha_entrega.hour)
    if len(hora) == 1:
        hora = "0" + str(receta.fecha_entrega.hour)

    armazon = "-"
    lejos_armazon = "-"
    lejos_armazon_precio = "-"
    lejos_color = "-"
    lejos_tipo = "-"
    lejos_tipo_precio = "-"
    lejos_tratamientos = "-"
    lejos_tratamientos_precio = "-"
    cerca_armazon = "-"
    cerca_armazon_precio = "-"
    cerca_color = "-"
    cerca_tipo = "-"
    cerca_tipo_precio = "-"
    cerca_tratamientos = "-"
    cerca_tratamientos_precio = "-"


    lejos_od_esfera = "-"
    lejos_od_cilindro = "-"
    lejos_od_eje = "-"
    lejos_oi_esfera = "-"
    lejos_oi_cilindro = "-"
    lejos_oi_eje = "-"
    lejos_distancia_interpupilar = "-"

    cerca_od_esfera = "-"
    cerca_od_cilindro = "-"
    cerca_od_eje = "-"
    cerca_oi_esfera = "-"
    cerca_oi_cilindro = "-"
    cerca_oi_eje = "-"
    cerca_distancia_interpupilar = "-"

    multifocal = "-"
    m_DI_Lejos = "-"
    m_DI_Cerca = "-"
    multifocal_Altura = "-"
    multifocal_Precio = "-"


    lejos = AnteojoLejos.objects.get(receta=obj)
    cerca = AnteojoCerca.objects.get(receta=obj)
    multifocal_obj = Multifocal.objects.get(receta=obj)
    if AnteojoLejos.objects.filter(receta=receta):
        lejos_armazon = lejos.armazon.descripcion
        lejos_armazon_precio = lejos.armazon.precio_venta_con_iva
        lejos_color = lejos.color
        lejos_tipo = lejos.tipo_lente.nombre
        lejos_tipo_precio = lejos.tipo_lente.precio_venta_con_iva
        lejos_tratamientos = ""
        lejos_tratamientos_precio = 0
        for t in lejos.tratamientos.all():
            lejos_tratamientos += (t.descripcion + ", ")
            lejos_tratamientos_precio += t.precio_venta_con_iva
        lejos_od_esfera = lejos.od_esfera
        lejos_od_cilindro = lejos.od_cilindro
        lejos_od_eje = lejos.od_eje
        lejos_oi_esfera = lejos.oi_esfera
        lejos_oi_cilindro = lejos.oi_cilindro
        lejos_oi_eje = lejos.oi_eje
        lejos_distancia_interpupilar = lejos.distancia_interpupilar

    if AnteojoCerca.objects.filter(receta=receta):
        cerca_armazon = cerca.armazon.descripcion
        cerca_armazon_precio = cerca.armazon.precio_venta_con_iva
        cerca_color = cerca.color
        cerca_tipo = cerca.tipo_lente.nombre
        cerca_tipo_precio = cerca.tipo_lente.precio_venta_con_iva
        cerca_tratamientos = ""
        cerca_tratamientos_precio = 0
        for t in cerca.tratamientos.all():
            cerca_tratamientos += (t.descripcion + ", ")
            cerca_tratamientos_precio += t.precio_venta_con_iva
        cerca_od_esfera = cerca.od_esfera
        cerca_od_cilindro = cerca.od_cilindro
        cerca_od_eje = cerca.od_eje
        cerca_oi_esfera = cerca.oi_esfera
        cerca_oi_cilindro = cerca.oi_cilindro
        cerca_oi_eje = cerca.oi_eje
        cerca_distancia_interpupilar = cerca.distancia_interpupilar

    if Multifocal.objects.filter(receta=receta):
        multifocal = multifocal_obj.tipo_multifocal
        m_DI_Lejos = multifocal_obj.di_lejos
        m_DI_Cerca = multifocal_obj.di_cerca
        multifocal_Altura = multifocal_obj.altura
        multifocal_Precio = ""

    armazon = lejos_armazon + " / " + cerca_armazon
    tipo = lejos_tipo + " / " + lejos_tipo
    obra_social = ""
    if receta.paciente.obra_social:
        obra_social= receta.paciente.obra_social.nombre

    telefono = ""
    if receta.paciente.telefono:
        telefono = receta.paciente.telefono

    pdf.add_data_to_pdf(BASE_DIR + "/loptique/static/Plantilla3.1Lite.pdf", {"Precio_1": "$",
                                                                            "Fecha 1": "{}/{}/{}".format(str(receta.fecha_inicio.day), str(receta.fecha_inicio.month), str(receta.fecha_inicio.year)),
                                                                            "Fecha y Hora de Entrega 1": "{}/{}/{} {}:{} aprox.".format(str(receta.fecha_entrega.day), str(receta.fecha_entrega.month), str(receta.fecha_entrega.year),  hora,  minutos),
                                                                            "Neto 1": "$",
                                                                            "Apellido y Nombre 1": str(receta.paciente.nombre),
                                                                            "Entrega 1": "$" + str(receta.seña),
                                                                            "Armazon 1": armazon,
                                                                            "Modelo 1": "",
                                                                            "Saldo1": "$",
                                                                            "Tipo de Cristal": tipo,
                                                                            "Forma de Pago 1": str(receta.forma_de_pago),
                                                                            "Observaciones 1": str(receta.observaciones),
                                                                            "Orden de Trabajo 2": str(receta.id),
                                                                            "DR": str(receta.doctor.nombre),
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
                                                                            "Lente_Precio_Lejos": "$",
                                                                            "DI_Lejos": lejos_distancia_interpupilar,
                                                                            "DI_Cerca": cerca_distancia_interpupilar,
                                                                            "Armazon_Precio_Lejos":"$" + str(lejos_armazon_precio),
                                                                            "Armazon_Lejos": lejos_armazon,
                                                                            "Tratamientos_Lejos": lejos_tratamientos,
                                                                            "Tratamientos_Precio_Lejos":"$" + str(lejos_tratamientos_precio),
                                                                            "Lente_Precio_Cerca": "$",
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
                                                                            "Precio 2": "$",
                                                                            "Armazon 2": armazon,
                                                                            "Neto 2": "$",
                                                                            "Laboratorio": str(receta.laboratorio),
                                                                            "Entrega 2":"$" + str(receta.seña),
                                                                            "Observaciones 2": str(receta.observaciones),
                                                                            "Saldo 2": "$",
                                                                            "Obra Social": obra_social,
                                                                            "Forma de Pago 2": str(receta.forma_de_pago),
                                                                            "Dia": "",
                                                                            "Mes": "",
                                                                            "Year": "",
                                                                            "Orden de Trabajo 1": str(receta.id),
                                                                            })

    file_path = BASE_DIR + '/loptique/static/' + 'Receta.pdf'
    response = redirect('/static/Receta.pdf')
    return response