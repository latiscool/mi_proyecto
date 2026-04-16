#Codifica el ejercicio 1. Básico
#Básico: imprime todos los números enteros del 0 al 100.
s = 0
for i in range(101):
    print(i)        

#Codifica el ejercicio 2. Múltiples de 2
#Múltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500
for i in range(2, 501, 2):
    print(i)    

#Codifica el ejercicio 3. Contando Vanilla Ice
#Contando Vanilla Ice: imprime los números enteros del 1 al 100. Si es divisible por 5 imprime “ice ice” en vez del número. Si es divisible por 10, imprime “baby”
for i in range(1, 101):
    if i % 5 == 0:
        print("ice ice")
    elif i % 10 == 0:
        print("baby")
    else:
        print(i)


#Codifica el ejercicio 4. Wow. Número gigante a la vista
#Wow. Número gigante a la vista: suma los números pares del 0 al 500,000 
# e imprime la suma total. (Sorpresa, será un número gigante).
suma = 0
for i in range(0, 500001, 2):
    suma += i       
print(suma)


#Codifica el ejercicio 5. Regrésame al 3
#Regrésame al 3: imprime los números positivos comenzando desde 2024, en cuenta regresiva de 3 en 3.
for i in range(2024, 0, -3):
    print(i)


#Codifica el ejercicio 6. Contador dinámico
#Contador dinámico: establece tres variables: numInicial, numFinal y multiplo. Comenzando en numInicial y pasando por numFinal, imprime los números enteros que sean múltiplos de multiplo. Por ejemplo: si numInicial = 3, numFinal = 10, y multiplo = 2, el bucle debería de imprimir 4, 6, 8, 10 (en líneas sucesivas).
numInicial = 3
numFinal = 10
multiplo = 2
for i in range(numInicial, numFinal + 1):
    if i % multiplo == 0:
        print(i)


