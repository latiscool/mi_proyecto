

#1. Actualizar valores en diccionarios y listas
print ("1. Actualiza los valores en diccionarios y listas")

matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]
#Cambia el valor de 3 en matriz por 6. Una vez realizado el cambio tu matriz debería ser: [ [10, 15, 20], [6, 7, 14] ]
matriz[1][0] = 6
print(matriz)
#Cambia el nombre del primer cantante de “Ricky Martin” 
# a “Enrique Martin Morales”
cantantes[0]["nombre"] = "Enrique Martin Morales"
print(cantantes)
#En ciudades, cambia “Cancún” por “Monterrey”
ciudades["México"][2] = "Monterrey"
print(ciudades)
#En las coordenadas, cambia el valor de “latitud” por 9.9355431
coordenadas[0]["latitud"] = 9.9355431
print(coordenadas)


print()
#2. Iterar a través de una lista de diccionarios
print("2. Crea la función iterarDiccionario(lista)")

#Crea la función iterarDiccionario(lista) 
# que reciba una lista de diccionarios y recorra
#  cada diccionario de la lista e imprima cada llave y el valor correspondiente.
#  Por ejemplo:

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

def iterarDiccionario(lista):
    for diccionario in lista:
        # 1. Creamos una lista vacía para almacenar los textos de cada llave-valor
        pares = [] 
        
        for llave, valor in diccionario.items():
            # 2. Agregamos el formato deseado a nuestra lista temporal
            pares.append(f"{llave} - {valor}") 
            
        # 3. Usamos el método .join() para unir todos los elementos de la lista 'pares'
        # separándolos por una coma y un espacio.
        print(", ".join(pares)) 

iterarDiccionario(cantantes)
print()


#BONUS: Que aparezcan en este formato:
#nombre - Ricky Martin, pais - Puerto Rico
#nombre - Chayanne, pais - Puerto Rico
#nombre - José José, pais - México
#nombre - Juan Luis Guerra, pais - República Dominicana

#3. Obtener valores de una lista de diccionarios
print("3. Crea la función iterarDiccionario2(llave, lista)")

#Crea la función iterarDiccionario2(llave, lista) que reciba una cadena 
# con el nombre de una llave y una lista de diccionarios. 
# La función debe imprimir el valor almacenado para esa clave de cada diccionario que se encuentra en la lista.
#  Por ejemplo, iterarDiccionario2(“nombre”, cantantes) debe de imprimir:

def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        if llave in diccionario:
            print(diccionario[llave])

iterarDiccionario2("nombre", cantantes)
print()


# 4. Iterar a través de un diccionario con valores de lista
print("4. Crea la función imprimirInformacion(diccionario)")

# Crea una función imprimirInformacion(diccionario) que reciba un diccionario
#  en donde los valores son listas. La función debe imprimir el nombre de 
# cada clave junto con el tamaño de su lista y seguido de esto los valores de la lista para esa clave. Por ejemplo:

costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

#Imprime 5 ciudades
#Imprime 5 comidas
def imprimirInformacion(diccionario):
    for clave, lista in diccionario.items():
        print(f"{len(lista)} {clave.upper()}")
        for elemento in lista:
            print(elemento)
        print()  # Agrega una línea en blanco para separar cada sección

imprimirInformacion(costa_rica)



