
import os
import time
import msvcrt
from datetime import datetime


# ============================================================
# 1. CONFIGURACIÓN
# ============================================================

PRECIO_TORTILLA = 27.00
PRECIO_ARROZ = 35.00
PRECIO_SALSA = 21.00
PRECIO_FRIJOLES = 40.00

CARPETA = "documentos_tortilleria"

INVENTARIO_INICIAL = {
    "Arroz": 20,
    "Salsa": 15,
    "Frijoles": 25
}

inventario = INVENTARIO_INICIAL.copy()

cantidad_tickets = 0
dinero_ganado = 0.00

ventas_productos = {
    "Tortilla": 0,
    "Arroz": 0,
    "Salsa": 0,
    "Frijoles": 0
}


# ============================================================
# 2. ENTRADA DEL TECLADO Y TEMPORIZADOR
# ============================================================

def leer_opcion_con_tiempo(tiempo=600):
    """Lee la opción del menú y reinicia el temporizador con cada tecla."""

    print("\nSeleccione una opción: ", end="", flush=True)

    texto = ""
    inicio = time.time()

    while time.time() - inicio < tiempo:

        if msvcrt.kbhit():
            tecla = msvcrt.getwch()

            # Cada tecla presionada cuenta como actividad y reinicia el tiempo.
            inicio = time.time()

            if tecla in ("\r", "\n"):
                print()
                return texto, "accion"

            elif tecla == "\b":
                if texto:
                    texto = texto[:-1]
                    print("\b \b", end="", flush=True)

            elif tecla in ("\x00", "\xe0"):
                # Consume el segundo código de las teclas especiales.
                msvcrt.getwch()

            elif tecla.isprintable():
                texto += tecla
                print(tecla, end="", flush=True)

        time.sleep(0.05)

    print()
    return "", "inactivo"


def confirmar_continuar():
    """Pregunta si el usuario desea continuar después de diez minutos."""

    while True:
        respuesta = input(
            "¿Desea seguir utilizando el programa? (si/no): "
        ).strip().lower()

        if respuesta == "si":
            print("\nContinuando con el programa...")
            return True

        elif respuesta == "no":
            print("\nCerrando el sistema...")
            return False

        else:
            print("Respuesta inválida. Escriba si o no.")


# ============================================================
# 3. FECHA
# ============================================================

def solicitar_fecha():
    """Solicita y valida una fecha con formato DD/MM/AAAA."""

    while True:

        entrada = input(
            "Ingrese la fecha (DD/MM/AAAA): "
        ).strip()

        try:

            fecha = datetime.strptime(
                entrada,
                "%d/%m/%Y"
            )

            return fecha.day, fecha.month, fecha.year

        except ValueError:

            print(
                "Fecha incorrecta. Use el formato DD/MM/AAAA."
            )


def convertir_fecha(Fecha):
    """Convierte la fecha guardada en una tupla a texto."""

    dia, mes, anio = Fecha

    return f"{dia:02d}/{mes:02d}/{anio:04d}"


# ============================================================
# 4. PREPARAR DOCUMENTOS
# ============================================================

def preparar_documentos(Fecha):
    """Crea la carpeta y los cuatro documentos iniciales."""

    try:

        os.makedirs(CARPETA, exist_ok=True)

        fecha = convertir_fecha(Fecha)

        documentos = {

            "ventas.txt": (
                "REGISTRO DE VENTAS DE LA TORTILLERÍA\n"
                f"Documento iniciado: {fecha}\n\n"
            ),

            "inventario.txt": (
                "REGISTRO DEL INVENTARIO\n"
                f"Documento iniciado: {fecha}\n"
                "STOCK|Arroz|20\n"
                "STOCK|Salsa|15\n"
                "STOCK|Frijoles|25\n"
            ),

            "productos.txt": (
                "LISTA DE PRODUCTOS Y PRECIOS\n"
                f"Documento iniciado: {fecha}\n\n"
                "Tortilla: $27.00 por kilogramo\n"
                "Arroz: $35.00 por pieza\n"
                "Salsa: $21.00 por pieza\n"
                "Frijoles: $40.00 por pieza\n"
            ),

            "procedimientos.txt": (
                "PROCEDIMIENTOS DE LA TORTILLERÍA\n"
                f"Documento iniciado: {fecha}\n\n"
                "1. Registrar la venta.\n"
                "2. Seleccionar los productos.\n"
                "3. Calcular el total.\n"
                "4. Entregar el ticket.\n"
                "5. Actualizar el inventario.\n"
                "6. Registrar el reabastecimiento.\n"
            )
        }

        for nombre, contenido in documentos.items():

            ruta = os.path.join(CARPETA, nombre)

            if not os.path.exists(ruta):

                with open(ruta, "w", encoding="utf-8") as archivo:

                    archivo.write(contenido)

        print("\nDocumentos preparados correctamente.")

    except PermissionError:

        print("No hay permisos para crear los documentos.")

    except OSError as error:

        print("Error al preparar los documentos:", error)


