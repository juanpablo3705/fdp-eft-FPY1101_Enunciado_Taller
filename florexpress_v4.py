# FlorExpress - Sistema de administración de catálogo y stock
# Evaluación Final Transversal - FPY1101

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

# funcion leer opción:
def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
            if (opcion >= 1) and (opcion <= 6):
                return opcion
            else:
                print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")

# funcion unidades por tipo (opción 1):
def unidades_tipo(tipo, arreglos, bodega):
    tipo = tipo.strip().lower() # así "RAMO" y "ramo" cuentan como lo mismo
    total_unidades = 0

    for codigo, datos_arreglo in arreglos.items():
        # datos_arreglo es la lista de ese arreglo, ej:
        # ['Ramo Primavera', 'ramo', 'rosado', 'M', True, 'primavera']
        # la posición 1 de esa lista es el "tipo".
        if datos_arreglo[1].lower() == tipo:
            # arreglos y bodega comparten el mismo código como clave, por
            # eso podemos ir directo a bodega[codigo] sin recorrerlo de nuevo
            total_unidades += bodega[codigo][1] # posición 1 = unidades

    print(f"El total de unidades disponibles es: {total_unidades}")

# funcion búsqueda por rango de precio (opción 2):
def busqueda_precio(precio_min, precio_max, arreglos, bodega):
    encontrados = []

    for codigo, datos_bodega in bodega.items():
        precio = datos_bodega[0]   # posición 0 = precio
        unidades = datos_bodega[1] # posición 1 = unidades

        if (precio >= precio_min) and (precio <= precio_max) and (unidades != 0):
            nombre_arreglo = arreglos[codigo][0]
            encontrados.append(f"{nombre_arreglo}--{codigo}")

    if len(encontrados) == 0:
        print("No hay arreglos en ese rango de precios.")
    else:
        encontrados.sort() # ordena alfabéticamente porque parte con el nombre
        print(f"Los arreglos encontrados son: {encontrados}")

# funcion buscar si el código existe (se reutiliza en opción 3 y 5, para no
# repetir la misma búsqueda tres veces):
def buscar_codigo(codigo, bodega):
    return codigo in bodega # True si la clave existe en el diccionario

# funcion actualizar precio (opción 3):
def actualizar_precio(codigo, nuevo_precio, bodega):
    if buscar_codigo(codigo, bodega):
        bodega[codigo][0] = nuevo_precio # posición 0 de la lista = precio
        return True
    else:
        return False

# ---------- validaciones para la opción 4 ----------
# el enunciado pide una función de validación por cada dato, y que ninguna
# de ellas imprima mensajes de error (solo retornan True o False, el mensaje
# se muestra después, en el programa principal).

def validar_codigo(codigo, arreglos):
    if codigo.strip() == "":
        return False
    elif codigo in arreglos:
        return False
    else:
        return True

def validar_texto(texto):
    # esta función se reutiliza para 4 datos distintos (nombre, tipo,
    # color_principal y temporada), porque los 4 comparten la misma regla
    # (no vacío ni solo espacios en blanco). como se usa para más de un
    # dato, el parámetro se llama de forma genérica "texto": no podría
    # llamarse igual que los 4 a la vez.
    if texto.strip() == "":
        return False
    else:
        return True

def validar_tamano(tamano):
    return (tamano == "S") or (tamano == "M") or (tamano == "L")

def validar_incluye_tarjeta(tarjeta_texto):
    return (tarjeta_texto == "s") or (tarjeta_texto == "n")

def validar_precio(precio):
    return precio > 0

def validar_unidades(unidades):
    return unidades >= 0

# funcion agregar arreglo (opción 4):
def agregar_arreglo(codigo, nombre, tipo, color_principal, tamano,
                     incluye_tarjeta, temporada, precio, unidades,
                     arreglos, bodega):
    if codigo in arreglos:
        return False

    # se agrega el mismo código en AMBOS diccionarios, cada uno con su
    # propia lista de datos (uno describe el arreglo, el otro lo administra)
    arreglos[codigo] = [nombre, tipo, color_principal, tamano,
                         incluye_tarjeta, temporada]
    bodega[codigo] = [precio, unidades]
    return True

# funcion eliminar arreglo (opción 5):
def eliminar_arreglo(codigo, arreglos, bodega):
    if buscar_codigo(codigo, bodega):
        del arreglos[codigo]
        del bodega[codigo]
        return True
    else:
        return False


