# funcion mostrar menú:
def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por tipo de arreglo")
    print("2. Búsqueda de arreglos por rango de precio")
    print("3. Actualizar precio de arreglo")
    print("4. Agregar arreglo")
    print("5. Eliminar arreglo")
    print("6. Salir")
    print("=====================================")

# funcion leer opcion menú:
def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción del menú: "))
            if (opcion >= 1) and (opcion <= 6):
                return opcion
            else:
                print("Debe seleccionar una opción válida.")
        except ValueError:
            print("Debe seleccionar una opción válida.")

# funcion opcion 1 - unidades por tipo de arreglo:
def unidades_tipo(tipo, arreglos, bodega):
    acumulador_arreglos = 0
    for clave, valores in arreglos.items():
        if tipo == valores[1]:
            acumulador_arreglos = acumulador_arreglos + bodega[clave][1]
    print(f"Total de unidades por tipo de arreglo: {acumulador_arreglos}.")

# funcion opcion 2 - busqueda de arreglos por rango de precios:
def busqueda_precio(p_min, p_max, bodega, arreglos):
    lista_encontrados = []
    for clave, valores in bodega.items():
        if (valores[0] >= p_min) and (valores[0] <= p_max) and (valores[1] != 0):
            nombre = arreglos[clave][0]
            codigo = clave
            lista_encontrados.append(f"{nombre}--{codigo}")
    if len(lista_encontrados) == 0:
        print("No hay arreglos en ese rango de precios.")
    else:
        lista_encontrados.sort()
        print(f"Arreglos encontrados en el rango de precios: {lista_encontrados}")



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
            while True:
                tipo = input("Ingrese el tipo de arreglos para mostrar sus unidades: ").strip().lower()
                if tipo.strip() != "":
                    break
                else:
                    print("Error, el tipo de  arreglos no puede estar vacío.")
            unidades_tipo(tipo, arreglos, bodega)
        case 2:
            while True:
                try:
                    p_min = int(input("Ingrese el precio mínimo: "))
                    p_max = int(input("Ingrese el precio máximo: "))
                except ValueError:
                    print("Debe ingresar valores enteros.")
                    continue
                if (p_min >= 0) and (p_max >= 0) and (p_min <= p_max):
                    break
                else:
                    print("Error, el precio mínimo debe ser menor o igual al precio máximo y ambos mayores que cero.")          
            busqueda_precio(p_min, p_max, bodega, arreglos)
        case 3:
            print("3")
        case 4:
            print("4")
        case 5:
            print("5")
        case 6:
            print("Programa finalizado.")
            break