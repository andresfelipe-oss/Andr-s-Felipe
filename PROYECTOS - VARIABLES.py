#Esto es un comenentario de una sola linea 
"""esto es un comenentario de 
varias linea"""

#inicializando variables
nombre="Andrés Felipe Huertas Barbosa"
edad=15 
estado=True 
nota=5.0

#Mostrar el contenido de las variables
print(nombre)
print(edad)
print(estado)
print(nota)

#Que tipo de dato contiene cada vaiable. 
print(type(nombre))
print(type(edad))
print(type(estado))
print(type(nota))

#vamos  utilizar la función input para recoger datos por medio del taclado.
nombre=input("cual es tu nombre? ")
edad=input("cual es tu edad? ")
estado=input("cual es tu estado? ")
nota=input("cual es tu nota? ")

#Para visualizar que guardamos en las variables anteriores
print("Hola,",nombre,"un gusto conocerte")
print("Tu edad es:",edad)
print("Tu estado es:",estado)
print("Tu nota es:",nota)