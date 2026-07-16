# ==========================================
# MÓDULO: CLIENTES
# ==========================================
# Este módulo administra la información de los clientes.
# Cada cliente será utilizado posteriormente para generar
# las guías de envío.

# Lista donde se almacenarán todos los clientes.
# Cada cliente se guarda con la siguiente estructura:
# [RUC, Razón Social, Dirección, Ciudad, Provincia, Teléfono]

clientes = []
#crea una lista dinámica donde se almacenan todos los clientes en memoria.

# ------------------------------------------
# FUNCIÓN: Registrar Cliente
# ------------------------------------------
def registrar_cliente():

    print("\n========== REGISTRAR CLIENTE ==========")

    # Se solicita el RUC, que será el identificador único del cliente.
    ruc = input("Ingrese el RUC: ")

    # Se recorre la lista para verificar que el RUC
    # no exista previamente.
    for cliente in clientes:

        if cliente[0] == ruc:

            print("\nERROR: El cliente ya se encuentra registrado.")

            # Se finaliza la función para evitar registros duplicados.
            return

    # Se solicitan los demás datos del cliente.
    nombre = input("Ingrese la razón social: ")
    direccion = input("Ingrese la dirección: ")
    ciudad = input("Ingrese la ciudad: ")
    provincia = input("Ingrese la provincia: ")
    telefono = input("Ingrese el teléfono: ")

    # Se crea una lista con toda la información del cliente.
    cliente = [
        ruc,
        nombre,
        direccion,
        ciudad,
        provincia,
        telefono
    ]

    # Se agrega el cliente a la lista principal.
    clientes.append(cliente)

    # Se imprime la lista para comprobar que el registro
    # fue almacenado correctamente (solo para pruebas).
    #print(clientes)

    print("\nCliente registrado correctamente.")


# ------------------------------------------
# FUNCIÓN: Buscar Cliente
# ------------------------------------------
def buscar_cliente():

    print("\n========== BUSCAR CLIENTE ==========")

    # Se solicita el RUC que se desea buscar.
    ruc_buscar = input("Ingrese el RUC: ")

    # Variable bandera para saber si el cliente existe.
    encontrado = False

    # Se recorre toda la lista de clientes.
    for cliente in clientes:

        # Se compara el RUC ingresado con el RUC almacenado.
        if cliente[0] == ruc_buscar:

            print("\nCliente encontrado")

            print("RUC:", cliente[0])
            print("Razón Social:", cliente[1])
            print("Dirección:", cliente[2])
            print("Ciudad:", cliente[3])
            print("Provincia:", cliente[4])
            print("Teléfono:", cliente[5])

            # Se cambia el estado de la variable
            # porque el cliente fue encontrado.
            encontrado = True

    # Si no hubo coincidencias se informa al usuario.
    if encontrado == False:

        print("\nCliente no registrado.")

    # Pausa para que el usuario pueda leer la información.
    input("\nPresione ENTER para volver al menú...")


# ------------------------------------------
# FUNCIÓN: Mostrar Todos los Clientes
# ------------------------------------------
def mostrar_clientes():

    print("\n========== LISTA DE CLIENTES ==========")

    # Se verifica si existen clientes registrados.
    if len(clientes) == 0:

        print("No existen clientes registrados.")

    else:

        # Contador utilizado para numerar los registros.
        contador = 1

        # Se recorre toda la lista de clientes.
        for cliente in clientes:

            print("--------------------------------")
            print("Cliente:", contador)
            print("RUC:", cliente[0])
            print("Nombre:", cliente[1])
            print("Ciudad:", cliente[3])

            # Incrementa el contador para el siguiente registro.
            contador = contador + 1

            # Pausa para visualizar cada cliente.
            input("\nPresione ENTER para volver al menú...")


# ------------------------------------------
# OBTENER CLIENTE POR RUC
# ------------------------------------------
def obtener_cliente(ruc_buscar):

    # Esta función es utilizada por otros módulos,
    # especialmente por el módulo de Guías.
    # Su objetivo es devolver toda la información
    # del cliente a partir del RUC.

    # Se recorre la lista buscando coincidencias.
    for cliente in clientes:

        if cliente[0] == ruc_buscar:

            # Devuelve el cliente encontrado.
            return cliente

    # Si no existe el cliente, retorna None
    # para que el módulo que llamó la función
    # pueda controlar ese caso.
    return None