# función solo mostrar menú:
def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por tipo de arreglo")
    print("2. Búsqueda de arreglos por rango de precio")
    print("3. Actualizar precio de arreglo")
    print("4. Agregar arreglo")
    print("5. Eliminar arreglo")
    print("6. Salir")
    print("=====================================")

# funcion leer opción:
def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción del menú (1-6): "))
            if opcion >= 1 and opcion <= 6:
                return opcion
            else:
                print("Error, la opción debe estar entre 1 y 6.")
        except ValueError:
            print("Error, la opción debe ser un número entero.")

# funcion opcion 1 - unidades por tipo de arreglo:
def unidades_tipo(tipo, arreglos, bodega):
    contador_unidades = 0
    for clave, valores in arreglos.items():
        if valores[1] == tipo:
            contador_unidades = contador_unidades + bodega[clave][1]
    print(f"El total de arreglos correspondientes es de {contador_unidades}.")

# funcion opcion 2 - buqueda de arreglos por rango de precio:
def busqueda_precio(p_min, p_max, arreglos, bodega):
    lista_encontrados = []
    for clave, valores in bodega.items():
        if (valores[0] >= p_min) and (valores[0] <= p_max) and (valores[1] > 0):
            nombre = arreglos[clave][0]
            codigo = clave
            lista_encontrados.append(f"{nombre}--{codigo}")
    if len(lista_encontrados) == 0:
        print("Error, no hay arreglos en ese rango de precios.")
    else:
        lista_encontrados.sort()
        print(f"Los arreglos encontrados son: {lista_encontrados}.")

# funcion opcion 3 - buscar codigo:
def buscar_codigo(codigo, bodega):
    return codigo in bodega

# funcion opcion 3 - actualizar precio:
def actualizar_precio(codigo, nuevo_precio, bodega):
    if buscar_codigo(codigo, bodega):
        bodega[codigo][0] = nuevo_precio
        return True
    else:
        return False





# programa principal:
arreglos = {
    'FLO1': ['Ramo Primavera', 'ramo', 'rosado', 'M', True, 'primavera'],
    'FLO2': ['Caja Elegante', 'caja', 'blanco', 'L', True, 'todo año'],
    'FLO3': ['Ramo Solar', 'ramo', 'amarillo', 'S', False, 'verano'],
    'FLO4': ['Centro Mesa', 'centro', 'rojo', 'M', True, 'todo año'],
    'FLO5': ['Ramo Bosque', 'ramo', 'verde', 'L', False, 'otoño'],
    'FLO6': ['Caja Noche', 'caja', 'morado', 'M', True, 'invierno']
}
bodega = {
    'FLO1': [15990, 8],
    'FLO2': [29990, 3],
    'FLO3': [9990, 12],
    'FLO4': [24990, 5],
    'FLO5': [19990, 0],
    'FLO6': [22990, 6]
}
while True:
    mostrar_menu()
    opcion_elegida = leer_opcion()
    match opcion_elegida:
        case 1:
            if len(arreglos) == 0:
                print("Error, no hay arreglos registrados.")
            else:
                while True:
                    tipo = input("Ingrese tipo de arreglo: ").lower().strip()
                    if tipo != "":
                        break
                    else:
                        print("Error, debe ingresar un tipo de arreglo.")
                unidades_tipo(tipo, arreglos, bodega)
        case 2:
            if len(arreglos) == 0:
                print("Error, no hay arreglos registrados.")
            else:
                while True:
                    try:
                        p_min = int(input("Ingrese un precio mínimo para el rango a buscar: "))
                        if p_min >= 0:
                            break
                        else:
                            print("Error, el precio mínimo debe ser mayor o igual que cero.")
                    except ValueError:
                        print("Debe ingresar valores enteros.")
                while True:
                    try:
                        p_max = int(input("Ingrese un precio máximo para el rango a buscar: "))
                        if (p_max >= p_min) and (p_max) > 0:
                            break
                        else:
                            print("Error, el precio máximo debe ser mayor que el precio mínimo y mayor que cero.")
                    except ValueError:
                        print("Debe ingresar valores enteros.")
                busqueda_precio(p_min, p_max, arreglos, bodega)
        case 3:
            if len(bodega) == 0:
                print("Error, no hay arreglos registrados.")
            else:
                while True:
                    while True:
                        codigo = input("Ingrese el código del arreglo a actualizar: ").strip().upper()
                        if buscar_codigo(codigo, bodega) == False:
                            print("Error, el código no existe.")
                        else:
                            break
                    while True:
                        try:
                            nuevo_precio = float(input("Ingrese el nuevo precio: "))
                            if nuevo_precio <= 0:
                                print("Error, el nuevo precio debe ser mayor o igual que cero.")
                            else:
                                break
                        except ValueError:
                            print("Error, el nuevo precio debe ser un número entero o decimal.")
                    if actualizar_precio(codigo, nuevo_precio, bodega):
                        print("Precio actualizado con éxito.")
                    else:
                        print("Error, código no encontrado.")
                    otro_intento = input("¿Desea actualizar otro precio? (s/n)").lower()
                    if otro_intento != "s":
                        break
        case 4:
            print("4")
        case 5:
            print("5")
        case 6:
            print("Programa finalizado.")
            break