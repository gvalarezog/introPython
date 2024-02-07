#defincion de funciones
# se utiliza la sintaxis def nombre_funcion(parametros): identación del bloque de codigo
# def saludar():
#     print(f'Hola')
#
# saludar()
#
# def saludar_nombre(nombre, apellido):
#     print(f'Hola {nombre.capitalize()} {apellido.capitalize()}')
#
# saludar_nombre('cARLOS', 'pEREZ')
#
# def suma(sumando1, sumando2):
#     resultado = sumando1 + sumando2
#     return resultado
#
# r = suma(5, 10)
# print(r)
#
# def escoger_modulo(modulo):#Modulo pueder un numero 1 o modulo 2
#     if modulo == 1:
#         return f'Modulo Uno ({modulo})'
#     elif modulo==2:
#         return f'Modulo Dos'
#     else:
#         return f'Modulo equivocado'
#
# # print(escoger_modulo(3))
#
# modulo = int(input('Ingrese el modulo 1 o 2: '))
#
# print(escoger_modulo(modulo))

def registrar(nombre, apellido, cedula=None):
    if cedula:
        return f'{nombre.capitalize()} {apellido.capitalize()} - {cedula}'
    else:
        return f'{nombre.capitalize()} {apellido.capitalize()}'



# print(registrar(apellido='Perez', cedula='0123456789', nombre='carlos'))
# print(registrar('Perez', '0123456789', 'carlos'))
# x = input('Nombre(*): ')
# y = input('Apellido(*): ')
# z = input('Cedula: ')
# # print(registrar(nombre, apellido, cedula))
# print(registrar(nombre=x, cedula=z, apellido=y))
# # print(registrar(nombre=x, apellido=y))


def registrar2(*args):
    print(f'cantidad de argmentos: {len(args)}')
    for argumento in args:
        print(argumento)
    # return f'{nombre.capitalize()} {apellido.capitalize()}'


# x = input('Nombre(*): ')
# y = input('Apellido(*): ')

# print(registrar2('Luis', 'Perez', '0258','lperez@mail.com', ))
# print(registrar2('Maria', 'PAz', '3698521470','mpaz@mail.com', '7412589630'))


def registrar3(**kwargs):
    for item in kwargs.items():
        print(item)


print(registrar3(nombre='Luis', apellido='Perez', cedula='0258',email='lperez@mail.com'))
print(registrar3(nombre='Maria', apellido='PAz', cedula='3698521470'
                 ,email='mpaz@mail.com', telf_movil='7412589630'))


def registrar4(nombre, *args, **kwargs):
    print(nombre)

# print(registrar4(nombre='Luis', ('Perez',), email='lperz@mail.com'))