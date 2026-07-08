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

# funcion opcion 3, 4 y 5 - buscar codigo:
def buscar_codigo(codigo, bodega):
    return codigo in bodega

# funcion opcion 3 - actualizar precio:
def actualizar_precio(codigo, nuevo_precio, bodega):
    if buscar_codigo(codigo, bodega):
        bodega[codigo][0] = nuevo_precio
        return True
    else:
        return False

# funcion opcion 4 - validar codigo:
def validar_codigo(codigo, bodega):
    if buscar_codigo(codigo, bodega) or (codigo.strip() == ""):
        return False
    else:
        return True

# funcion opcion 4 - validar nombre:
def validar_nombre(nombre):
    if nombre.strip() == "":
        return False
    else:
        return True
    
# funcion opcion 4 - validar tipo:
def validar_tipo(tipo):
    if tipo.strip() == "":
        return False
    else:
        return True
    
# funcion opcion 4 - validar color principal:
def validar_color_principal(color_principal):
    if color_principal.strip() == "":
        return False
    else:
        return True
    
# funcion opcion 4 - validar tamaño:
def validar_tamano(tamano):
    if (tamano == "S") or (tamano == "M") or (tamano == "L"):
        return True
    else:
        return False

# funcion opcion 4 - validar incluye tarjeta:
def validar_incluye_tarjeta(incluye_tarjeta):
    if (incluye_tarjeta == "s") or (incluye_tarjeta == "n"):
        return True
    else:
        return False
    
# funcion opcion 4 - validar temporada:
def validar_temporada(temporada):
    if temporada.strip() == "":
        return False
    else:
        return True
    
# funcion opcion 4 - validar precio:
def validar_precio(precio):
    if precio > 0:
        return True
    else:
        return False
    
# funcion opcion 4 - validar unidades:
def validar_unidades(unidades):
    if unidades >= 0:
        return True
    else:
        return False
    
# funcion opcion 4 - agregar arreglo:
def agregar_arreglo(arreglos, bodega, codigo, nombre, tipo, color_principal, tamano, incluye_tarjeta, temporada, precio, unidades):
    if buscar_codigo(codigo, bodega):
        print("Error, el código ya existe.")
        return False
    else:
        arreglos[codigo] = [nombre, tipo, color_principal, tamano, incluye_tarjeta, temporada]
        bodega[codigo] = [precio, unidades]
        print("Arreglo agregado con éxito.")
        return True

# funcion opcion 5 - eliminar arreglo:
def eliminar_arreglo(arreglos, bodega, codigo):
    if buscar_codigo(codigo, bodega):
        del(bodega[codigo])
        del(arreglos[codigo])
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
                            nuevo_precio = int(input("Ingrese el nuevo precio: "))
                            if nuevo_precio <= 0:
                                print("Error, el nuevo precio debe ser mayor o igual que cero.")
                            else:
                                break
                        except ValueError:
                            print("Error, el nuevo precio debe ser un número entero.")
                    if actualizar_precio(codigo, nuevo_precio, bodega):
                        print("Precio actualizado con éxito.")
                    else:
                        print("Error, código no encontrado.")
                    otro_intento = input("¿Desea actualizar otro precio? (s/n)").lower()
                    if otro_intento != "s":
                        break
        case 4:
            while True:
                codigo = input("Ingrese el código del arreglo a agregar: ").upper().strip()
                if validar_codigo(codigo, bodega):
                    break
                else:
                    print("Error, el código no debe estar vacío ni ser sólo espacios o ya estar registrado.")
            while True:
                nombre = input("Ingrese el nombre del arreglo a agregar: ").title().strip()
                if validar_nombre(nombre):
                    break
                else:
                    print("Error, el nombre no debe estar vacío ni ser sólo espacios.")
            while True:
                tipo = input("Ingrese el tipo del arreglo a agregar: ").lower().strip()
                if validar_tipo(tipo):
                    break
                else:
                    print("Error, el tipo no debe estar vacío ni ser sólo espacios.")
            while True:
                color_principal = input("Ingrese el color principal del arreglo a agregar: ").lower().strip()
                if validar_color_principal(color_principal):
                    break
                else:
                    print("Error, el color principal no debe estar vacío ni ser sólo espacios.")
            while True:
                tamano = input("Ingrese el tamaño del arreglo a agregar (S/M/L): ").upper().strip()
                if validar_tamano(tamano):
                    break
                else:
                    print("Error, el tamaño debe ser exactamente S, M ó L.")
            while True:
                incluye_tarjeta = input("Ingrese si el arreglo incluye tarjeta (s = sí, n = no): ").strip().lower()
                if validar_incluye_tarjeta(incluye_tarjeta):
                    if incluye_tarjeta == "s":
                        incluye_tarjeta = True
                    else:
                        incluye_tarjeta = False
                    break
                else:
                    print("Error, sólo debe ingresar exactamente s ó n.")
            while True:
                temporada = input("Ingrese la temporada a la que corresponde el arreglo: ").strip().lower()
                if validar_temporada(temporada):
                    break
                else:
                    print("Error, la temporada no debe estar vacía ni ser sólo espacios.")
            while True:
                try:
                    precio = int(input("Ingrese el precio del arreglo a agregar: "))
                    if validar_precio(precio):
                        break
                    else:
                        print("Error, el precio debe ser mayor que cero.")
                except ValueError:
                    print("Error, el precio debe ser un número entero.")
            while True:
                try:
                    unidades = int(input("Ingrese el número de unidades del arreglo a agregar: "))
                    if validar_unidades(unidades):
                        break
                    else:
                        print("Error, las unidades deben ser un número mayor o igual que cero.")
                except ValueError:
                    print("Error, las unidades deben ser un número entero.")
            agregar_arreglo(arreglos, bodega, codigo, nombre, tipo, color_principal, tamano, incluye_tarjeta, temporada, precio, unidades)
        case 5:
            if len(bodega) == 0:
                print("Error, no hay arreglos registrados.")
            else:
                while True:
                    codigo = input("Ingrese el código del arreglo a eliminar: ").strip().upper()
                    if codigo.strip() == "":
                        print("Error, el código no puede estar vacío o ser sólo espacios.")
                    else:
                        if eliminar_arreglo(arreglos, bodega, codigo):
                            print("Arreglo eliminado.")
                            break
                        else:
                            print("El código no existe.")
                            break
        case 6:
            print("Programa finalizado.")
            break