# ============================================================
# 5. CARGAR INVENTARIO
# ============================================================

def cargar_inventario():
    """Recupera las últimas existencias guardadas en el archivo."""

    global inventario

    ruta = os.path.join(CARPETA, "inventario.txt")

    try:

        with open(ruta, "r", encoding="utf-8") as archivo:

            for linea in archivo:

                datos = linea.strip().split("|")

                if len(datos) == 3 and datos[0] == "STOCK":

                    producto = datos[1]

                    if producto in inventario:

                        try:

                            cantidad = int(datos[2])

                            if cantidad >= 0:

                                inventario[producto] = cantidad

                        except ValueError:

                            print("Se encontró una cantidad inválida.")

    except FileNotFoundError:

        print("No se encontró el archivo de inventario.")

    except PermissionError:

        print("No hay permisos para leer el inventario.")

    except OSError as error:

        print("Error al cargar el inventario:", error)


# ============================================================
# 6. GUARDAR INVENTARIO
# ============================================================

def guardar_inventario(Fecha, usuario):
    """Agrega un registro de las existencias actuales al archivo."""

    ruta = os.path.join(CARPETA, "inventario.txt")

    try:

        with open(ruta, "a", encoding="utf-8") as archivo:

            archivo.write("\nACTUALIZACIÓN DE INVENTARIO\n")
            archivo.write(f"Fecha: {convertir_fecha(Fecha)}\n")
            archivo.write(f"Usuario: {usuario}\n")

            for producto, cantidad in inventario.items():

                archivo.write(
                    f"{producto}: {cantidad} piezas disponibles\n"
                )

                archivo.write(
                    f"STOCK|{producto}|{cantidad}\n"
                )

        return True

    except PermissionError:

        print("No hay permisos para guardar el inventario.")

        return False

    except OSError as error:

        print("Error al guardar el inventario:", error)

        return False


# ============================================================
# 7. CARGAR HISTORIAL DE VENTAS
# ============================================================

def cargar_ventas():
    """Recupera el total de tickets, dinero y productos vendidos."""

    global cantidad_tickets
    global dinero_ganado
    global ventas_productos

    ruta = os.path.join(CARPETA, "ventas.txt")

    try:

        with open(ruta, "r", encoding="utf-8") as archivo:

            for linea in archivo:

                datos = linea.strip().split("|")

                if len(datos) == 5 and datos[0] == "VENTA":

                    try:

                        cantidad_tickets += 1
                        dinero_ganado += float(datos[4])

                    except ValueError:

                        print(
                            "Se encontró un registro de venta inválido."
                        )

                elif len(datos) == 6 and datos[0] == "PRODUCTO":

                    producto = datos[2]

                    if producto in ventas_productos:

                        try:

                            ventas_productos[producto] += float(datos[3])

                        except ValueError:

                            print(
                                "Se encontró una cantidad de venta inválida."
                            )

    except FileNotFoundError:

        print("No se encontró el historial de ventas.")

    except PermissionError:

        print("No hay permisos para leer las ventas.")

    except OSError as error:

        print("Error al cargar las ventas:", error)


# ============================================================
# 8. PANTALLA INICIAL
# ============================================================

def pantalla_inicial():
    """Solicita el nombre del usuario y muestra una bienvenida."""

    print("\n======================================")
    print("       SISTEMA DE LA TORTILLERÍA")
    print("======================================")

    while True:

        usuario = input(
            "Ingrese su nombre de usuario: "
        ).strip()

        if usuario:

            break

        print("El nombre no puede estar vacío.")

    usuario = usuario.title()

    print(
        f"\nBienvenido/a {usuario} al sistema de la tortillería."
    )

    return usuario


