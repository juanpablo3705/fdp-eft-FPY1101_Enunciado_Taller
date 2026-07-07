def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por tipo de arreglo")
    print("2. Búsqueda de arreglos por rango de precio")
    print("3. Actualizar precio de arreglo")
    print("4. Agregar arreglo")
    print("5. Eliminar arreglo")
    print("6. Salir")
    print("=====================================")

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))

            if opcion > 0 and opcion <= 6:
                return opcion
            else:
                print("Debe seleccionar una opción válida")

        except ValueError:
            print("Debe seleccionar una opción válida")

def unidades_tipo(tipoBuscado, diccionarioArreglos, diccionarioBodega):

    tipoBuscado = tipoBuscado.strip().lower()
    acumulador_stock = 0
    
    for codigo_arreglo, lista_atributos in diccionarioArreglos.items():
        
        if lista_atributos[1] == tipoBuscado:
            
            for codigo_bodega, lista_atributos_bodega in diccionarioBodega.items():

                if codigo_arreglo == codigo_bodega:

                    acumulador_stock += lista_atributos_bodega[1]
                    break

    print(f"Existen {acumulador_stock} arreglos para el tipo {tipoBuscado}")


def busqueda_precio(p_min, p_max, diccionarioBodega, diccionarioArreglos):

    lista_arreglos = []

    for codigo_bodega, lista_atributos_bodega in diccionarioBodega.items():
        if lista_atributos_bodega[0] >= p_min and lista_atributos_bodega[0] <= p_max and lista_atributos_bodega[1] > 0:
            
            for codigo_arreglo, lista_atributos in diccionarioArreglos.items():

                if codigo_bodega == codigo_arreglo:
                    lista_arreglos.append(f"{lista_atributos[0]} -- {codigo_bodega}")
                    break

    if len(lista_arreglos) == 0:
        print("No hay arreglos en ese rango de precios.")
    else:

        lista_arreglos.sort()

        for arreglo in lista_arreglos:
            print(arreglo)

def buscar_codigo(codigo, diccionarioBodega):

    for codigo_bodega in diccionarioBodega.keys():

        if codigo == codigo_bodega: 
            return True
        
    return False

def actualizar_precio(codigo, nuevo_precio, diccionarioBodega):
    
    if buscar_codigo(codigo, diccionarioBodega) == True:

        lista_atributos = diccionarioBodega[codigo]
        
        lista_atributos[0] = nuevo_precio

        return True

    else:
        return False


# Aplicación principal

arreglos = {
    'FLO1': ['Ramo Primavera', 'ramo', 'rosado', 'M', True, 'primavera'],
    'FLO2': ['Caja Elegante', 'caja', 'blanco', 'L', True, 'todo año'],
    'FLO3': ['Ramo Solar', 'ramo', 'amarillo', 'S', False, 'verano'],
    'FLO4': ['Centro Mesa', 'centro', 'rojo', 'M', True, 'todo año'],
    'FLO5': ['Ramo Bosque', 'ramo', 'verde', 'L', False, 'otoño'],
    'FLO6': ['Caja Noche', 'caja', 'morado', 'M', True, 'invierno'],
}

bodega = {
    'FLO1': [15990, 8],
    'FLO2': [29990, 3],
    'FLO3': [9990, 12],
    'FLO4': [24990, 5],
    'FLO5': [19990, 0],
    'FLO6': [22990, 6],
}

while True:
    mostrar_menu()

    opcionSelecciona = leer_opcion()

    if opcionSelecciona == 1:

        tipo_buscado = input("Ingresa el tipo de arreglo: ")

        unidades_tipo(tipo_buscado, arreglos, bodega)

    elif opcionSelecciona == 2:

        while True:
            try:
                precio_minimo = int(input("Ingrese el precio minimo del rango: "))
                precio_maximo = int(input("Ingrese el precio maximo del rango: "))

                if precio_minimo < 0 or precio_minimo > precio_maximo:
                    print("Debe ingresar valores enteros positivos mayor que cero, el rango minimo debe ser menor al rango maximo")
                else:   
                    busqueda_precio(precio_minimo, precio_maximo, bodega, arreglos)
                    break

            except ValueError:
                print("Debe ingresar valores enteros")
    
    elif opcionSelecciona == 3:
        while True:
            codigo_buscado = input("Ingrese el codigo del arreglo a actualizar: ").strip().upper() # flo1 -> FLO1

            while True:
                try:
                    precio_nuevo = int(input("Ingrese el precio nuevo: "))

                    if precio_nuevo <= 0:
                        print("Debe ingresar valores enteros positivos")
                    else:
                        break
                except ValueError:
                    print("Debe ingresar valores enteros positivos")

            actualizado = actualizar_precio(codigo_buscado, precio_nuevo, bodega)

            if actualizado == True:
                print("Precio actualizado")
            else:
                print("El código no existe")

            otro_precio = input("¿Desea actualizar otro precio (s/n)?").lower()

            if otro_precio == 's':
                continue
            else:
                break
