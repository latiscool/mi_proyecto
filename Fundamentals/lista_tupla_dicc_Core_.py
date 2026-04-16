# Ejercicios Listas, Tuplas y Diccionarios (Core)
'''

#ok 1.- Carga de Datos:
Crea una lista de diccionarios llamada ventas, donde cada diccionario represente una venta.
 Cada venta debe incluir las siguientes claves:

«fecha»: una cadena de texto que represente la fecha de la venta (por ejemplo, «2024-01-01»).
«producto»: una cadena de texto que represente el nombre del producto vendido.
«cantidad»: un número entero que represente la cantidad de productos vendidos.
«precio»: un número flotante que represente el precio unitario del producto.

'''



ventas = [
    {"fecha": "2024-01-01", "producto": "Laptop",    "cantidad": 3,  "precio": 850000.0},
    {"fecha": "2024-01-01", "producto": "Mouse",     "cantidad": 10, "precio": 15000.0},
    {"fecha": "2024-01-02", "producto": "Laptop",    "cantidad": 2,  "precio": 850000.0},
    {"fecha": "2024-01-02", "producto": "Teclado",   "cantidad": 5,  "precio": 35000.0},
    {"fecha": "2024-01-03", "producto": "Mouse",     "cantidad": 8,  "precio": 15000.0},
    {"fecha": "2024-01-03", "producto": "Monitor",   "cantidad": 4,  "precio": 250000.0},
    {"fecha": "2024-01-04", "producto": "Teclado",   "cantidad": 3,  "precio": 35000.0},
    {"fecha": "2024-01-04", "producto": "Monitor",   "cantidad": 2,  "precio": 250000.0},
    {"fecha": "2024-01-05", "producto": "Laptop",    "cantidad": 1,  "precio": 850000.0},
    {"fecha": "2024-01-05", "producto": "Mouse",     "cantidad": 15, "precio": 15000.0},
]

print("=" * 55) # Imprime una línea de separación
print("LISTA DE VENTAS ORIGINAL")
print("=" * 55)
for venta in ventas:
    print(venta)

'''
#ok 2.-Cálculo de Ingresos Totales:
Utiliza un bucle para iterar sobre la lista ventas y calcular los ingresos totales generados por todas las ventas.
Los ingresos totales se calculan multiplicando la cantidad vendida 
por el precio unitario para cada venta y sumando los resultados.
'''
ingresos_totales = 0

for venta in ventas:
    ingreso_venta = venta["cantidad"] * venta["precio"] # Calcula el ingreso de cada venta
    ingresos_totales += ingreso_venta # Suma el ingreso de cada venta al total

print("\n" + "=" * 55)
print("INGRESOS TOTALES GENERADOS")
print("=" * 55)
print(f"Ingresos totales: ${ingresos_totales:,.0f}")


'''
#ok 3.-Análisis del Producto Más Vendido:
Crea un diccionario llamado ventas_por_producto donde las claves sean los nombres de los productos y los valores sean la cantidad total vendida de cada producto.
Utiliza este diccionario para identificar el producto que tuvo la mayor cantidad total vendida.


'''

ventas_por_producto = {}

for venta in ventas:
    producto = venta["producto"] # Obtiene el nombre del producto de la venta
    cantidad = venta["cantidad"] # Obtiene la cantidad vendida de la venta
    if producto in ventas_por_producto: # Si el producto ya está en el diccionario, suma la cantidad
        ventas_por_producto[producto] += cantidad
    else:
        ventas_por_producto[producto] = cantidad # Si el producto no está en el diccionario, lo agrega con la cantidad inicial

# Identificar el producto con mayor cantidad total
producto_mas_vendido = ""
mayor_cantidad = 0

for producto, cantidad in ventas_por_producto.items(): # Itera sobre el diccionario para encontrar el producto con la mayor cantidad vendida
    if cantidad > mayor_cantidad:
        mayor_cantidad = cantidad
        producto_mas_vendido = producto

print("\n" + "=" * 55)
print("PRODUCTO MÁS VENDIDO")
print("=" * 55)
print(f"Ventas por producto: {ventas_por_producto}")
print(f"Producto más vendido: {producto_mas_vendido} ({mayor_cantidad} unidades)")

'''
#ok 4.-Promedio de Precio por Producto:
Crea un diccionario llamado precios_por_producto donde las claves sean los nombres de los productos y los valores sean tuplas. Cada tupla debe contener dos elementos: la suma de los precios de venta de todas las unidades vendidas y la cantidad total de unidades vendidas.
Calcula el precio promedio de venta para cada producto utilizando la información de este diccionario.
'''
precios_por_producto = {}

for venta in ventas: # Itera sobre cada venta para calcular la suma de precios y cantidad total por producto
    producto = venta["producto"]
    precio   = venta["precio"]
    cantidad = venta["cantidad"]

    ingreso = precio * cantidad # Calcula el ingreso total de la venta (precio por cantidad)

    if producto in precios_por_producto: # Si el producto ya está en el diccionario, actualiza la suma de precios y cantidad total
        suma_anterior, cantidad_anterior = precios_por_producto[producto]
        precios_por_producto[producto] = (suma_anterior + ingreso, cantidad_anterior + cantidad)
    else:
        precios_por_producto[producto] = (ingreso, cantidad)

print("\n" + "=" * 55)
print("PRECIO PROMEDIO POR PRODUCTO")
print("=" * 55)

for producto, tupla in precios_por_producto.items(): # Itera sobre el diccionario para calcular e imprimir el precio promedio de cada producto
    suma_precios, total_unidades = tupla # Desempaqueta la tupla para obtener la suma de precios y cantidad total
    precio_promedio = suma_precios / total_unidades
    print(f"{producto}: Precio promedio = ${precio_promedio:,.0f} (sobre {total_unidades} unidades)")



