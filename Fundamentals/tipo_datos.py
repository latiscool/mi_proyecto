'''Tipos de Datos en Python
# Listas, son estructuras de datos mutables, se pueden modificar sus elementos
list_vacia=[]
gatos =["Garfield","Silvestre","Hello Kitty"]

#print print(gatos[2]) # Imprime el elemento en la posición 2, que es "Hello Kitty"
#ok ❯ python tipo_datos.py 
#ok Hello Kitty

gatos[1]="Tom" #! Cambia el elemento en la posición 1 de "Silvestre" a "Tom"
gatos.append("Felix") #! Agrega "Felix" al final de la lista
#print print(gatos)
#ok ❯ python tipo_datos.py
#ok  ['Garfield', 'Tom', 'Hello Kitty', 'Felix']

gatos.pop() #! Elimina el último elemento de la lista, que es "Felix"
#print print(gatos)
#ok ❯ python tipo_datos.py
#ok  ['Garfield', 'Tom', 'Hello Kitty']

gatos.pop(1) #! Elimina el elemento en la posición 1, que es "Tom"
print(gatos)
#ok ❯ python tipo_datos.py


# Tuplas, son inmutables, no se pueden modificar sus elementos

perros = ("Scooby Doo", "Gran Danes", "Scooby Galletas")
print(perros[0]) #! Imprime el elemento en la posición 0, que es "Scooby Doo"
perros[2]= " comida de perro" #! Esto generará un error porque las tuplas no se pueden modificar
#print print(perros) #! Esto no se ejecutará debido al error anterior


'''
# Diccionarios, son estructuras de datos mutables, se pueden modificar sus elementos

diccionario_vacio = {}
persona ={"nombre":"Carmen", "edad":30, "altura": 1.71, "usa_lentes": False}
persona ["nombre"]= "Valeria" #! Cambia el valor asociado a la clave "nombre" de "Carmen" a "Valeria"
persona["hobbies"] = ["jugar videojuegos", "programacion"] #! Agrega una nueva clave "hobbies" con una lista de hobbies como valor

#print print(persona)#! Imprime el diccionario actualizado con los cambios realizados
#ok ❯ python tipo_datos.py
#ok  {'nombre': 'Valeria', 'edad': 30, 'altura': 1.71, 'usa_lentes': False, 'hobbies': ['jugar videojuegos', 'programacion']}

altura = persona.pop("altura") #! Elimina la clave "altura" y devuelve su valor, que es 1.71 y lo asigna a la variable altura
print(altura) #! Imprime el valor de la variable altura, que es 1.71
print(persona) #! Imprime el diccionario actualizado sin la clave "altura"
#ok ❯ python tipo_datos.py
#ok 1.71
#ok  {'nombre': 'Valeria', 'edad': 30, 'usa_l

#Len, es una función incorporada en Python que se utiliza para obtener 
# la longitud (número de elementos) de un objeto, como una lista, tupla, diccionario, cadena de texto, entre otros.

print(len(persona)) #! Imprime la longitud del diccionario persona, que es 4 porque tiene 4 claves
#ok ❯ python tipo_datos.py
#ok 4

