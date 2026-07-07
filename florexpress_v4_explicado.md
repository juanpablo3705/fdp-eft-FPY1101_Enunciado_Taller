# FlorExpress explicado línea por línea

Esta guía recorre `florexpress_v4.py` de arriba hacia abajo, como si estuviéramos
revisando el código juntos en una clase. La idea no es memorizar, sino entender
el "por qué" de cada decisión.

---

## Encabezado

```python
# FlorExpress - Sistema de administración de catálogo y stock
# Evaluación Final Transversal - FPY1101
```

Son comentarios, no código. Python los ignora por completo al ejecutar el
programa; están ahí solo para que cualquier persona (incluido tú, en el
futuro) sepa de qué trata el archivo con solo abrirlo.

---

## `mostrar_menu()`

```python
def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por tipo de arreglo")
    ...
    print("=====================================")
```

`def mostrar_menu():` crea una función llamada `mostrar_menu`. Los paréntesis
están vacíos porque esta función **no necesita ningún dato de afuera** para
hacer su trabajo: solo tiene que imprimir siempre el mismo texto. Por eso no
recibe parámetros ni tampoco usa `return`: su único trabajo es mostrar cosas
en pantalla, no calcular ni entregar un valor a quien la llamó.

Cada línea `print(...)` muestra una línea de texto. No hay ninguna lógica
aquí, es puro texto — pero se separó en una función aparte para no repetir
estas 8 líneas cada vez que el programa vuelve a mostrar el menú.

---

## `leer_opcion()`

```python
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
```

- `while True:` arma un ciclo que **no tiene condición de salida propia** — se
  repite para siempre, a menos que algo dentro de él use `return` o `break`.
  Se usa `while` y no `for` porque no sabemos de antemano cuántas veces el
  usuario se va a equivocar antes de escribir algo válido: puede ser 0 veces
  o puede ser 20.

- `try:` abre un bloque "riesgoso": todo lo que está adentro se intenta
  ejecutar, pero si algo falla, Python no hace explotar el programa, sino que
  salta directo al `except` correspondiente.

- `opcion = int(input("Ingrese una opción: "))`: primero `input(...)` muestra
  el texto y espera que el usuario escriba algo, devolviendo siempre un
  **string** (texto), aunque el usuario haya escrito números. Luego
  `int(...)` intenta convertir ese texto a un número entero. Si el usuario
  escribió `"3"`, se convierte sin problema. Si escribió `"hola"`, `int()`
  no puede convertirlo y lanza un error de tipo `ValueError`.

- `if (opcion >= 1) and (opcion <= 6):` — si la conversión funcionó, revisamos
  que el número esté dentro del rango válido del menú (1 a 6). El `and`
  exige que **ambas** condiciones se cumplan a la vez.

- `return opcion`: si todo salió bien, la función termina aquí mismo y le
  entrega ese número de vuelta a quien la llamó (en este caso, al programa
  principal). `return` corta la ejecución de la función inmediatamente — las
  líneas de abajo ni siquiera se llegan a ejecutar.

- `else: print(...)`: si el número no está entre 1 y 6 (por ejemplo el
  usuario escribió `9`), avisamos el error. Como no hay `return` aquí, la
  función no termina: el `while True` de más arriba hace que se vuelva a
  intentar desde el principio.

- `except ValueError: print(...)`: este bloque solo se ejecuta si `int(...)`
  falló (el usuario escribió algo que no es un número). Igual que el `else`
  de arriba, no hay `return`, así que el ciclo se repite y se vuelve a pedir
  el dato.

**Idea clave**: esta función nunca termina hasta que el `return opcion` se
ejecuta con éxito. Es un patrón muy típico para "pedir un dato hasta que sea
válido".

---

## `unidades_tipo(tipo, arreglos, bodega)` — Opción 1

```python
def unidades_tipo(tipo, arreglos, bodega):
    tipo = tipo.strip().lower()
    total_unidades = 0
```

- `def unidades_tipo(tipo, arreglos, bodega):` esta función sí necesita datos
  de afuera: el tipo de arreglo a buscar (`tipo`), y los dos diccionarios que
  contienen toda la información (`arreglos`, `bodega`). Recuerda: estos
  nombres (`tipo`, `arreglos`, `bodega`) solo existen **dentro** de esta
  función; son como cajones vacíos que se llenan con lo que sea que le
  pasemos cuando la llamemos.

