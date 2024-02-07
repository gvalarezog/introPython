# colores = ('rojo', 'azul', 'amarillo', 'azul')
# print(colores)
# print(type(colores))
# print(len(colores))
#
# tupla1 = (1)
# print(type(tupla1))
# tupla2 = (1,)
# print(type(tupla2))
# print(colores[2])
#
# if "rojo " in colores:
#     print("Si está'el color rojo")
# else:
#     print("No esta el color rojo")
#
# # colores.insert(2,'negro')
# # colores[0] = 'negro'
# # print(colores)
#
# #se convierte la tupla a una lista
# lista = list(colores)
# print(type(lista))
# #cambiando el elemento del indice 1
# lista[1] = 'negro'
# #conveirto la lista en tupla
# colores = tuple(lista)
# print(colores)
# print(type(colores))

################################################
###Conjuntos - set
################################################
marcas = {'sony', 'prima', False, 'samsung', 0, 'prima', 'sony', True, 1}
print(marcas)
print(type(marcas))
print(len(marcas))
materias = set()
materias.add('LPP')
print(materias)

for item in marcas:
    print(item)


marcas.add('rca')
print(marcas)
print(len(marcas))
# print(marcas[0])

marcas2 = {'panasonic', 'tcl', 'sony'}
marcas.update(marcas2)
print(marcas)


marcas.discard("sony")
print(marcas)

marcas2.clear()
print(marcas2)
marcas.clear()
print(marcas)


#########
#Diccionarios - dict
#########
datos_personales = {'cedula': '0123456789', 'nombre': 'Luis', 'vip': True, 'cedula': '987654321'}
list_datos_personales = {'0123456789', 'Luis', True}

print(datos_personales)
print(len(datos_personales))
print(type(datos_personales))

datos_personales['nombre']='Jose'
print(datos_personales)
print(datos_personales['cedula'])
print(datos_personales.get('cedula'))

print(datos_personales['nombre'])
print(datos_personales['vip'])

datos_personales['cedula']='987654321'
print(datos_personales)

datos_personales['colores_fav']=['rojo', 'negro']
print(datos_personales)
datos_personales['telefonos']={'casa': '043698741', 'movil': '099663322'}
print(datos_personales)

print(datos_personales.keys())
print(datos_personales.values())
print(datos_personales.items())
datos_personales.pop('telefonos')
print(datos_personales)








