# def clase_ip(ip):
#     primera_octeto = int(ip.split('.')[0]) #192.168.0.1 -> 192
#     if primera_octeto <= 127 and primera_octeto >= 0:
#         return 'Clase A'
#     elif primera_octeto <= 191:
#         return 'Clase B'
#     elif primera_octeto <= 223:
#         return 'Clase C'
#     else:
#         return 'No es una dirección de clase A, B o C'
#
# ip = input("Ingresa la dirección IP: ")
# clase = clase_ip(ip)
# print("La dirección IP pertenece a la clase:", clase)


############
#While Loops -> Lazos condicionales
############
i = 0
# while i < 20:
#     i += 1
#     if i == 11:
#         # break
#         continue
#     print(i)
# else:
#     print(f'I es igual que 20')
#
# bandera_salida = True
# while bandera_salida:
#     print(f'Ingrese una opción es la letra del menú:')
#     print(f'Menu A')
#     print(f'Menu B')
#     print(f'Menu C')
#     print(f'Menu Z - Salida del menu')
#     opcion_escogida = input('Opcion: ')
#     # if opcion_escogida == 'Z' or opcion_escogida == 'z':
#     if opcion_escogida.lower() == 'z':
#         bandera_salida = False
#         # break
# else:
#     print('Adios')
# print('Salio del programa')


#####################
########## for -> lazo for no usa ninguna condicional
####################

# lista_colores = ['amarillo', 'azul', 'rojo','5','verde']
# for elemento_color in lista_colores:
#     if elemento_color.isdigit():
#         print('No es un color')
#     else:
#         print(elemento_color)
#
# print('x'.center(50,'x'))
#
# tupla_marcas = ('Audi', 'Ford', 'Chery')
# for marca in tupla_marcas:
# #     print(marca.lower())
#
# numeros = [1,2,3,4,5]
#
# resultado = 1
# nombre = input('Ingres nombre:')
# apellido = input('Ingres apellido:')
#
# def grabar_datos_en_archivo(nombre, archivo):
#     pass
#
# print(f'El nombre es {nombre}')
# grabar_datos_en_archivo(nombre, apellido)


for x in "kasjdfkljsaydkjfklsajdfklyyyyaksdjfkajsdkfjksaldjfyyyyylaskdflyyyy":
    if x == 'y':
        break
    print(x)






