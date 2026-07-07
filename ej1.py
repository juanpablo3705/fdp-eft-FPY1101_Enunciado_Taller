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

# funcion opcion 1 unidades por tipo de arreglo:
def unidades_tipo(tipo, arreglos, bodega):
    while True:
        tipo = input("Ingrese tipo de arreglo (ramo, caja o centro): ").lower().strip()
        if tipo != "ramo" or tipo != "caja" or tipo != "centro":
            print("Error, debe ingresar un tipo de arreglo válido (ramo, caja o centro).")
        else:
            break
    



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
            print("1")
        case 2:
            print("2")
        case 3:
            print("3")
        case 4:
            print("4")
        case 5:
            print("5")
        case 6:
            print("Programa finalizado.")
            break