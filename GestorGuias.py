# Clase

class DatosEnvio:

    def __init__(self, numero_guia, empresa, ruc, ciudad, transportista):
        self.numero_guia = numero_guia
        self.empresa = empresa
        self.ruc = ruc
        self.ciudad = ciudad
        self.transportista = transportista


# Lista donde se almacenarán las guías

lista_datos_envio = []


# Programa principal

while True:

    print("\n========== MENÚ ==========")
    print("1. Registrar guía")
    print("2. Mostrar guías")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    # Registrar guía

    if opcion == "1":

        if len(lista_datos_envio) >= 20:
            print("\nYa se alcanzó el límite de 20 guías.")
            continue

        numero_guia = int(input("Ingrese el número de guía: "))
        empresa = input("Ingrese la razón social de la empresa: ")
        ruc = input("Ingrese el RUC: ")
        ciudad = input("Ingrese la ciudad de destino: ")
        transportista = input("Ingrese el transportista: ")

        guia = DatosEnvio(
            numero_guia,
            empresa,
            ruc,
            ciudad,
            transportista
        )

        lista_datos_envio.append(guia)

        print("\nGuía registrada correctamente.")

    # Mostrar guías

    elif opcion == "2":

        if len(lista_datos_envio) == 0:

            print("\nNo existen guías registradas.")

        else:

            print("\n===== GUÍAS REGISTRADAS =====")

            for guia in lista_datos_envio:

                print("--------------------------------")
                print("Número de guía :", guia.numero_guia)
                print("Empresa        :", guia.empresa)
                print("RUC            :", guia.ruc)
                print("Ciudad         :", guia.ciudad)
                print("Transportista  :", guia.transportista)

    # Salir

    elif opcion == "3":

        print("\nGracias por usar el sistema.")
        break

    # Opción inválida

    else:

        print("\nOpción inválida.")
