from decimal import Decimal
from django.core.validators import RegexValidator
my_validator = RegexValidator("^[^$)]+$", "No puede contener '$' ni ')'.")

from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
from django.utils import timezone
from phone_field import PhoneField


class Localidad(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Localidades"

class Persona(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    domicilio = models.CharField(max_length=50, blank=True)
    localidad = models.ForeignKey(
        'Localidad',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    edad = models.SmallIntegerField(null=True,blank=True)
    telefono = PhoneField(blank=True, help_text='Contact phone number')
    email = models.EmailField(max_length=254, blank=True)
    cuit = models.CharField(max_length=20, blank=True)
    ivas = [
        ("RI", 'Responsable Inscripto'),
    ]
    iva = models.CharField(
        max_length=2,
        choices=ivas,
        blank=True,
    )
    sexos = [
        ("H", 'Hombre'),
        ("M", 'Mujer'),
    ]
    sexo = models.CharField(
        max_length=2,
        choices=sexos,
        blank=True,
    )

    def __str__(self):
        return self.nombre

    @staticmethod
    def autocomplete_search_fields():
        return 'nombre',


class Rubro(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    rubro = models.ForeignKey(
        'Rubro',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    proveedor = models.ForeignKey(
        'Proveedor',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    marca = models.ForeignKey(
        'Marca',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    codigo_patilla = models.CharField(max_length=50, null=True, blank=True)
    descripcion = models.CharField(max_length=50, null=False, validators=[my_validator])
    codigo_secundario = models.CharField(max_length=50, null=True, blank=True)
    grupo = models.ForeignKey(
        'GrupoProducto',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    stock_actual = models.SmallIntegerField(default=0, blank=True)
    comprometido = models.SmallIntegerField(default=0, blank=True)
    precio_costo_sin_iva = models.SmallIntegerField(blank=True, default=0, validators=[MinValueValidator(Decimal('0'))])
    precio_venta_con_iva = models.SmallIntegerField(blank=True, default=0, validators=[MinValueValidator(Decimal('0'))])

    def __str__(self):
        return "{} (${})".format(self.descripcion, self.precio_venta_con_iva)


class Cristal(models.Model):
    nombre = models.CharField(max_length=50)

    precio_costo_sin_iva = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0, validators=[MinValueValidator(Decimal('0'))])
    precio_venta_con_iva = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(Decimal('0'))])

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "cristales"

class Material(models.Model):
    descripcion = models.CharField(max_length=50)
    proveedor = models.ForeignKey(
        'Proveedor',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    precio_costo_sin_iva = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0, validators=[MinValueValidator(Decimal('0'))])
    precio_venta_con_iva = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(Decimal('0'))])

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "materiales"

class Armazon(models.Model):
    descripcion = models.CharField(max_length=50, validators=[my_validator])
    proveedor = models.ForeignKey(
        'Proveedor',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    precio_costo_sin_iva = models.SmallIntegerField(null=True, blank=True, validators=[MinValueValidator(Decimal('0'))])
    precio_venta_con_iva = models.SmallIntegerField(validators=[MinValueValidator(Decimal('0'))])

    def __str__(self):
        return "{} (${})".format(self.descripcion, self.precio_venta_con_iva)

    class Meta:
        verbose_name_plural = "armazones"

class Tratamiento(models.Model):
    descripcion = models.CharField(max_length=50, validators=[my_validator])

    precio_costo_sin_iva = models.SmallIntegerField(null=True, blank=True, validators=[MinValueValidator(Decimal('0'))])
    precio_venta_con_iva = models.SmallIntegerField(validators=[MinValueValidator(Decimal('0'))])

    def __str__(self):
        return "{} (${})".format(self.descripcion,self.precio_venta_con_iva)


class Color(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "colores"

class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    proovedor = models.ForeignKey(
        'Proveedor',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.nombre


class GrupoProducto(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class GrupoPaciente(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Banco(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Proveedor(Persona):
    banco = models.ForeignKey(
        'Banco',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    cbu = models.CharField(max_length=50, default="", blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "proveedores"

class Cuota(models.Model):
    forma_de_pago = models.ForeignKey(
        'FormaDePago',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    descripcion = models.CharField(max_length=50)
    cuotas = models.SmallIntegerField()
    recargo = models.SmallIntegerField()
    retencion = models.SmallIntegerField()

    def __str__(self):
        return self.descripcion


class FormaDePago(models.Model):
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = "Formas De Pago"

class Doctor(Persona):
    pass

    class Meta:
        verbose_name_plural = "Doctores"

class Obra_Social(models.Model):
    nombre = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Obras Sociales"

class Paciente(Persona):
    obra_social = models.ForeignKey(
        'Obra_Social',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.nombre


class Anteojo(models.Model):
    od_esfera = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0)
    od_cilindro = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0)
    od_eje = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0)
    oi_esfera = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0)
    oi_cilindro = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0)
    oi_eje = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0)
    distancia_interpupilar = models.CharField(max_length=10, blank=True, default=0)

    tipo_lente = models.ForeignKey(
        'Cristal',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    color = models.ForeignKey(
        'Color',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    precio_lente = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, validators=[MinValueValidator(Decimal('0'))])
    descuento_lente = models.CharField(max_length=10, default="0", blank=True)
    precio_final_lente = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, validators=[MinValueValidator(Decimal('0'))])

    armazon = models.ForeignKey(
        'Armazon',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    precio_armazon = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, validators=[MinValueValidator(Decimal('0'))])
    descuento_armazon = models.CharField(max_length=10, default="0", blank=True)
    precio_final_armazon = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, validators=[MinValueValidator(Decimal('0'))])

    precio_tratamientos = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, validators=[MinValueValidator(Decimal('0'))])
    descuento_tratamientos = models.CharField(max_length=10, default="0", blank=True)
    precio_final_tratamientos = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, validators=[MinValueValidator(Decimal('0'))])

    tratamientos = models.ManyToManyField(Tratamiento, blank=True)

"""
    @property
    def precio_final_armazon(self):
        return self.precio_armazon - self.descuento_armazon

    @property
    def precio_final_tratamientos(self):
        return self.precio_tratamientos - self.descuento_tratamientos

    @property
    def precio_armazon(self):
        if self.armazon:
            return (self.armazon.precio_venta_con_iva)
        return 0

    @property
    def precio_tratamientos(self):
        precio = 0
        if self.tratamientos:
            for t in self.tratamientos.all():
                precio += t.precio_venta_con_iva
        return precio
"""

class AnteojoLejos(Anteojo):
    receta = models.OneToOneField(
        'Receta',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "Lejos de {}".format(self.receta)

    class Meta:
        verbose_name_plural = "Anteojos Lejos"

class AnteojoCerca(Anteojo):
    receta = models.OneToOneField(
        'Receta',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "Cerca de {}".format(self.receta)

    class Meta:
        verbose_name_plural = "Anteojos Cerca"

class Tipo_Multifocal(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tipos Multifocal"

class Multifocal(models.Model):
    receta = models.OneToOneField(
        'Receta',
        on_delete=models.CASCADE,
    )

    tipo_multifocal = models.ForeignKey(
        'Tipo_Multifocal',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    di_lejos = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=False, default=0)
    di_cerca = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=False, default=0)
    altura = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=False, default=0)

    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True,
                                         validators=[MinValueValidator(Decimal('0'))])
    descuento = models.CharField(max_length=10, default="0", blank=True)

    precio_final = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True,
                                               validators=[MinValueValidator(Decimal('0'))])


    def __str__(self):
        return "Multifocal de {}".format(self.receta)

    class Meta:
        verbose_name_plural = "multifocales"

class Venta(models.Model):
    paciente = models.ForeignKey(
        'Paciente',
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
    )
    forma_de_pago = models.ForeignKey(
        'FormaDePago',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    observaciones = models.CharField(max_length=254, null=False, default="", blank=True)

    fecha_inicio = models.DateField(null=True, auto_now_add=True)
    fecha_entrega = models.DateTimeField(null=False, )

    sub_total = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=False)
    seña = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=False, blank=True)
    descuento = models.CharField(max_length=10, default="0", blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=False, blank=True)

    @property
    def saldo(self):
        return self.sub_total - self.seña

    estados = [
        ("Seña", 'Parcialmente Pagado'),
        ("Total", 'Completamente Pagado'),
    ]
    estado_de_pago = models.CharField(
        max_length=5,
        choices=estados,
        blank=True,
        default="Seña"
    )

    def fecha_entrega_(self):
        return "{}/{}/{}".format(str(self.fecha_entrega.day), str(self.fecha_entrega.month),
                                 str(self.fecha_entrega.year), )

    def save(self, *args, **kwargs):
        super(Venta, self).save(*args, **kwargs)
        if len(Transaccion.objects.filter(venta=self)) == 0:
            if self.seña > 0:
                Transaccion.objects.create(venta=self, monto=self.seña, seña=True,
                                           descripcion="Seña de {}".format(self.__str__()))
        sumaDePagos = 0
        for pago in Transaccion.objects.filter(venta=self):
            sumaDePagos += pago.monto
        if sumaDePagos >= self.sub_total:
            self.estado_de_pago = "Total"
        else:
            self.estado_de_pago = "Seña"
        super(Venta, self).save(*args, **kwargs)


class Receta(Venta):
    doctor = models.ForeignKey(
        'Doctor',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    laboratorio = models.CharField(max_length=50, null=False, default="", blank=True)


    def save(self, *args, **kwargs):
        super(Receta, self).save(*args, **kwargs)
        """
        anteojolejos = 0
        antejoCerca = 0
        multifocal = 0
        if len(AnteojoLejos.objects.filter(receta=self)) > 0:
            obj = AnteojoLejos.objects.filter(receta=self).first()
            anteojolejos = obj.precio_lente + obj.precio_armazon + obj.precio_tratamientos
        if len(AnteojoCerca.objects.filter(receta=self)) > 0:
            obj = AnteojoCerca.objects.filter(receta=self).first()
            antejoCerca = obj.precio_lente + obj.precio_armazon + obj.precio_tratamientos
        if len(Multifocal.objects.filter(receta=self)) > 0:
            obj = Multifocal.objects.filter(receta=self).first()
            multifocal = obj.precio_multifocal

        self.sub_total = anteojolejos + antejoCerca + multifocal
        super(Receta, self).save(*args, **kwargs)"""

    def __str__(self):
        return "Receta de {} ({}/{}/{})".format(self.paciente, str(self.fecha_entrega.day),
                                                str(self.fecha_entrega.month), str(self.fecha_entrega.year), )


class Venta_varios(Venta):
    productos = models.ManyToManyField(Producto)

    def __str__(self):
        return "Compra de {} ({}/{}/{})".format(self.paciente, str(self.fecha_entrega.day),
                                                str(self.fecha_entrega.month), str(self.fecha_entrega.year), )

    class Meta:
        verbose_name_plural = "Ventas Varios"

class Caja(models.Model):
    total = models.SmallIntegerField(default=0)


class Transaccion(models.Model):
    descripcion = models.CharField(max_length=254)
    venta = models.ForeignKey(
        'Venta',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    monto = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=False, validators=[MinValueValidator(Decimal('0'))])
    fecha = models.DateTimeField(null=False, auto_now_add=True)
    seña = models.BooleanField(default=False)
    egreso = models.BooleanField(default=False)

    def isSeña(self):
        return self.seña

    isSeña.boolean = seña
    isSeña.short_description = 'Es Seña'


    def save(self, *args, **kwargs):
        if self.seña:
            if self.monto != self.venta.seña:
                self.monto = self.venta.seña

        super(Transaccion, self).save(*args, **kwargs)

    def fecha_(self):
        return "{}/{}/{}".format(str(self.fecha.day), str(self.fecha.month),
                                 str(self.fecha.year), )

    def __str__(self):
        return "{} ({})".format(self.fecha, self.monto)