'''
#ok 5.-Ventas por Día:
Crea un diccionario llamado ingresos_por_dia donde las claves sean las fechas y los valores sean los ingresos totales generados en cada día.
Utiliza un bucle para calcular los ingresos totales por día y almacenar estos valores en el diccionario.

'''
ingresos_por_dia = {}

for venta in ventas: # Itera sobre cada venta para calcular los ingresos totales por día
    fecha   = venta["fecha"]
    ingreso = venta["cantidad"] * venta["precio"] 
    if fecha in ingresos_por_dia: # Si la fecha ya está en el diccionario, suma el ingreso de la venta al total del día
        ingresos_por_dia[fecha] += ingreso
    else:
        ingresos_por_dia[fecha] = ingreso

print("\n" + "=" * 55)
print("INGRESOS TOTALES POR DÍA")
print("=" * 55)
for fecha, ingreso in ingresos_por_dia.items():
    print(f"{fecha}: ${ingreso:,.0f}")


'''
#ok Representación de Datos:
Crea un diccionario llamado resumen_ventas donde las claves sean los nombres de los productos y los valores sean diccionarios anidados. Cada diccionario anidado debe contener:
«cantidad_total»: la cantidad total vendida del producto.
«ingresos_totales»: los ingresos totales generados por la venta del producto.
«precio_promedio»: el precio promedio de venta del producto.
'''

resumen_ventas = {}

for producto in ventas_por_producto: # Itera sobre cada producto en el diccionario de ventas por producto para construir el resumen de ventas
    cantidad_total   = ventas_por_producto[producto]
    suma_ingresos, _ = precios_por_producto[producto]
    precio_promedio  = suma_ingresos / cantidad_total

    resumen_ventas[producto] = {
        "cantidad_total":   cantidad_total,
        "ingresos_totales": suma_ingresos,
        "precio_promedio":  precio_promedio
    }

print("\n" + "=" * 55)
print("RESUMEN DE VENTAS POR PRODUCTO")
print("=" * 55)
for producto, datos in resumen_ventas.items():
    print(f"\n{producto}:")
    print(f"  - Cantidad total vendida : {datos['cantidad_total']} unidades")
    print(f"  - Ingresos totales       : ${datos['ingresos_totales']:,.0f}")
    print(f"  - Precio promedio        : ${datos['precio_promedio']:,.0f}")

print("\n" + "=" * 55)
print("FIN DEL ANÁLISIS")
print("=" * 55)


'''
RESULTADO DE LA EJECUCIÓN DEL CÓDIGOS
=======================================================
LISTA DE VENTAS ORIGINAL
=======================================================
{'fecha': '2024-01-01', 'producto': 'Laptop', 'cantidad': 3, 'precio': 850000.0}
{'fecha': '2024-01-01', 'producto': 'Mouse', 'cantidad': 10, 'precio': 15000.0}
{'fecha': '2024-01-02', 'producto': 'Laptop', 'cantidad': 2, 'precio': 850000.0}
{'fecha': '2024-01-02', 'producto': 'Teclado', 'cantidad': 5, 'precio': 35000.0}
{'fecha': '2024-01-03', 'producto': 'Mouse', 'cantidad': 8, 'precio': 15000.0}
{'fecha': '2024-01-03', 'producto': 'Monitor', 'cantidad': 4, 'precio': 250000.0}
{'fecha': '2024-01-04', 'producto': 'Teclado', 'cantidad': 3, 'precio': 35000.0}
{'fecha': '2024-01-04', 'producto': 'Monitor', 'cantidad': 2, 'precio': 250000.0}
{'fecha': '2024-01-05', 'producto': 'Laptop', 'cantidad': 1, 'precio': 850000.0}
{'fecha': '2024-01-05', 'producto': 'Mouse', 'cantidad': 15, 'precio': 15000.0}

=======================================================
INGRESOS TOTALES GENERADOS
=======================================================
Ingresos totales: $7,375,000

=======================================================
PRODUCTO MÁS VENDIDO
=======================================================
Ventas por producto: {'Laptop': 6, 'Mouse': 33, 'Teclado': 8, 'Monitor': 6}
Producto más vendido: Mouse (33 unidades)

=======================================================
PRECIO PROMEDIO POR PRODUCTO
=======================================================
Laptop: Precio promedio = $850,000 (sobre 6 unidades)
Mouse: Precio promedio = $15,000 (sobre 33 unidades)
Teclado: Precio promedio = $35,000 (sobre 8 unidades)
Monitor: Precio promedio = $250,000 (sobre 6 unidades)

=======================================================
INGRESOS TOTALES POR DÍA
=======================================================
2024-01-01: $2,700,000
2024-01-02: $1,875,000
2024-01-03: $1,120,000
2024-01-04: $605,000
2024-01-05: $1,075,000

=======================================================
RESUMEN DE VENTAS POR PRODUCTO
=======================================================

Laptop:
  - Cantidad total vendida : 6 unidades
  - Ingresos totales       : $5,100,000
  - Precio promedio        : $850,000

Mouse:
  - Cantidad total vendida : 33 unidades
  - Ingresos totales       : $495,000
  - Precio promedio        : $15,000

Teclado:
  - Cantidad total vendida : 8 unidades
  - Ingresos totales       : $280,000
  - Precio promedio        : $35,000

Monitor:
  - Cantidad total vendida : 6 unidades
  - Ingresos totales       : $1,500,000
  - Precio promedio        : $250,000

=======================================================
FIN DEL ANÁLISIS
=======================================================

'''