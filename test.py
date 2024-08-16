#ejercicio 1|
 
x = int(input("Introduce un numero: "))
y = int(input("Introduce otro numero: "))
 
if x > y:
    print("El numero mayor es: ",x)
else:
    print("El numero mayor es: ",y)
    
 
#ejercicio 2
 
a = int(input("Introduce un numero: "))
b = int(input("Introduce otro numero: "))
c = int(input("Introduce otro numero: "))
 
def max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print("El numero maximo es: ",max(a,b,c))
 
#ejercicio 3
 
def longitud(elemento):
    contador = 0
    for _ in elemento:
        contador += 1
    return contador

j = int(input("Cuantos elementos tiene l alista: "))
lista = []
for i in range(j):
    lista.append(int(input("Introduce el numero")))
 
print("Tiene una longitud de",longitud(lista), "caracteres")
 
 #ejercicio 4

es_vocal=str(input("introduce una letra por favor: "))
 
if es_vocal == "a" or es_vocal == "e" or es_vocal == "i" or es_vocal == "o" or es_vocal == "u":
        print(True)
 
elif es_vocal == "A" or es_vocal == "E" or es_vocal == "I" or es_vocal == "O" or es_vocal == "U":
        print(True)
    
else:
        print(False) 

#Ejercicio 5

# Definir la función longitud para obtener la longitud de una lista
def longitud(lista):
    return len(lista)

# Definir la función suma para sumar todos los elementos de una lista
def suma(lista):
    g = 0
    for num in lista:
        g += num
    return g

# Definir la función multi para multiplicar todos los elementos de una lista
def multi(lista):
    g = 1
    for num in lista:
        g *= num
    return g

# Leer el número de elementos
y = int(input("¿Cuántos elementos tiene la lista? "))
lista = []

# Leer los elementos de la lista
for _ in range(y):
    lista.append(int(input("Introduce el número: ")))

# Imprimir la longitud de la lista
print("Tiene una longitud de", longitud(lista), "elementos")

# Imprimir la suma de los elementos de la lista
print("La suma de los elementos es", suma(lista))

# Imprimir el producto de los elementos de la lista
print("El producto de los elementos es", multi(lista))


#Ejercicio 6

def inversa(cadena) :
   cadena_inversa = cadena[::-1]
   return cadena_inversa
 
print(inversa("Hola Don Pepito"))

#Ejercicio 7

def es_palindromo(cadena):
    cadena_limpia = cadena.replace(" ", "").lower()
    cadena_invertida = cadena_limpia[::-1]
    return cadena_limpia == cadena_invertida
print(es_palindromo("radar"))
print(es_palindromo("hola"))
print(es_palindromo("A man a plan a canal Panama"))

#Ejercicio 8

def superposicion(lista1, lista2):
    for elemento1 in lista1:
        for elemento2 in lista2:
            if elemento1 == elemento2:
                return True
    return False
print(superposicion([1, 2, 3], [3, 4, 5]))
print(superposicion([1, 2, 3], [4, 5, 6]))
print(superposicion([], [1, 2, 3]))
print(superposicion([1, 2, 3], []))
print(superposicion([1, 2, 3], [2]))

#Ejercicio 9 

def generar_n_caracteres(n, caracter):
    if len(caracter) != 1:
        raise ValueError("El segundo argumento debe ser un carácter único.")
    return caracter * n
print(generar_n_caracteres(5, "x"))
print(generar_n_caracteres(3, "#"))
print(generar_n_caracteres(0, "a"))

#Ejercicio 10

def histograma(lista):
    for numero in lista:
        print('*' * numero)
histograma([4, 9, 7])
