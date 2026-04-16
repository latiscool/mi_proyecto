# CADENAS

#ok CONVERSION

# DE NUMERO A CADENA
''' 
#! print ("¿Cuantas voclaes hat? " + 5) 
# Esto no se puede hacer, no se pueden sumar un string 
# con un numero, hay que convertir el numero a string

print("¿Cuantas voclaes hat? " + str(5))
#ok ❯ python cadenas.py
#ok ¿Cuantas voclaes hat? 5

# DE CADENA A NUMERO

tiempo_preparacion = 1
tiempo_horneado = "2"
#! tiempo_total =tiempo_preparacion + tiempo_horneado 
# Esto no se puede hacer, no se pueden sumar un numero con un string, 
# hay que convertir el string a numero 

tiempo_total = tiempo_preparacion + int(tiempo_horneado)

print(tiempo_total)
#ok ❯ python cadenas.py
#ok 3
'''

# Interpolación de cadenas "f"

nombre = "Marcelo"
edad = 29

print(f"Mi nomre es {nombre} y tengo {edad} añode de edad.")