- `tipo = tipo.strip().lower()`: aquí reasignamos la variable `tipo`,
  reemplazándola por una versión "limpia" de sí misma.
  - `.strip()` quita espacios en blanco sobrantes al principio y al final
    (por si el usuario escribió `" ramo "` con espacios de más).
  - `.lower()` convierte todo el texto a minúsculas.
  - Esto es importante porque el enunciado exige que "ramo" y "RAMO" se
    traten como el mismo tipo — sin esta línea, la comparación de más abajo
    fallaría si el usuario escribe en mayúsculas.

- `total_unidades = 0`: creamos una variable "acumuladora" que va a ir
  sumando unidades a medida que encontremos arreglos que coincidan. Empieza
  en 0 porque todavía no hemos contado nada.

```python
    for codigo, datos_arreglo in arreglos.items():
        if datos_arreglo[1].lower() == tipo:
            total_unidades += bodega[codigo][1]
```

- `for codigo, datos_arreglo in arreglos.items():` — recorremos **todo** el
  diccionario `arreglos`. `.items()` entrega, en cada vuelta, una pareja
  (clave, valor): `codigo` toma el valor de la clave (ej. `'FLO1'`), y
  `datos_arreglo` toma el valor asociado, que es una lista (ej.
  `['Ramo Primavera', 'ramo', 'rosado', 'M', True, 'primavera']`).
  Usamos `for` porque el número de vueltas es fijo: una por cada arreglo que
  exista en el diccionario, ni una más ni una menos.

- `datos_arreglo[1]`: como `datos_arreglo` es una lista, se accede a sus
  elementos por posición, empezando desde 0. La posición 1 (la segunda)
  guarda el "tipo" del arreglo, según el orden que define el enunciado:
  `[nombre, tipo, color_principal, tamaño, incluye_tarjeta, temporada]`.

- `if datos_arreglo[1].lower() == tipo:` comparamos el tipo de este arreglo
  (convertido también a minúsculas) contra el `tipo` que buscamos. Si
  coinciden, entramos al `if`.

- `total_unidades += bodega[codigo][1]`: si el tipo coincide, buscamos ese
  mismo `codigo` en el diccionario `bodega` (recuerda que ambos diccionarios
  usan el mismo código como clave, así que no hace falta recorrer `bodega`
  con otro `for`, basta con `bodega[codigo]`). La posición 1 de esa lista es
  `unidades` (`[precio, unidades]`). `+=` es una forma corta de escribir
  `total_unidades = total_unidades + bodega[codigo][1]`: le suma ese valor
  al acumulador.

```python
    print(f"El total de unidades disponibles es: {total_unidades}")
```

- Terminado el `for`, ya recorrimos todos los arreglos posibles, así que
  imprimimos el resultado final. El `f""` antes de las comillas es un
  **f-string**: permite insertar el valor de una variable directamente
  dentro del texto, escribiéndola entre llaves `{}`.

- Nota que esta función **no tiene `return`**: el enunciado pide justamente
  que no retorne nada y que muestre el resultado directamente por pantalla.

---

## `busqueda_precio(precio_min, precio_max, arreglos, bodega)` — Opción 2

```python
def busqueda_precio(precio_min, precio_max, arreglos, bodega):
    encontrados = []
```

- Creamos una lista vacía. La vamos a ir llenando con los arreglos que
  cumplan las condiciones del enunciado.

```python
    for codigo, datos_bodega in bodega.items():
        precio = datos_bodega[0]
        unidades = datos_bodega[1]

        if (precio >= precio_min) and (precio <= precio_max) and (unidades != 0):
            nombre_arreglo = arreglos[codigo][0]
            encontrados.append(f"{nombre_arreglo}--{codigo}")
```

- Esta vez recorremos `bodega`, no `arreglos`, porque las condiciones que
  necesitamos revisar (precio y unidades) viven ahí.

- `precio = datos_bodega[0]` y `unidades = datos_bodega[1]`: le ponemos
  nombre a cada posición de la lista para que el código sea más legible que
  escribir `datos_bodega[0]` y `datos_bodega[1]` una y otra vez.

- La condición combina tres cosas con `and`: el precio debe estar dentro del
  rango **y además** tener unidades distintas de cero. Si cualquiera de las
  tres falla, el arreglo no se agrega a la lista.