# ============================================================
# 9. CARGA DEL PROGRAMA
# ============================================================

def cargar_programa():
    """Muestra una animación de carga de tres segundos."""

    print("\nCargando sistema: ", end="", flush=True)

    for i in range(3):

        time.sleep(1)

        print("■", end="", flush=True)

    print("\nSistema listo.")


# ============================================================
# 10. REALIZAR VENTA
# ============================================================

def realizar_venta(usuario, caja, Fecha):
    """Registra una compra, calcula su total y actualiza existencias."""

    global cantidad_tickets
    global dinero_ganado
    global ventas_productos

    compra = []

    print("\n======================================")
    print("             NUEVA VENTA")
    print("======================================")

    print("\nSeleccione la cantidad de tortillas:")
    print("1. Medio kilo")
    print("2. Un kilo")
    print("3. Dos kilos")
    print("4. Tres kilos")
    print("5. Cuatro kilos")

    opciones_tortilla = {
        "1": 0.5,
        "2": 1,
        "3": 2,
        "4": 3,
        "5": 4
    }

    while True:

        opcion = input(
            "Seleccione una opción: "
        ).strip()

        if opcion in opciones_tortilla:

            kilos = opciones_tortilla[opcion]

            compra.append({
                "producto": "Tortilla",
                "cantidad": kilos,
                "unidad": "kg",
                "precio": PRECIO_TORTILLA,
                "subtotal": kilos * PRECIO_TORTILLA
            })

            break

        print("Opción inválida.")

    # Agregar productos adicionales

    while True:

        print("\n¿Desea agregar otro producto?")
        print("1. Arroz")
        print("2. Salsa")
        print("3. Frijoles")
        print("4. Terminar compra")

        opcion = input(
            "Seleccione una opción: "
        ).strip()

        if opcion == "4":

            break

        productos = {
            "1": ("Arroz", PRECIO_ARROZ),
            "2": ("Salsa", PRECIO_SALSA),
            "3": ("Frijoles", PRECIO_FRIJOLES)
        }

        if opcion not in productos:

            print("Opción inválida.")

            continue

        nombre, precio = productos[opcion]

        while True:

            try:

                cantidad = int(
                    input(
                        f"Cantidad de {nombre}: "
                    )
                )

                if cantidad <= 0:

                    print("La cantidad debe ser mayor a cero.")

                    continue

                if cantidad > inventario[nombre]:

                    print(
                        f"Inventario insuficiente. "
                        f"Disponibles: {inventario[nombre]} piezas."
                    )

                    continue

                break

            except ValueError:

                print("Ingrese un número entero válido.")

        compra.append({
            "producto": nombre,
            "cantidad": cantidad,
            "unidad": "pieza",
            "precio": precio,
            "subtotal": cantidad * precio
        })

    # Calcular el total

    total = 0

    for producto in compra:

        total += producto["subtotal"]

    # Mostrar ticket

    print("\n======================================")
    print("                 TICKET")
    print("======================================")
    print("Tortillería")
    print("Usuario:", usuario)
    print("Caja:", caja)
    print("Fecha:", convertir_fecha(Fecha))
    print("--------------------------------------")

    for producto in compra:

        print(
            f"{producto['producto']}: "
            f"{producto['cantidad']} {producto['unidad']} "
            f"x ${producto['precio']:.2f} "
            f"= ${producto['subtotal']:.2f}"
        )

    print("--------------------------------------")
    print(f"TOTAL: ${total:.2f}")
    print("======================================")

    # Guardar la venta antes de descontar el inventario

    ruta = os.path.join(CARPETA, "ventas.txt")

    try:

        with open(ruta, "a", encoding="utf-8") as archivo:

            archivo.write(
                f"VENTA|{convertir_fecha(Fecha)}|"
                f"{usuario}|{caja}|{total:.2f}\n"
            )

            for producto in compra:

                archivo.write(
                    f"PRODUCTO|{convertir_fecha(Fecha)}|"
                    f"{producto['producto']}|"
                    f"{producto['cantidad']}|"
                    f"{producto['unidad']}|"
                    f"{producto['subtotal']:.2f}\n"
                )

        # Descontar las existencias después de guardar la venta

        for producto in compra:

            nombre = producto["producto"]

            if nombre in inventario:

                inventario[nombre] -= producto["cantidad"]

            ventas_productos[nombre] += producto["cantidad"]

        cantidad_tickets += 1
        dinero_ganado += total

        guardar_inventario(Fecha, usuario)

        print("\nVenta registrada correctamente.")

    except PermissionError:

        print("No hay permisos para guardar la venta.")

    except OSError as error:

        print("Error al guardar la venta:", error)


