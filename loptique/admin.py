from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.utils.html import format_html

from .models import *
# Register your models here.
from .pdf_filler import start_gen

admin.site.site_header = 'Administración Loptique'
admin.site.site_title = "Loptique Administración"
admin.site.index_title = "Loptique"


class AnteojoLejosInLine(admin.StackedInline):  # Para ver los prestamos de la persona
    model = AnteojoLejos
    # readonly_fields = ('precio_final_lente', 'precio_final_armazon', 'precio_final_tratamientos')
    fieldsets = (
        ('Lente', {
            'fields': (
                'od_esfera', 'od_cilindro', 'od_eje', 'oi_esfera', 'oi_cilindro', 'oi_eje', 'distancia_interpupilar',
                'tipo_lente',
                'color', 'precio_lente', 'descuento_lente', 'precio_final_lente')
        }),
        ('Armazon', {
            'fields': (
                'armazon', 'precio_armazon', 'descuento_armazon', 'precio_final_armazon')
        }),
        ('Tratamientos', {
            'fields': (
                'tratamientos', 'precio_tratamientos', 'descuento_tratamientos', 'precio_final_tratamientos')
        }),
    )


class AnteojoCercaInLine(admin.StackedInline):  # Para ver los prestamos de la persona
    model = AnteojoCerca
    # readonly_fields = ('precio_final_lente', 'precio_final_armazon', 'precio_final_tratamientos')
    fieldsets = (
        ('Lente', {
            'fields': (
                'od_esfera', 'od_cilindro', 'od_eje', 'oi_esfera', 'oi_cilindro', 'oi_eje', 'distancia_interpupilar',
                'tipo_lente',
                'color', 'precio_lente', 'descuento_lente', 'precio_final_lente')
        }),
        ('Armazon', {
            'fields': (
                'armazon', 'precio_armazon', 'descuento_armazon', 'precio_final_armazon')
        }),
        ('Tratamientos', {
            'fields': (
                'tratamientos', 'precio_tratamientos', 'descuento_tratamientos', 'precio_final_tratamientos')
        }),
    )


class MultifocalInLine(admin.StackedInline):  # Para ver los prestamos de la persona
    model = Multifocal


class PagosInLine(admin.TabularInline):  # Para ver los prestamos de la persona
    model = Transaccion


class RecetaAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'fecha_entrega_', 'sub_total', 'estado_de_pago']
    list_display_links = ['paciente', 'fecha_entrega_', 'sub_total', 'estado_de_pago']
    search_fields = ['paciente__nombre', ]
    list_filter = ['fecha_inicio', 'doctor__nombre', 'forma_de_pago__descripcion', 'estado_de_pago']

    change_form_template = 'btn_imprimir.html'
    readonly_fields = ('saldo', 'estado_de_pago', )
    inlines = [AnteojoLejosInLine, AnteojoCercaInLine, MultifocalInLine, PagosInLine]
    fieldsets = (
        ('Principal', {
            'fields': (
                'paciente', 'fecha_entrega', 'doctor', 'laboratorio', 'observaciones', 'forma_de_pago', 'sub_total',
                'descuento', 'total', 'seña',
                'saldo', 'estado_de_pago')
        }),
    )

    """   fieldsets = (
        ('Principal', {
            'fields': (
                'paciente', 'fecha_entrega')
        }),
        ('Precio', {
            'fields': (
                'sub_total', 'descuento', 'seña', 'saldo', 'forma_de_pago', 'estado_de_pago')
        }),
        ('Otros', {
            'fields': (
                'doctor', 'laboratorio', 'observaciones',)
        }),
    )"""

    def response_change(self, request, obj):
        if "_imprimir" in request.POST:
            return redirect("http://{}/genpdf/{}".format(request.get_host(), obj.id))
        return super().response_change(request, obj)

    class Media:
        html = ('btn_imprimir.html')

        js = (
            'js/realtime.js',
        )


class AnteojoAdmin(admin.ModelAdmin):
    readonly_fields = ('precio_lente', 'precio_armazon', 'precio_tratamientos')
    fieldsets = (
        ('Lente', {
            'fields': (
                'od_esfera', 'od_cilindro', 'od_eje', 'oi_esfera', 'oi_cilindro', 'oi_eje', 'distancia_interpupilar',
                'tipo_lente',
                'color', 'precio_lente', 'descuento_lente', 'precio_final_lente')
        }),
        ('Armazon', {
            'fields': (
                'armazon', 'precio_armazon', 'descuento_armazon', 'precio_final_armazon')
        }),
        ('Tratamientos', {
            'fields': (
                'tratamientos', 'precio_tratamientos', 'descuento_tratamientos', 'precio_final_tratamientos')
        }),
    )


class AnteojoLejosAdmin(AnteojoAdmin):
    pass


class AnteojoCercaAdmin(AnteojoAdmin):
    pass


class VariosAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'fecha_entrega_', 'sub_total', 'estado_de_pago']
    list_display_links = ['paciente', 'fecha_entrega_', 'sub_total', 'estado_de_pago']
    search_fields = ['paciente__nombre', ]
    list_filter = ['fecha_inicio', 'forma_de_pago__descripcion', 'estado_de_pago']
    readonly_fields = ('saldo', 'estado_de_pago')
    fieldsets = (
        ('Principal', {
            'fields': (
                'paciente', 'productos', 'fecha_entrega')
        }),
        ('Precio', {
            'fields': (
                'sub_total', 'descuento', 'total','seña', 'saldo','estado_de_pago')
        }),
        ('Otros', {
            'fields': (
                'observaciones',)
        }),
    )
    class Media:

        js = (
            'js/realtime2.js',
        )


class TransaccionAdmin(admin.ModelAdmin):
    change_list_template = "btn_balance.html"
    list_display = ['descripcion', 'fecha_', 'monto']
    list_display_links = ['descripcion', 'fecha_', 'monto']
    search_fields = ['descripcion', ]
    list_filter = ['seña', 'fecha', 'egreso']


class PacienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'domicilio', 'edad', 'sexo']
    list_display_links = ['nombre', 'domicilio', 'edad', 'sexo']
    search_fields = ['nombre', 'cuit', 'email', 'telefono']
    list_filter = ['sexo', 'obra_social__nombre']


admin.site.register(Venta_varios, VariosAdmin)
admin.site.register(Armazon)
admin.site.register(Banco, )
admin.site.register(Color, )
admin.site.register(Cristal, )
admin.site.register(FormaDePago, )
admin.site.register(GrupoPaciente, )
admin.site.register(GrupoProducto, )
admin.site.register(Localidad, )
admin.site.register(Marca, )
admin.site.register(Obra_Social, )
# admin.site.register(Persona, )
admin.site.register(Rubro, )
admin.site.register(Tipo_Multifocal, )
admin.site.register(Tratamiento, )
admin.site.register(Doctor, )
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Receta, RecetaAdmin)
# admin.site.register(Multifocal, )
admin.site.register(Cuota, )
# admin.site.register(AnteojoLejos, AnteojoLejosAdmin)
# admin.site.register(AnteojoCerca, AnteojoCercaAdmin)
admin.site.register(Proveedor, )
admin.site.register(Producto, )
admin.site.register(Material, )
admin.site.register(Transaccion, TransaccionAdmin)