- `arreglos[codigo][0]`: si pasó la condición, vamos al diccionario
  `arreglos` con ese mismo código, y tomamos la posición 0 (el nombre).

- `encontrados.append(...)`: `.append()` agrega un elemento al final de una
  lista. Aquí agregamos un string armado con el formato que pide el
  enunciado: `"Nombre--Código"`.

```python
    if len(encontrados) == 0:
        print("No hay arreglos en ese rango de precios.")
    else:
        encontrados.sort()
        print(f"Los arreglos encontrados son: {encontrados}")
```

- `len(encontrados)` cuenta cuántos elementos tiene la lista. Si es 0,
  significa que ningún arreglo cumplió las condiciones.

- `encontrados.sort()`: ordena la lista alfabéticamente. Como cada elemento
  empieza con el nombre del arreglo (ej. `"Ramo Primavera--FLO1"`), ordenar
  la lista completa equivale a ordenar por nombre, que es justo lo que pide
  el enunciado.

- El `print` final muestra la lista completa. Al imprimir una lista
  directamente dentro de un f-string, Python la muestra con el formato
  `['elemento1', 'elemento2', ...]`, que coincide con el ejemplo del
  enunciado.

---

## `buscar_codigo(codigo, bodega)`

```python
def buscar_codigo(codigo, bodega):
    return codigo in bodega
```

- El operador `in` revisa si `codigo` es una de las claves del diccionario
  `bodega`, y entrega directamente `True` o `False`. Por eso podemos
  escribir `return codigo in bodega` en una sola línea: no hace falta un
  `if/else` porque `in` ya nos da un booleano listo para retornar.

- Esta función se reutiliza dentro de `actualizar_precio` y
  `eliminar_arreglo`, para no repetir esta misma búsqueda tres veces en el
  código.

---

## `actualizar_precio(codigo, nuevo_precio, bodega)` — Opción 3

```python
def actualizar_precio(codigo, nuevo_precio, bodega):
    if buscar_codigo(codigo, bodega):
        bodega[codigo][0] = nuevo_precio
        return True
    else:
        return False
```

- Primero preguntamos si el código existe, reutilizando `buscar_codigo`.

- `bodega[codigo][0] = nuevo_precio`: si existe, vamos a la lista de ese
  código en `bodega` y **reemplazamos** el valor en la posición 0 (el
  precio) por el nuevo valor. Esto modifica el diccionario directamente,
  no crea uno nuevo.

- `return True` / `return False`: la función no imprime ningún mensaje ella
  misma. Solo informa, con un valor booleano, si la operación funcionó o no.
  El mensaje ("Precio actualizado" / "El código no existe") se decide
  después, en el programa principal, según lo que esta función retorne —
  así lo pide el enunciado.

---

## Funciones de validación (para la Opción 4)

El enunciado exige una función independiente por cada dato, y que **ninguna**
imprima mensajes de error: solo deben retornar `True` o `False`.

```python
def validar_codigo(codigo, arreglos):
    if codigo.strip() == "":
        return False
    elif codigo in arreglos:
        return False
    else:
        return True
```

- Un código es inválido si está vacío (`codigo.strip() == ""`) **o** si ya
  existe en el diccionario `arreglos`. Se usa `elif` en vez de dos `if`
  separados porque, en cuanto una condición se cumple, ya sabemos que el
  resultado es `False` y no necesitamos seguir revisando.

```python
def validar_texto(texto):
    if texto.strip() == "":
        return False
    else:
        return True
```

- Esta función se reutiliza para 4 datos distintos: nombre, tipo,
  color_principal y temporada, porque los 4 comparten exactamente la misma
  regla ("no vacío ni solo espacios"). Por eso el parámetro se llama de
  forma genérica `texto`: no podría llamarse igual que los 4 datos a la vez.

```python
def validar_tamano(tamano):
    return (tamano == "S") or (tamano == "M") or (tamano == "L")
```

- Acá no hace falta `if/else` porque la expresión con `or` **ya es** un
  booleano por sí sola: si `tamano` es igual a cualquiera de las tres
  letras, el resultado ya es `True`; si no es ninguna, es `False`. Escribir
  `if (condición): return True else: return False` sería más largo sin
  aportar nada distinto.

