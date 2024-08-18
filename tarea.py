#Ejercicio 1

def max_in_list(lista):
    num_mayor = lista[0]
    for num in lista:
        if num > num_mayor:
            num_mayor = num
    return num_mayor

l = int(input("Introduce la longitud de la lista: "))
llista = []

for i in range(l):
    llista.append(int(input("Introduce el número: ")))

num_mayor = max_in_list(llista)
print("El número mayor en la lista es:", num_mayor)
print("---------------------------------------")

#Ejercicio 2

def mas_larga():
    long = int(input("¿Cuántas palabras quieres ingresar? "))
    lista_de_palabras = []
    for i in range(long):
        palabra = input(f"Introduce la palabra {i+1}: ")
        lista_de_palabras.append(palabra)

    palabra_mas_larga = ""

    for palabra in lista_de_palabras:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra
    return palabra_mas_larga

print("La palabra más larga es:", mas_larga())
print("---------------------------------------")

#Ejercicio 3

def filtrar_palabras():
    long = int(input("¿Cuántas palabras quieres ingresar? "))
    lista_de_palabras = []
    for i in range(long):
        palabra = input(f"Ingrese la palabra {i+1}: ")
        lista_de_palabras.append(palabra)
    
    n = int(input("Ingrese un valor entero para filtrar las palabras que tengan mas caracteres que el valor ingresado: "))
    palabras_filt = []
    for palabra in lista_de_palabras:
        if len(palabra) > n:
            palabras_filt.append(palabra)
    return palabras_filt

palabras_filtradas = filtrar_palabras()
print("Palabras filtradas:", palabras_filtradas)
print("---------------------------------------")

#Ejercicio 4

def contar_mayusculas(cadena):
    cont_mayusculas = 0
    for caracter in cadena:
        if caracter.isupper():
            cont_mayusculas += 1
    return cont_mayusculas

cadena_usuario = input("Ingrese una palabra/oracion con letras mayusculas y minusculas: ")
num_mayusculas = contar_mayusculas(cadena_usuario)
print("La cadena tiene", num_mayusculas, "letras mayúsculas.")
print("---------------------------------------")

#Ejercicio 5

def binario_a_entero(binario):
    entero = int(binario, 2)
    return entero

num_binario = input("Ingrese un número binario: ")
num_entero = binario_a_entero(num_binario)
print(f"El número binario {num_binario} es {num_entero} en decimal.")
print("---------------------------------------")

#Ejercicio 6

def calcul_edad(año_nacimiento, año_actual):
    return año_actual - año_nacim

año_actual = int(input("Ingrese el año actual: "))
personas = []
for i in range(3):
    nombre = input(f"Ingrese el nombre de la persona {i + 1}: ")
    año_nacim = int(input(f"Ingrese el año de nacimiento de {nombre}: "))
    edad = calcul_edad(año_nacim, año_actual)
    personas.append((nombre, edad))

print("\nEdades que cumplirán este año:")
for nombre, edad in personas:
    print(f"{nombre} cumplirá {edad} años en {año_actual}.")
print("---------------------------------------")

#Ejercicio 7

edades = []
for i in range(10):
    edad = int(input(f"Ingrese la edad de la persona {i + 1}: "))
    edades.append(edad)

edades_tuple = tuple(edades)
mayores_de_20 = sum(1 for edad in edades_tuple if edad > 20)
print(f"La cantidad de personas con edades superiores a 20 es: {mayores_de_20}")
print("---------------------------------------")

#Ejercicio 8

nombres = ["Barbara", "Leslie", "Nicolas", "Estefany", "Zulema", "Javier", "Ian", "Irma", "Aranza", "Pancho"]
letra = input("Ingrese la letra por la que desea buscar nombres: ").strip().upper()
cant = sum(1 for nombre in nombres if nombre.upper().startswith(letra))

print(f"La cantidad de nombres que comienzan con la letra '{letra}' es: {cant}")
print("---------------------------------------")

#Ejercicio 9

def contar_vocales(palab):
    conteo_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    palab = palab.lower()
    
    for letra in palab:
        if letra in conteo_vocales:
            conteo_vocales[letra] += 1
    for vocal, conteo in conteo_vocales.items():
        print(f"Cantidad de '{vocal}' en la palabra: {conteo}")

palab_usuario = input("Ingrese una palabra: ")
contar_vocales(palab_usuario)
print("---------------------------------------")

#Ejercicio 10

def es_bisiesto(año):
    
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False

año_usuario = int(input("Ingrese un año: "))

if es_bisiesto(año_usuario):
    print(f"El año {año_usuario} es un año bisiesto.")
else:
    print(f"El año {año_usuario} no es un año bisiesto.")
print("---------------------------------------")