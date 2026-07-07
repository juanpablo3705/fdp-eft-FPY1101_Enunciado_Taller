def leer_opcion():
    while True:
        print("========== MENÚ PRINCIPAL ==========")
        print("1. Unidades por tipo de arreglo")
        print("2. Búsqueda de arreglos por rango de precio")
        print("3. Actualizar precio de arreglo")
        print("4. Agregar arreglo")
        print("5. Eliminar arreglo")
        print("6. Salir")
        print("=====================================")
        
        try:
            opcion = int(input("Ingrese una opción: "))

            if opcion <= 0 or opcion > 6:
                print("Debe seleccionar una opción válida")
            else:
                return opcion
        except ValueError:
            print("Debe seleccionar una opción válida")

# Busca unidades por tipo en la bodega según los arreglos disponibles
def unidades_tipo(tipo_buscado, diccionario_arreglos, diccionario_bodega):
    
    tipo_buscado = tipo_buscado.strip().lower() # RAMO -> ramo
    cantidad_arreglos = 0

    # Por cada arreglo en el diccionario validamos si es el tipo buscado (ej: FL01 -> ramo)
    for codigo_arreglo, arreglo in diccionario_arreglos.items():
        
        if tipo_buscado == arreglo[1]:
            
            # Por cada arreglo en bodega buscamos el ramo del tipo buscado (ej: FL01 -> 8)
            for codigo_arreglo_bodega, bodega in diccionario_bodega.items():
                if codigo_arreglo == codigo_arreglo_bodega:
                    cantidad_arreglos += bodega[1]
                    break

    print(f"La cantidad de arreglos disponibles para el tipo {tipo_buscado} es {cantidad_arreglos}")

# Mostrar todos los arreglos que estén en un rango de precio
def busqueda_precio(p_min, p_max, diccionario_arreglos, diccionario_bodega):

    lista_arreglos_rango = []
    
    # Por cada elemento en bodega validamos el rango de precio
    for codigo_bodega, arreglo_bodega in diccionario_bodega.items():

        # obtenemos el precio del arreglo en bodega
        precio = arreglo_bodega[0]

        # Validamos el rango de precio y stock
        if precio >= p_min and precio <= p_max and arreglo_bodega[1] > 0:
            
            # Por cada arreglo buscamos su nombre y lo agregamos a la lista de arreglos que coinciden con el rango
            for codigo_arreglo, arreglo in diccionario_arreglos.items():

                if codigo_arreglo == codigo_bodega:

                    lista_arreglos_rango.append(f"{arreglo[0]} -- {codigo_arreglo}")

                    break

    # Mostramos los arreglos de forma ordenada si encontramos alguno, sino mostramos un mensaje alternativo
    if len(lista_arreglos_rango) > 0:

        # Ordenamos la lista en memoria
        lista_arreglos_rango.sort()

        for arreglo in lista_arreglos_rango:
            print(arreglo)
    else:
        print("No hay arreglos en ese rango de precios.")


# Busque existencia de un codigo en particular
def buscar_codigo(codigo_buscado, diccionario_arreglos):

    codigo_buscado = codigo_buscado.strip().upper()

    for llave_arreglo in diccionario_arreglos.keys():

        if codigo_buscado == llave_arreglo:
            return True
        
    return False

# Elimina el arreglo desde ambos diccionarios solo si existe, devuelve true si lo elimino y false si no lo elimino
def eliminar_arreglo(codigo_buscado, diccionario_arreglos, diccionario_bodega):

    if buscar_codigo(codigo_buscado, diccionario_arreglos):
        
        del diccionario_arreglos[codigo_buscado]
        del diccionario_bodega[codigo_buscado]

        return True
    else:
        return False


# Programa principal
# Diccionario que representa cada arreglo, cada arreglo es un elemento que se indentifica con el codigo de arreglo
arreglos = {
    'FLO1': ['Ramo Primavera', 'ramo', 'rosado', 'M', True, 'primavera'],
    'FLO2': ['Caja Elegante', 'caja', 'blanco', 'L', True, 'todoaño'],
    'FLO3': ['Ramo Solar', 'ramo', 'amarillo', 'S', False, 'verano'],
    'FLO4': ['Centro Mesa', 'centro', 'rojo', 'M', True, 'todo año'],
    'FLO5': ['Ramo Bosque', 'ramo', 'verde', 'L', False, 'otoño'],
    'FLO6': ['Caja Noche', 'caja', 'morado', 'M', True, 'invierno'],
}

# Diccionario que representa la bodega, cada arreglo es un elemento que se indentifica con el codigo de arreglo
bodega = {
    'FLO1': [15990, 8],
    'FLO2': [29990, 3],
    'FLO3': [9990, 12],
    'FLO4': [24990, 5],
    'FLO5': [19990, 0],
    'FLO6': [22990, 6],
}

while True:
    opcion_seleccionada = leer_opcion()

    if opcion_seleccionada == 1:

        tipo_buscar = input("Ingresa el tipo de arreglo a buscar: ")
        unidades_tipo(tipo_buscar, arreglos, bodega)
    
    elif opcion_seleccionada == 2:

        try:
            rango_minimo = int(input("Ingresa el precio minimo buscado: "))
            rango_maximo = int(input("Ingresa el precio máximo buscado: "))

            if rango_minimo < 0 or rango_minimo > rango_maximo:
                print("Debe ingresar valores enteros positivos mayor que cero, el rango minimo debe ser menor al rango maximo")
            else:
                busqueda_precio(rango_minimo, rango_maximo, arreglos, bodega)

        except ValueError:
            print("Debe ingresar valores enteros")

    elif opcion_seleccionada == 5:
        
        codigo_eliminar = input("Ingresa el codigo del arreglo a eliminar: ")

        eliminado = eliminar_arreglo(codigo_eliminar, arreglos, bodega)

        if eliminado == True:
            print("Arreglo eliminado")
        else:
            print("El código no existe")

    elif opcion_seleccionada == 6:
        print("Programa finalizado.")
