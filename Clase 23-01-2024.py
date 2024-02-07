# #uso de "" o ''
# x = 'Carlos'
# print(x)
# x = "Carlos"
# print(x)
#
# query = "select * from personas where nombre = 'Carlos';"
# ruta = 'c:\\ruta"variaable"'
#
# a = 0
# A = 5
#
# print(a)
# print(A)
# x = 'Orange'
# y = "Banana"
# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)
#
# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)
#
# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)
#
# a = 5
# b = 2
# resultado = a * b
# print(resultado)

x = "Python"
y = "es"
z = "asombroso"
a = ' '
b = ' '
# print(x, y, z)
# print(x + a + y + b + z) # Python es asombroso
print(x + ' ' + y + ' ' + z)  # Python es asombroso

# x = 5
# y = 'Juan'
# print(x + y)


x: int = 'Diez'
print(x)

# import sys
# integer = '10000'
# print("The size of the integer variable is:",sys.getsizeof(integer), "bytes.")

# x = 10
# y = 10.5
# z = '10'
# print(type(x))
# print(type(y))
# print(type(z))
# print(type(10))
#
# r = -87.7e100
# print(r)
# print(type(r))


# x = 1    # int
# y = 2.8  # float
#
# #convert from int to float:
# a = float(x)
#
# #convert from float to int:
# b = int(y)
#
# print(a)
# print(b)
#
# t = '1'
# s = int(t)
# print(s)
#
# q='''
# hola de muchas
# lineas de
# texto
# '''
#
# p="""
# hola de muchas
# lineas de
# texto"""
# print(p)


a = "Hello, World!"
print(a[1])
print(a[0])
print(a[10])
print(a[12])
# print(a[13])

cadena = 'casa'
print(len(cadena))
print(len(a))

txt = "The best things in life are free!"
print("fri" in txt)

txt = "The best things in life are free!"
print("expensive" not in txt)

b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[-5:-2])

nombre = 'lUis'
print(nombre.upper())

apellido = 'PAz'
print(apellido.lower())

print(nombre.capitalize() + ' ' + apellido.capitalize())