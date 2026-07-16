# ==========================================
# MÓDULO: TRANSPORTISTAS
# ==========================================
# Este módulo administra la información de los
# transportistas que realizarán el envío de las guías.

# Lista donde se almacenarán los transportistas.
# Cada registro contiene:
# [Nombre, Ciudad, Tipo]
transportistas = []

# transportistas = [] crea una lista dinámica en memoria
# donde se almacenarán todos los transportistas registrados.


# ------------------------------------------
# FUNCIÓN: Registrar Transportista
# ------------------------------------------
def registrar_transportista():

    print("\n====== REGISTRAR TRANSPORTISTA ======")

    # Se solicita el nombre del transportista.
    nombre = input("Nombre del transportista: ")

    # Se recorre la lista para verificar
    # que el transportista no exista.
    for transportista in transportistas:

        # upper() convierte el texto a mayúsculas
        # para evitar diferencias entre mayúsculas y minúsculas.
        if transportista[0].upper() == nombre.upper():

            print("\nEse transportista ya existe.")

            # return finaliza la función
            # para evitar registros duplicados.
            return

    # Se solicitan los datos del transportista.
    ciudad = input("Ciudad principal: ")
    tipo = input("Tipo (Cooperativa/Courier): ")

    # Se crea una lista con la información ingresada.
    transportista = [
        nombre,
        ciudad,
        tipo
    ]

    # append() agrega el nuevo transportista
    # al final de la lista.
    transportistas.append(transportista)

    print("\nTransportista registrado correctamente.")


# ------------------------------------------
# FUNCIÓN: Mostrar Transportistas
# ------------------------------------------
def mostrar_transportistas():

    print("\n====== LISTA DE TRANSPORTISTAS ======")

    # len() devuelve la cantidad
    # de transportistas registrados.
    if len(transportistas) == 0:

        print("No existen transportistas registrados.")

    else:

        # Contador utilizado para numerar
        # cada transportista mostrado.
        contador = 1

        # Se recorren todos los registros.
        for transportista in transportistas:

            print("--------------------------------")
            print("Transportista:", contador)
            print("Nombre:", transportista[0])
            print("Ciudad:", transportista[1])
            print("Tipo:", transportista[2])

            # Se incrementa el contador.
            contador = contador + 1


# ------------------------------------------
# OBTENER TRANSPORTISTA
# ------------------------------------------
def obtener_transportista(nombre_buscar):

    # Esta función es utilizada por el módulo Guías.
    # Recibe el nombre del transportista y devuelve
    # toda su información.

    # Se recorren todos los transportistas.
    for transportista in transportistas:

        # upper() convierte ambos textos a mayúsculas
        # para que la comparación no dependa
        # de cómo escribió el usuario el nombre.
        if transportista[0].upper() == nombre_buscar.upper():

            # Devuelve el transportista encontrado
            # y finaliza la función.
            return transportista

    # Si no existe el transportista,
    # retorna None para que el módulo
    # que llama la función pueda controlar el error.
    return None