######
#Ejercicios de Coecciones con las diferentes estructura de control
#############
# lista = list()
# tupla = (1,2,)
# conjuto = {}
# diccionario = {'key1':'Valor1', 'llave2':'valor2'}

# if True:
#     pass
# else:
#     pass
#
# # while True:
# #     pass
#
# for item in lista:
#     pass

# lista.append('item1')
# lista.append('item2')
# lista.append('item3')
# lista.append('item4')
# lista.append('item5')
# lista.append('item6')
# lista.append('item7')

# for item in lista:
#     print(item)
#
# i = 0
# while i < len(lista):
#     print(lista[i])
#     i += 1

from datos import empleados, cantidad_de_elementos

sample_employee = {
    "id": 1001,
    "imageUrl": "https://hub.dummyapis.com/Image?text=LY&height=120&width=120",
    "firstName": "Lawrence",
    "lastName": "Yundt",
    "email": "Lawrence.Yundt@dummyapis.com",
    "contactNumber": "4331598199",
    "age": 78,
    "dob": "16/05/1946",
    "salary": 1.0,
    "address": "Address1"
  }
# print(sample_employee["firstName"])

# cantidad_empleados = len(empleados)
# print(f'Cantidad de emmpleados: {cantidad_empleados}')
#
# for empleado in empleados:
#     # print(empleado)
#     if empleado["age"] > 70:
#         # print(empleado["firstName"].upper()+' '+empleado["lastName"].lower())
#         print(f'{empleado["firstName"].upper()} {empleado["lastName"].lower()}')

# cantidad_empleados = len(empleados)
cantidad_empleados = cantidad_de_elementos(empleados)
suma_edades = 0
for empleado in empleados:
    suma_edades += empleado['age']

promedio = suma_edades / cantidad_empleados
print(f'El promedio de edades es: {promedio}')





