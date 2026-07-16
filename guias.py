# ==========================================
# MÓDULO: GUÍAS DE ENVÍO
# ==========================================
# Este módulo permite generar, consultar, listar
# y modificar las guías de envío. Para crear una guía
# primero se valida que existan el cliente,
# el destinatario y el transportista.

# Se importan funciones de otros módulos para reutilizar
# información ya registrada.
from clientes import obtener_cliente
from destinatarios import obtener_destinatario
from transportistas import obtener_transportista

# Lista donde se almacenarán todas las guías de envío.
# Cada guía contiene:
# [Número Guía, Pedido, RUC, Cliente, Destinatario,
# Dirección, Ciudad, Provincia, Transportista, Estado]
guias = []

# guias = [] crea una lista dinámica en memoria donde
# se almacenarán todas las guías generadas.


# ------------------------------------------
# GENERAR GUÍA
# ------------------------------------------
def generar_guia():

    print("\n========== GENERAR GUÍA ==========")

    # Se solicita el número único de la guía.
    numero_guia = input("Número de Guía: ")

    # Se solicita el número de pedido generado en Odoo.
    pedido = input("Número Pedido Odoo: ")

    # Se solicita el RUC del cliente.
    ruc = input("RUC del Cliente: ")

    # Se busca el cliente utilizando una función
    # del módulo Clientes.
    cliente = obtener_cliente(ruc)

    # Si la función devuelve None,
    # significa que el cliente no existe.
    if cliente == None:

        print("\nEl cliente no existe.")

        # return finaliza la función.
        return

    # Se obtiene el destinatario asociado al cliente.
    destinatario = obtener_destinatario(ruc)

    # Si no existe destinatario,
    # no es posible generar la guía.
    if destinatario == None:

        print("\nEl cliente no tiene destinatarios registrados.")

        return

    # Se muestran los datos recuperados.
    print("\nCliente encontrado")
    print("Razón Social:", cliente[1])

    print("\nDestinatario")
    print("Nombre:", destinatario[1])
    print("Dirección:", destinatario[2])
    print("Ciudad:", destinatario[3])
    print("Provincia:", destinatario[4])

    # Se solicita el nombre del transportista.
    nombre_transportista = input("\nTransportista: ")

    # Se busca el transportista registrado.
    transportista = obtener_transportista(nombre_transportista)

    # Si no existe, se cancela el proceso.
    if transportista == None:

        print("\nEl transportista no existe.")

        return

    # Estado inicial que tendrá toda guía nueva.
    estado = "REGISTRADA"

    # Se crea la lista con toda la información
    # necesaria para la guía.
    guia = [

        numero_guia,

        pedido,

        cliente[0],

        cliente[1],

        destinatario[1],

        destinatario[2],

        destinatario[3],

        destinatario[4],

        transportista[0],

        estado

    ]

    # append() agrega la nueva guía
    # al final de la lista.
    guias.append(guia)

    print("\n===================================")
    print(" GUÍA GENERADA CORRECTAMENTE")
    print("===================================")


# ------------------------------------------
# BUSCAR GUÍA
# ------------------------------------------
def buscar_guia():

    print("\n========== BUSCAR GUÍA ==========")

    # Se solicita el número de guía.
    numero = input("Número de Guía: ")

    # Variable bandera para saber si existe la guía.
    encontrado = False

    # Se recorren todas las guías registradas.
    for guia in guias:

        # Se compara el número ingresado
        # con el número almacenado.
        if guia[0] == numero:

            print("\n===================================")
            print(" GUÍA DE ENVÍO ")
            print("===================================")
            print("Número Guía:", guia[0])
            print("Pedido Odoo:", guia[1])
            print("RUC:", guia[2])
            print("Cliente:", guia[3])
            print("Destinatario:", guia[4])
            print("Dirección:", guia[5])
            print("Ciudad:", guia[6])
            print("Provincia:", guia[7])
            print("Transportista:", guia[8])
            print("Estado:", guia[9])
            print("===================================")

            # La guía fue encontrada.
            encontrado = True

    # Si no hubo coincidencias,
    # se informa al usuario.
    if encontrado == False:

        print("\nGuía no encontrada.")


# ------------------------------------------
# MOSTRAR GUÍAS
# ------------------------------------------
def mostrar_guias():

    print("\n========== HISTORIAL ==========")

    # len() devuelve la cantidad de guías registradas.
    if len(guias) == 0:

        print("No existen guías registradas.")

    else:

        # Contador utilizado para numerar cada guía.
        contador = 1

        # Se recorren todas las guías almacenadas.
        for guia in guias:

            print("--------------------------------")
            print("Registro:", contador)
            print("Guía:", guia[0])
            print("Pedido:", guia[1])
            print("Cliente:", guia[2])
            print("Transportista:", guia[8])
            print("Estado:", guia[9])

            # Incrementa el contador.
            contador = contador + 1


# ------------------------------------------
# MODIFICAR GUÍA
# ------------------------------------------
def modificar_guia():

    print("\n========== MODIFICAR GUÍA ==========")

    # Se solicita el número de guía a modificar.
    numero = input("Ingrese el número de guía: ")

    # Variable bandera para verificar
    # si la guía fue encontrada.
    encontrado = False

    # Se recorren todas las guías.
    for guia in guias:

        # Se compara el número ingresado
        # con el número almacenado.
        if guia[0] == numero:

            print("\nGuía encontrada")

            # Se muestra el estado actual.
            print("Estado actual:", guia[9])

            # Se solicita el nuevo estado.
            nuevo_estado = input("Nuevo estado: ")

            # Se reemplaza el estado anterior
            # por el nuevo valor ingresado.
            guia[9] = nuevo_estado

            print("\nEstado actualizado correctamente.")

            # La guía fue encontrada y modificada.
            encontrado = True

    # Si después del recorrido la variable
    # continúa en False, significa que
    # la guía no existe.
    if encontrado == False:

        print("\nLa guía no existe.")