```python
def validar_incluye_tarjeta(tarjeta_texto):
    return (tarjeta_texto == "s") or (tarjeta_texto == "n")

def validar_precio(precio):
    return precio > 0

def validar_unidades(unidades):
    return unidades >= 0
```

- Mismo principio: son comparaciones que ya retornan `True`/`False` por sí
  solas, así que no necesitan un `if` para "traducir" el resultado.

---

## `agregar_arreglo(...)` — Opción 4

```python
def agregar_arreglo(codigo, nombre, tipo, color_principal, tamano,
                     incluye_tarjeta, temporada, precio, unidades,
                     arreglos, bodega):
    if codigo in arreglos:
        return False

    arreglos[codigo] = [nombre, tipo, color_principal, tamano,
                         incluye_tarjeta, temporada]
    bodega[codigo] = [precio, unidades]
    return True
```

- Esta función recibe **9 datos del arreglo** más los dos diccionarios. El
  orden y los nombres de estos 9 parámetros no son arbitrarios: son
  exactamente los que exige el enunciado del PDF, para que el programa
  principal pueda llamarla tal cual está especificado.

- `if codigo in arreglos: return False`: aunque en el programa principal ya
  validamos que el código no existiera (con `validar_codigo`), esta función
  vuelve a comprobarlo como respaldo. Si en verdad ya existiera, corta acá
  con `return False` y las líneas de abajo ni se ejecutan.

- `arreglos[codigo] = [...]`: esto **crea una nueva entrada** en el
  diccionario `arreglos`, usando `codigo` como clave nueva y una lista con
  los 6 datos descriptivos como valor.

- `bodega[codigo] = [precio, unidades]`: lo mismo, pero en el otro
  diccionario, con los 2 datos operativos.

- `return True`: si llegamos hasta acá, todo salió bien.

---

## `eliminar_arreglo(codigo, arreglos, bodega)` — Opción 5

```python
def eliminar_arreglo(codigo, arreglos, bodega):
    if buscar_codigo(codigo, bodega):
        del arreglos[codigo]
        del bodega[codigo]
        return True
    else:
        return False
```

- Reutilizamos `buscar_codigo` de nuevo.

- `del arreglos[codigo]` y `del bodega[codigo]`: `del` elimina por completo
  una clave (y su valor) de un diccionario. Hay que borrar el mismo código
  en **ambos** diccionarios, porque representan al mismo arreglo desde dos
  puntos de vista distintos (uno describe, el otro administra el stock).

---

## Programa principal

```python
arreglos = { ... }
bodega = { ... }
```

- Acá se crean los dos diccionarios con los datos iniciales que da el
  enunciado. Se crean **aquí**, fuera de cualquier función, y por eso deben
  pasarse como argumento a cada función que los necesite — ninguna función
  puede "ver" estas variables directamente si no se las entregamos.

```python
while True:
    mostrar_menu()
    opcion_elegida = leer_opcion()
```

- El ciclo principal del programa: se repite para siempre (no tiene
  condición propia de salida) hasta que algo de adentro use `break`.

- En cada vuelta: se muestra el menú, y se pide y valida una opción
  (`leer_opcion` ya se encarga de que `opcion_elegida` sea un número entre
  1 y 6, nunca otra cosa).

```python
    match opcion_elegida:

        case 1:
            tipo = input("Ingrese tipo de arreglo a consultar: ")
            unidades_tipo(tipo, arreglos, bodega)
```

- `match opcion_elegida:` es como una versión más ordenada de escribir
  varios `if opcion_elegida == 1: ... elif opcion_elegida == 2: ...`. Cada
  `case número:` es una de esas ramas.

- Dentro del `case 1`, pedimos el dato que la función necesita
  (`input(...)`) y se lo pasamos. Fíjate que la variable se llama `tipo`,
  igual que el parámetro de `unidades_tipo` — así queda clarísimo qué dato
  estamos entregando, sin tener que "traducir" nombres en la cabeza.

```python
        case 2:
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
```

- Igual que en `leer_opcion`, usamos `while True` + `try/except` porque no
  sabemos cuántas veces el usuario se equivocará antes de ingresar dos
  números válidos.

- El enunciado pide que esta validación (que sean enteros) ocurra **aquí**,
  en el programa principal, antes de llamar a la función — a diferencia de,
  por ejemplo, `validar_precio`, que valida adentro de su propia función.
  Por eso el `try/except` está en este nivel y no dentro de
  `busqueda_precio`.

