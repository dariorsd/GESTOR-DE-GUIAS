# ==========================================
# MÓDULO: DESTINATARIOS
# ==========================================
# Este módulo administra los destinatarios de cada cliente.
# La información registrada será utilizada posteriormente
# para generar las guías de envío.

# Lista donde se almacenan todos los destinatarios.
# Cada registro contiene:
# [RUC Cliente, Nombre, Dirección, Ciudad, Provincia, Teléfono]
destinatarios = []

# destinatarios = [] crea una lista dinámica en memoria
# donde se almacenarán todos los destinatarios registrados.


# ------------------------------------------
# REGISTRAR DESTINATARIO
# ------------------------------------------
def registrar_destinatario():

    print("\n===== REGISTRAR DESTINATARIO =====")

    # Se solicita el RUC del cliente para relacionar
    # el destinatario con el cliente correspondiente.
    ruc_cliente = input("RUC del Cliente: ")

    # Se solicitan los datos del destinatario.
    nombre = input("Nombre del Destinatario: ")
    direccion = input("Dirección: ")
    ciudad = input("Ciudad: ")
    provincia = input("Provincia: ")
    telefono = input("Teléfono: ")

    # Se crea una lista con toda la información ingresada.
    destinatario = [
        ruc_cliente,
        nombre,
        direccion,
        ciudad,
        provincia,
        telefono
    ]

    # append() agrega el nuevo destinatario
    # al final de la lista.
    destinatarios.append(destinatario)

    # Se imprime la lista únicamente para verificar
    # que el registro fue almacenado correctamente.
    #print(destinatarios)

    print("\nDestinatario registrado correctamente.")


# ------------------------------------------
# BUSCAR DESTINATARIO
# ------------------------------------------
def buscar_destinatario():

    # Muestra todos los registros.
    # Solo se utiliza durante las pruebas.
    #print(destinatarios)

    print("\n===== BUSCAR DESTINATARIO =====")

    # strip() elimina espacios en blanco al inicio y al final.
    ruc = input("Ingrese el RUC del cliente: ").strip()

    # Variable bandera para saber si se encontró información.
    encontrado = False

    # for recorre todos los destinatarios registrados.
    for destinatario in destinatarios:

        # Mensajes utilizados para comprobar la comparación.
        print("RUC guardado:", destinatario[0])
        print("RUC buscado:", ruc)

        # Se compara el RUC almacenado con el RUC ingresado.
        if destinatario[0].strip() == ruc:

            print("--------------------------------")
            print("Cliente:", destinatario[0])
            print("Destinatario:", destinatario[1])
            print("Dirección:", destinatario[2])
            print("Ciudad:", destinatario[3])
            print("Provincia:", destinatario[4])
            print("Teléfono:", destinatario[5])

            # Si existe coincidencia,
            # la variable cambia a True.
            encontrado = True

    # Si después del recorrido la variable continúa
    # en False significa que no hubo coincidencias.
    if encontrado == False:

        print("\nNo existen destinatarios registrados.")


# ------------------------------------------
# MOSTRAR DESTINATARIOS
# ------------------------------------------
def mostrar_destinatarios():

    print("\n===== LISTA DESTINATARIOS =====")

    # len() devuelve la cantidad de registros almacenados.
    if len(destinatarios) == 0:

        print("No existen destinatarios.")

    else:

        # Contador utilizado para numerar cada registro.
        contador = 1

        # Se recorren todos los destinatarios.
        for destinatario in destinatarios:

            print("--------------------------------")
            print("Registro:", contador)
            print("Cliente:", destinatario[0])
            print("Destinatario:", destinatario[1])
            print("Ciudad:", destinatario[3])

            # Se incrementa el contador en una unidad.
            contador = contador + 1


# ------------------------------------------
# OBTENER DESTINATARIO
# ------------------------------------------
def obtener_destinatario(ruc_buscar):

    # Esta función es utilizada por el módulo Guías.
    # Recibe un RUC y devuelve el destinatario asociado.

    # Se recorren todos los registros.
    for destinatario in destinatarios:

        # Se compara el RUC buscado con el RUC almacenado.
        if destinatario[0] == ruc_buscar:

            # return devuelve el registro encontrado
            # y finaliza inmediatamente la función.
            return destinatario

    # Si no existe coincidencia,
    # return None indica que no se encontró información.
    return None