# ============================================================
# 11. ADMINISTRAR INVENTARIO
# ============================================================

def administrar_inventario(usuario, Fecha):
    """Permite agregar, restablecer y consultar el inventario."""

    global inventario

    while True:

        print("\n======================================")
        print("         ADMINISTRAR INVENTARIO")
        print("======================================")
        print("1. Agregar existencias")
        print("2. Restablecer inventario")
        print("3. Consultar inventario")
        print("4. Regresar al menú")

        opcion = input(
            "\nSeleccione una opción: "
        ).strip()

        if opcion == "1":

            productos = list(inventario.keys())

            print("\nPRODUCTOS DISPONIBLES")

            for i, producto in enumerate(productos, start=1):

                print(
                    f"{i}. {producto}: "
                    f"{inventario[producto]} piezas"
                )

            try:

                seleccion = int(
                    input("\nSeleccione el producto: ")
                )

                if seleccion < 1 or seleccion > len(productos):

                    print("Producto inválido.")

                    continue

                nombre = productos[seleccion - 1]

                cantidad = int(
                    input(
                        f"¿Cuántas piezas de {nombre} desea agregar?: "
                    )
                )

                if cantidad <= 0:

                    print("La cantidad debe ser mayor a cero.")

                    continue

                inventario[nombre] += cantidad

                if guardar_inventario(Fecha, usuario):

                    print(
                        f"\nSe agregaron {cantidad} piezas de {nombre}."
                    )

                    print(
                        f"Existencias actuales: "
                        f"{inventario[nombre]} piezas."
                    )

            except ValueError:

                print("Ingrese un número entero válido.")

        elif opcion == "2":

            print("\nINVENTARIO ACTUAL")

            for producto, cantidad in inventario.items():

                print(f"{producto}: {cantidad} piezas")

            confirmacion = input(
                "\n¿Está seguro de restablecer el inventario? (si/no): "
            ).strip().lower()

            if confirmacion == "si":

                inventario = INVENTARIO_INICIAL.copy()

                if guardar_inventario(Fecha, usuario):

                    print(
                        "\nInventario restablecido correctamente."
                    )

                    for producto, cantidad in inventario.items():

                        print(f"{producto}: {cantidad} piezas")

            elif confirmacion == "no":

                print("Operación cancelada.")

            else:

                print("Respuesta inválida. Operación cancelada.")

        elif opcion == "3":

            print("\nINVENTARIO ACTUAL")

            for producto, cantidad in inventario.items():

                print(f"{producto}: {cantidad} piezas")

        elif opcion == "4":

            print("\nRegresando al menú principal...")

            break

        else:

            print("Opción inválida. Intente nuevamente.")


# ============================================================
# 12. LISTAR DOCUMENTOS
# ============================================================

def listar_documentos():
    """Muestra los archivos de texto disponibles."""

    try:

        documentos = []

        for nombre in os.listdir(CARPETA):

            if nombre.endswith(".txt"):

                documentos.append(nombre)

        documentos.sort()

        if not documentos:

            print("No hay documentos disponibles.")

            return []

        print("\nDOCUMENTOS DISPONIBLES")

        for i, nombre in enumerate(documentos, start=1):

            print(f"{i}. {nombre}")

        return documentos

    except FileNotFoundError:

        print("La carpeta no existe.")

        return []

    except PermissionError:

        print("No hay permisos para consultar los documentos.")

        return []

    except OSError as error:

        print("Error al listar documentos:", error)

        return []


# ============================================================
# 13. SELECCIONAR DOCUMENTO
# ============================================================