- Si los números son válidos, llamamos a la función y luego `break`: esto
  corta el `while True` de esta opción (no el del programa completo), y
  volvemos al menú principal.

```python
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
```

- Hay **dos** `while True` anidados (uno dentro de otro): el de afuera
  controla si el usuario quiere seguir actualizando precios; el de adentro
  solo se encarga de validar que el nuevo precio sea un entero positivo.

- `.strip().upper()`: quita espacios y convierte a mayúsculas, para que
  `"flo1"` y `"FLO1"` se traten como el mismo código.

- Una vez que tenemos `codigo` y `nuevo_precio` válidos, llamamos a
  `actualizar_precio` y decidimos qué imprimir **solo según lo que ella
  retorne** (`True` o `False`) — el enunciado es explícito en que esta
  decisión debe tomarse en el programa principal, no dentro de la función.

- Al final, preguntamos si quiere actualizar otro precio. Si la respuesta no
  es `"s"`, `break` corta el ciclo de afuera y volvemos al menú.

```python
        case 4:
            codigo = input("Ingrese código del arreglo: ").strip().upper()
            nombre = input("Ingrese nombre: ")
            tipo = input("Ingrese tipo: ")
            color_principal = input("Ingrese color principal: ")
            tamano = input("Ingrese tamaño (S/M/L): ").strip().upper()
            tarjeta_texto = input("¿Incluye tarjeta? (s/n): ").strip().lower()
            temporada = input("Ingrese temporada: ")
```

- Se piden **todos** los datos de texto primero, tal como pide el
  enunciado: "todos los datos se solicitan, y luego se validan de forma
  independiente". Nota que cada variable se llama igual que el parámetro que
  recibirá más adelante (`codigo`, `nombre`, `tipo`...).

```python
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
```

- `precio` y `unidades` necesitan ser convertidos a número antes de poder
  aplicarles `validar_precio`/`validar_unidades` (que comparan con `> 0` o
  `>= 0`, algo que no se puede hacer directamente sobre un texto). Por eso
  tienen su propio `try/except` aquí, distinto al de los datos de texto.

```python
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
```

- Este es un `if/elif` largo, y la clave para entenderlo es que **se
  detiene en la primera condición que sea verdadera**. `not validar_codigo(...)`
  se lee como "si NO es válido según `validar_codigo`". Si el código ya
  existe, esa primera condición ya es `True`, se imprime su mensaje, y
  Python **ni siquiera revisa** las líneas de `elif` que vienen después.

- Solo si las 9 validaciones son `False` en su respectivo `not` (es decir,
  todas pasaron), caemos al `else` final.

```python
            else:
                incluye_tarjeta = (tarjeta_texto == "s")
                agregado = agregar_arreglo(codigo, nombre, tipo, color_principal,
                                            tamano, incluye_tarjeta, temporada,
                                            precio, unidades, arreglos, bodega)
                if agregado:
                    print("Arreglo agregado")
                else:
                    print("El código ya existe")
```

- `incluye_tarjeta = (tarjeta_texto == "s")`: recién aquí convertimos el
  texto `"s"`/`"n"` a un valor booleano real (`True`/`False`), porque ya
  sabemos que pasó la validación. Antes de este punto, `tarjeta_texto`
  seguía siendo el string que escribió el usuario.

- Llamamos a `agregar_arreglo` con los 9 datos ya validados y los dos
  diccionarios, y guardamos lo que retorna en `agregado`.

- Igual que en las otras opciones, el mensaje final ("Arreglo agregado" /
  "El código ya existe") se decide en base al valor booleano que retornó la
  función, no dentro de ella.

```python
        case 5:
            codigo = input("Ingrese código del arreglo a eliminar: ").strip().upper()
            if eliminar_arreglo(codigo, arreglos, bodega):
                print("Arreglo eliminado")
            else:
                print("El código no existe")
```

- Más simple que las anteriores: se pide el código, se llama a la función,
  y el mensaje depende del `True`/`False` que retorne.

```python
        case 6:
            print("Programa finalizado.")
            break
```

- El `break` aquí corta el `while True` **del programa principal** (el más
  externo de todos), terminando la ejecución del programa.

---