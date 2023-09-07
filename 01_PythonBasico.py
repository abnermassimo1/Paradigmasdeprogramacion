#===========================================================
#          Martinez Castañeda Abner Alfredo 
#=============================================================

#          Pardigmas de Programacion
#          Matematica Algoritmica
#          ESFM-IPN     sept- 2023

#=============================================================

'''ESTE ES UN SUPERCOMENTARIO
    DE INICIO A NUESTRO RESUMEN
'''
#=============================================================

# OPERACIONES BÁSICAS:

print (2+3)     #suma
print (2*3)     #multiplicacion
print (2/3)     #division
print (2**10)   #potencia
print (2**0.5)  #raiz cuadrada 
print (10%2)    #modulo
print (10%0.1)  #exclusivo en python

#=============================================================
# Para saber el tipo de objeto se usa type

t=0
print(type(t)) # entero
t=3.6
print(type(t)) # real (flotante)
t=True
print(type(t)) # booleano (bool)

#=============================================================
# Mensajes a pantalla

print ("Este es un comando de python","Este es otro enunciado", t)
print ('id: ', 1)
print ('First name:', 'Steve')
print ('Lasta Name:', 'Jobs')
print("vamos a sumar esto" + "con esto otro")

#============================================================
# Continuar una instrccion en varios renglones
if 100 > 99 and \
     200 <= 300 and \
     True != False:
         print('Hola mundo!')

#=============================================================
# Comandos diferentes en la misma linea

print ("Hola"); print("tu!!")   #Se considera mala practica

#=============================================================
#Usando parentesis redondos, cuadrados o llaves
#se puede escribir en varios renglones


lista = [1, 2, 3, 4,
        5, 6, 7, 8,
        9, 10, 11, 12]

matriz = [ [1,2,3,4],[5,6,7,8],[9,10,11,12] ]

print(lista)
print(matriz)

#==============================================================
# Indentacion estricta para procesos dependientes de : (dos puntos)
if 10 >5:
    print ("diez es mayor que cinco")
    print("otra indentacion")
for i in lista:
    print(i)
    print("ok")
if 10>5:
    print("verdadero")
elif 5>3: # comienza segundo condicional
    print ("esto no se imprimira")
else:
    print ("aqui nunca llega")


#=================================================================
#Funciones

def say_hello(name):
    print("Hello", name)
    print("Welcome to Phyton Tutoriales")

say_hello("Julian")

#=================================================================



