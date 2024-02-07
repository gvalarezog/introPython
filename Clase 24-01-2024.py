# a = True
# print(a)
# print(type(a))
#
# bandera = False
#
# bandera = 3 < 4
# print(bandera)

# a = int(input('Ingrese el primer numero para la operación: '))
# # a = 5
# b = int(input('Ingrese el segundo numero para la operación: '))
# print(type(a))
# print(type(b))
# suma = a + b
# resta = a - b
# multiplicacion = a * b
# division = a / b
# residuo = a % b
# print(f'El resultado de la suma de {a} y {b} es: {suma}')
# print(f'El resultado de la resta de {a} y {b} es: {resta}')
# print(f'El resultado de la multiplicación de {a} y {b} es: {multiplicacion}')
# print(f'El resultado de la división de {a} y {b} es: {division} '
#       f'y el tipo de dato es {type(division)}')
# print(f'El resultado de la operación residuo de {a} y {b} es: {residuo} '
#       f'y el tipo de dato es {type(residuo)}')

# x = 0
# x = x + 1
# print(x)
# x+=1 # lo mismo x=x+1
# print(x)


#####################################
#listas
####################################
frutas = ['manzana', 'naranja', 'pera', 'naranja']
digitos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
direccion = ['Quito', 5, True, True]

print(len(frutas))
print(len(digitos))
print(len(direccion))

print(frutas[0])
print(frutas[2])
print(frutas[3])
print(frutas[-3])

frutas[1] = 'sandia'
print(frutas)


if 'uva' in frutas:
    print('Pera esta dentro de frutas')

frutas.append('uva')

if 'uva' in frutas:
    print('Uva esta dentro de frutas')
print(frutas)

frutas.insert(0,'piña')
print(frutas)

frutas.insert(3,'mandarina')
print(frutas)

frutas.remove('sandia')
print(frutas)

frutas.pop(5)
print(frutas)

persona = list()
cedula = input('Ingrese cedula: ')
persona.append(cedula)
# persona = ['0123456789', 'Luis', 'Perez', 'lperez@mail.com']
print(persona)