def seleccionar_documento():
    """Permite elegir un documento mediante su número."""

    documentos = listar_documentos()

    if not documentos:

        return None

    while True:

        opcion = input(
            "\nSeleccione el número del documento: "
        ).strip()

        try:

            numero = int(opcion)

            if 1 <= numero <= len(documentos):

                return documentos[numero - 1]

            print("Seleccione un número de la lista.")

        except ValueError:

            print("Ingrese un número válido.")


# ============================================================
# 14. LEER DOCUMENTO
# ============================================================

def leer_documento():
    """Abre y muestra el contenido del documento seleccionado."""

    nombre = seleccionar_documento()

    if nombre is None:

        return

    ruta = os.path.join(CARPETA, nombre)

    try:

        with open(ruta, "r", encoding="utf-8") as archivo:

            print("\n======================================")
            print("       CONTENIDO DEL DOCUMENTO")
            print("======================================")
            print(archivo.read())

    except FileNotFoundError:

        print("El documento ya no existe.")

    except PermissionError:

        print("No hay permisos para leer el documento.")

    except OSError as error:

        print("Error al leer el documento:", error)


# ============================================================
# 15. AGREGAR INFORMACIÓN A DOCUMENTOS
# ============================================================

def escribir_documento(usuario, Fecha):
    """Agrega información al final de un documento existente."""

    nombre = seleccionar_documento()

    if nombre is None:

        return

    ruta = os.path.join(CARPETA, nombre)

    try:

        contenido = input(
            "\nEscriba la información que desea agregar: "
        )

        if not contenido.strip():

            print("El contenido no puede estar vacío.")

            return

        with open(ruta, "a", encoding="utf-8") as archivo:

            archivo.write("\n")
            archivo.write(f"Fecha: {convertir_fecha(Fecha)}\n")
            archivo.write(f"Usuario: {usuario}\n")
            archivo.write(contenido + "\n")

        print("Información agregada correctamente.")

    except FileNotFoundError:

        print("El documento no existe.")

    except PermissionError:

        print("No hay permisos para modificar el documento.")

    except OSError as error:

        print("Error al modificar el documento:", error)


# ============================================================
# 16. CREAR DOCUMENTO
# ============================================================

def crear_documento(usuario, Fecha):
    """Crea un nuevo archivo de texto sin reemplazar los existentes."""

    print("\n======================================")
    print("           CREAR DOCUMENTO")
    print("======================================")

    nombre = input(
        "Ingrese el nombre del documento: "
    ).strip()

    if not nombre:

        print("El nombre no puede estar vacío.")

        return

    if os.path.basename(nombre) != nombre:

        print("Ingrese solamente el nombre del documento.")

        return

    if not nombre.endswith(".txt"):

        nombre += ".txt"

    ruta = os.path.join(CARPETA, nombre)

    try:

        contenido = input(
            "Ingrese el contenido inicial: "
        )

        with open(ruta, "x", encoding="utf-8") as archivo:

            archivo.write("DOCUMENTO DE LA TORTILLERÍA\n")
            archivo.write(f"Creado por: {usuario}\n")
            archivo.write(f"Fecha: {convertir_fecha(Fecha)}\n")
            archivo.write("--------------------------------------\n")
            archivo.write(contenido + "\n")

        print("Documento creado correctamente.")

    except FileExistsError:

        print("Ese documento ya existe.")

    except PermissionError:

        print("No hay permisos para crear el documento.")

    except OSError as error:

        print("Error al crear el documento:", error)


# ============================================================
# 17. MENÚ PRINCIPAL CON TEMPORIZADOR
# ============================================================

