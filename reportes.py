# ==========================================
# MÓDULO: REPORTES
# ==========================================
# Este módulo permite generar reportes utilizando
# la información almacenada en las guías de envío.

# Se importa la lista de guías desde el módulo Guías.
from guias import guias


# ------------------------------------------
# TOTAL DE GUÍAS
# ------------------------------------------
def total_guias():

    # Muestra el título del reporte.
    print("\n========== REPORTE ==========")

    # len() devuelve la cantidad total
    # de guías registradas.
    print("Total de Guías Registradas:", len(guias))


# ------------------------------------------
# GUÍAS POR ESTADO
# ------------------------------------------
def guias_registradas():

    # Variable que almacenará la cantidad
    # de guías con estado REGISTRADA.
    contador = 0

    # Se recorren todas las guías registradas.
    for guia in guias:

        # Se verifica si el estado de la guía
        # es igual a REGISTRADA.
        if guia[9] == "REGISTRADA":

            # Se incrementa el contador.
            contador = contador + 1

    # Se muestra el resultado del reporte.
    print("\nGuías Registradas:", contador)


# ------------------------------------------
# BUSCAR GUÍAS POR CLIENTE
# ------------------------------------------
def buscar_por_cliente():

    # Se solicita el RUC del cliente.
    ruc = input("\nIngrese el RUC del cliente: ")

    # Variable bandera para verificar
    # si existen guías para ese cliente.
    encontrado = False

    # Se recorren todas las guías.
    for guia in guias:

        # Se compara el RUC ingresado
        # con el RUC almacenado en la guía.
        if guia[2] == ruc:

            print("--------------------------------")
            print("Guía:", guia[0])
            print("Cliente:", guia[3])
            print("Destino:", guia[6])
            print("Transportista:", guia[8])
            print("Estado:", guia[9])

            # Se encontró al menos una guía.
            encontrado = True

    # Si después del recorrido la variable
    # continúa en False, significa que
    # el cliente no tiene guías registradas.
    if encontrado == False:

        print("\nNo existen guías para ese cliente.")