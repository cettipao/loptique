import openpyxl
from loptique.models import *

codigo_colores = []
colores = []
marcas = []
provedores = []

def populate():
    doc = openpyxl.load_workbook("ANTEOJOS STOCK 2021.xlsx")

    receta = Rubro.objects.get(nombre="Receta")
    sol = Rubro.objects.get(nombre="Sol")

    fila = 7
    while True:
        if doc["Hoja1"]["B" + str(fila)].value == "DONE":
            break
        if doc["Hoja1"]["B" + str(fila)].value != None:

            codigo = doc["Hoja1"]["B" + str(fila)].value
            rubro = doc["Hoja1"]["C" + str(fila)].value
            marca = doc["Hoja1"]["E" + str(fila)].value
            compra = doc["Hoja1"]["I" + str(fila)].value
            if compra == None:
                compra = 0
            ventas = doc["Hoja1"]["J" + str(fila)].value
            if ventas == None:
                ventas = 0
            codigo_color = str(doc["Hoja1"]["H" + str(fila)].value).upper()
            color = str(doc["Hoja1"]["G" + str(fila)].value).upper()

            if marca != None:
                if marca not in marcas:
                    marcas.append(marca)
                    marca = Marca.objects.create(nombre=marca)
                else:
                    marca = Marca.objects.get(nombre=marca)
                    marca = marca

            if str(rubro).lower() == "sol":
                rubro = sol
            elif str(rubro).lower() == "receta":
                rubro = receta

            codigo = str(codigo).split("/")

            if codigo[0] not in provedores:
                provedores.append(codigo[0])
                provedor = Proveedor.objects.create(codigo=codigo[0])
            else:
                provedor = Proveedor.objects.get(codigo=codigo[0])

            Producto.objects.create(proveedor=provedor, modelo=codigo[1], marca=marca,
                                    rubro=rubro, stock_actual=(int(compra)-int(ventas)))

            print("Proovedor: {}".format(codigo[0]))
            print("Modelo: {}".format(codigo[1]))
            print("Color: {}".format(color))
            print("Marca: {}".format(marca))
            print("Rubro: {}".format(rubro))
            print("Stock: {}".format(int(compra)-int(ventas)))
            print("-------------------------")
        fila += 1
    print(marcas)
    print(provedores)