def mostrar_menu(usuario, caja, Fecha):
    """Muestra el menú y controla diez minutos de inactividad."""

    menu = [
        ["1", "Iniciar nueva venta"],
        ["2", "Leer documentos"],
        ["3", "Agregar información a documentos"],
        ["4", "Crear documentos nuevos"],
        ["5", "Administrar inventario"],
        ["6", "Cambiar de usuario"],
        ["7", "Cerrar caja y salir"]
    ]

    while True:

        print("\n======================================")
        print("             MENÚ PRINCIPAL")
        print("======================================")

        for elemento in menu:

            print(elemento[0] + ". " + elemento[1])

        # Espera una respuesta durante diez minutos.
        # Cada vez que regresa al menú, el tiempo comienza nuevamente.

        opcion, estado = leer_opcion_con_tiempo(600)

        opcion = opcion.strip()

        if estado == "inactivo":

            if confirmar_continuar():
                continue
            else:
                return "salir"

        # Cada opción tiene una acción independiente.

        elif opcion == "1":

            print("\nHas seleccionado: NUEVA VENTA")

            realizar_venta(usuario, caja, Fecha)

        elif opcion == "2":

            print("\nHas seleccionado: LEER DOCUMENTOS")

            leer_documento()

        elif opcion == "3":

            print("\nHas seleccionado: AGREGAR INFORMACIÓN")

            escribir_documento(usuario, Fecha)

        elif opcion == "4":

            print("\nHas seleccionado: CREAR DOCUMENTO")

            crear_documento(usuario, Fecha)

        elif opcion == "5":

            print("\nHas seleccionado: ADMINISTRAR INVENTARIO")

            administrar_inventario(usuario, Fecha)

        elif opcion == "6":

            print("\nHas seleccionado: CAMBIAR DE USUARIO")

            return "cambiar"

        elif opcion == "7":

            print("\nHas seleccionado: CERRAR CAJA")

            return "salir"

        else:

            print("Opción inválida. Intente nuevamente.")


# ============================================================
# 18. RESUMEN DE PRODUCTOS
# ============================================================

def resumen_productos():
    """Muestra las cantidades vendidas de cada producto."""

    print("\n======================================")
    print("        RESUMEN DE PRODUCTOS")
    print("======================================")

    for producto, cantidad in ventas_productos.items():

        print(f"{producto}: {cantidad:g} vendidos")

    if all(
        cantidad == 0
        for cantidad in ventas_productos.values()
    ):

        print("\nTodavía no hay productos vendidos.")

        return

    producto_mas = max(
        ventas_productos,
        key=ventas_productos.get
    )

    productos_vendidos = {
        producto: cantidad
        for producto, cantidad in ventas_productos.items()
        if cantidad > 0
    }

    producto_menos = min(
        productos_vendidos,
        key=productos_vendidos.get
    )

    print("\nProducto más vendido:")

    print(
        f"{producto_mas}: "
        f"{ventas_productos[producto_mas]:g}"
    )

    print("\nProducto menos vendido:")

    print(
        f"{producto_menos}: "
        f"{ventas_productos[producto_menos]:g}"
    )


# ============================================================
# 19. CIERRE DE CAJA
# ============================================================

def cierre_caja(caja):
    """Muestra el dinero recaudado, los tickets y el inventario final."""

    print("\n======================================")
    print("              CIERRE DE CAJA")
    print("======================================")

    print("Número de caja:", caja)
    print("Tickets registrados:", cantidad_tickets)

    print(f"Dinero recaudado: ${dinero_ganado:.2f}")

    print("\nINVENTARIO FINAL")

    for producto, cantidad in inventario.items():

        print(f"{producto}: {cantidad} piezas")

    resumen_productos()

    print("\nGracias por utilizar el sistema.")

    print("======================================")


# ============================================================
# 20. FUNCIÓN PRINCIPAL
# ============================================================

def main():
    """Inicia el sistema, carga los datos y controla el menú."""

    global cantidad_tickets
    global dinero_ganado
    global ventas_productos

    usuario = pantalla_inicial()

    Fecha = solicitar_fecha()

    preparar_documentos(Fecha)

    cargar_inventario()

    cargar_ventas()

    cargar_programa()

    while True:

        try:

            caja = int(
                input("\nIngrese el número de caja: ")
            )

            if caja > 0:

                break

            print("El número de caja debe ser mayor a cero.")

        except ValueError:

            print("Ingrese un número entero válido.")

    while True:

        resultado = mostrar_menu(
            usuario,
            caja,
            Fecha
        )

        if resultado == "cambiar" or resultado == "inicio":

            print("\nRegresando a la pantalla inicial...")

            usuario = pantalla_inicial()

            Fecha = solicitar_fecha()

        elif resultado == "salir":

            cierre_caja(caja)

            break


# ============================================================
# 21. EJECUTAR PROGRAMA
# ============================================================
if __name__ == "__main__":
    main()