# programa principal:
# los dos diccionarios se crean aquí (no dentro de una función) y se pasan
# como argumento a cada función que los necesita, tal como pide el
# enunciado (no está permitido usarlos como variables globales adentro).

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
    opcion_elegida = leer_opcion()

    match opcion_elegida:

        case 1:
            # la variable se llama igual que el parámetro de la función
            # (tipo), así queda claro de inmediato qué dato le estamos
            # pasando, sin tener que "traducir" nombres mentalmente.
            tipo = input("Ingrese tipo de arreglo a consultar: ")
            unidades_tipo(tipo, arreglos, bodega)

        case 2:
            # el enunciado pide que la validación de "son enteros" ocurra
            # aquí en el programa principal, antes de llamar a la función
            while True:
                try:
                    precio_min = int(input("Ingrese precio mínimo: "))
                    precio_max = int(input("Ingrese precio máximo: "))
                    if (precio_min < 0) or (precio_max < 0) or (precio_min > precio_max):
                        print("Debe ingresar valores enteros positivos, el mínimo "
                              "debe ser menor o igual al máximo")
                    else:
                        busqueda_precio(precio_min, precio_max, arreglos, bodega)
                        break
                except ValueError:
                    print("Debe ingresar valores enteros")

        case 3:
            while True:
                codigo = input("Ingrese código del arreglo: ").strip().upper()

                while True:
                    try:
                        nuevo_precio = int(input("Ingrese nuevo precio: "))
                        if nuevo_precio <= 0:
                            print("Debe ingresar un valor entero positivo")
                        else:
                            break
                    except ValueError:
                        print("Debe ingresar un valor entero positivo")

                if actualizar_precio(codigo, nuevo_precio, bodega):
                    print("Precio actualizado")
                else:
                    print("El código no existe")

                otro = input("¿Desea actualizar otro precio (s/n)?: ").strip().lower()
                if otro != "s":
                    break

        case 4:
            # se piden todos los datos primero, y recién después se valida
            # cada uno por separado, tal como pide el enunciado. cada
            # variable se llama igual que el parámetro que recibe en su
            # función correspondiente (codigo, nombre, tipo, etc.)
            codigo = input("Ingrese código del arreglo: ").strip().upper()
            nombre = input("Ingrese nombre: ")
            tipo = input("Ingrese tipo: ")
            color_principal = input("Ingrese color principal: ")
            tamano = input("Ingrese tamaño (S/M/L): ").strip().upper()
            tarjeta_texto = input("¿Incluye tarjeta? (s/n): ").strip().lower()
            temporada = input("Ingrese temporada: ")

            # precio y unidades se piden con su propio try/except, porque
            # deben ser convertidos a número antes de poder validarlos
            while True:
                try:
                    precio = int(input("Ingrese precio: "))
                    break
                except ValueError:
                    print("El precio debe ser un número entero")

            while True:
                try:
                    unidades = int(input("Ingrese unidades: "))
                    break
                except ValueError:
                    print("Las unidades deben ser un número entero")

            # if/elif encadenado: se detiene en la PRIMERA validación que
            # falle y muestra su mensaje específico; si todas pasan, cae
            # al else final y recién ahí se agrega el arreglo
            if not validar_codigo(codigo, arreglos):
                print("El código ya existe")
            elif not validar_texto(nombre):
                print("El nombre no puede estar vacío")
            elif not validar_texto(tipo):
                print("El tipo no puede estar vacío")
            elif not validar_texto(color_principal):
                print("El color principal no puede estar vacío")
            elif not validar_tamano(tamano):
                print("El tamaño debe ser 'S', 'M' o 'L'")
            elif not validar_incluye_tarjeta(tarjeta_texto):
                print("Debe responder 's' o 'n'")
            elif not validar_texto(temporada):
                print("La temporada no puede estar vacía")
            elif not validar_precio(precio):
                print("El precio debe ser mayor que cero")
            elif not validar_unidades(unidades):
                print("Las unidades deben ser mayores o iguales a cero")
            else:
                # recién aquí convertimos el "s"/"n" a booleano, porque ya
                # sabemos que tarjeta_texto pasó la validación
                incluye_tarjeta = (tarjeta_texto == "s")
                agregado = agregar_arreglo(codigo, nombre, tipo, color_principal,
                                            tamano, incluye_tarjeta, temporada,
                                            precio, unidades, arreglos, bodega)
                if agregado:
                    print("Arreglo agregado")
                else:
                    print("El código ya existe")

        case 5:
            codigo = input("Ingrese código del arreglo a eliminar: ").strip().upper()
            if eliminar_arreglo(codigo, arreglos, bodega):
                print("Arreglo eliminado")
            else:
                print("El código no existe")

        case 6:
            print("Programa finalizado.")
            break
