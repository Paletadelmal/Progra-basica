#Ejercicio 1

nom = input("Introduce tu nombre: ")
edad= int(input("Introduce tu edad: "))

print("Hola ", nom, "Bienvenido")
print("Tu edad es: ", edad , "anos") 
print("---------------------------------------")

#Ejercicio 2

n1= float(input("Introduce un numero: "))
n2= float(input("Introduce otro numero: "))
suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2
print("La suma de los numeros es: ", suma)
print("La resta de los numeros es: ", resta)
print("La multiplicacion de los numeros es: ", multi)
print("La division de los numeros es: ", div)
print("---------------------------------------")

#Ejercicio 3

frase= str(input("Introduce una frase: "))

print(frase.lower())
print(frase.upper())
print(frase.title())
print("---------------------------------------")

#Ejercicio 4

from datetime import datetime

def calcular_dias_desde_nacimiento():
    fecha_nacimiento_str = input("Introduce tu fecha de nacimiento en formato DD/MM/AAAA: ")
    fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%d/%m/%Y")
    fecha_actual = datetime.now()
    diferencia_dias = (fecha_actual - fecha_nacimiento).days

    print(f"Han pasado {diferencia_dias} días desde tu fecha de nacimiento.")
calcular_dias_desde_nacimiento()
print("---------------------------------------")

#Ejercicio 5

def redondear_a_dos_decimales():
    numero = float(input("Introduce un número flotante: "))
    numero_redondeado = round(numero, 2)
    print(f"El número redondeado a dos decimales es: {numero_redondeado}")
redondear_a_dos_decimales()
print("---------------------------------------")

#Ejercicio 6

def mostrar_contenido_archivo():
    nom_archivo = input("Introduce el nombre del archivo de texto (con extensión): ")

    try:
        with open(nom_archivo, 'r') as archivo:
            contenido = archivo.read()
            print("\nContenido del archivo:")
            print(contenido)
    except FileNotFoundError:
        print("El archivo no fue encontrado. Por favor, verifica el nombre y la ruta.")

mostrar_contenido_archivo()
print("---------------------------------------")

#Ejercicio 7

def sumar_numeros():
    numeros = input("Introduce una lista de números separados por comas: ")
    lista_numeros = [float(num) for num in numeros.split(',')]
    suma = sum(lista_numeros)
    print(f"La suma de los números es: {suma}")

sumar_numeros()
print("---------------------------------------")

#Ejercicio 8

cadena_1=str(input("Introduce tu cadena: "))
cadena_2=str(input("Introduce tu otra cadena: "))

print(cadena_1 + " " + cadena_2)
print("---------------------------------------")

#Ejercicio 9

tu_nombre=str(input("Introduce tu nombre: "))
tu_nombre_invertido= tu_nombre[::-1]
print("Tu nombre invertido: ", tu_nombre_invertido )
print("---------------------------------------")

#Ejercicio 10

lista_calificaciones = []
num_calif= int(input("Ingrese el numero de calificaciones a registrar: "))
if num_calif <= 0:
    print("El numero de calificaciones debe ser mayor a 0")
else:
 for i in range(num_calif):

        calif = float(input("Ingrese la calificacion: "))
        lista_calificaciones.append(calif)
        promedio = sum(lista_calificaciones) / len(lista_calificaciones)

print("---------------------------------------")
#Ejercicio 11

peso=float(input("Introduce tu peso: "))
altura=float(input("Introduce tu altura: "))
imc=peso/(altura**2)
print ("Tu indice de masa corporal es: ",imc)
print("---------------------------------------")
#Ejercicio 12

import random


numero=random.randint(1,100)
print("ADIVINA EL NUMERO")

while True:
    numero_usuario=int(input("ingresa un numero:"))
    if numero_usuario==numero:
        print("Felicidades adivinaste el numero")
        break
    elif numero_usuario<numero:
        print("El numero es mayor")
    else:
        print("El numero es menor")
print("---------------------------------------")

#Ejercicio 13

def ordenar_nombres():
    cantidad = int(input("¿Cuántos nombres deseas ingresar? "))

    nombres = []
    for i in range(cantidad):
        nombre = input(f"Introduce el nombre {i+1}: ")
        nombres.append(nombre)
    nombres.sort()

    print("Nombres ordenados alfabéticamente:")

    for nombre in nombres:
        print(nombre)

ordenar_nombres()
print("---------------------------------------")

#Ejercicio 14

tabla_de_mult = int(input("Introduce cual tabla de multiplicar quieres: "))

for i in range(10):
    print(tabla_de_mult, " x ", (i+1), " = ", (tabla_de_mult * (i+1))) 
#ejercicio 15

oracion=str(input("Introduce tu oracion: "))
palabras= oracion.split()
print ("El numero de palabras en la oracion es: ", len(palabras))
print("---------------------------------------")