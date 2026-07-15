# Clase

class DatosEnvio:

    def __init__( self, usuario, numero_guia, empresa, ruc, distrito, transportista, estado):

        self.usuario = usuario
        self.numero_guia = numero_guia
        self.empresa = empresa
        self.ruc = ruc
        self.distrito = distrito
        self.transportista = transportista
        self.estado = estado

# Lista donde se almacenarán las guías

lista_datos_envio = []

# usuarios y contraseñas

usuario1 = "Dario"
clave1 = "2026"
usuario2 = "Hernan"
clave2 = "2026"
usuario3 = "Martina"
clave3 = "2026"
usuario4 = "James"
clave4 = "2026"

# Programa principal

intentos = 0

while intentos < 3:

    usuario = input("Usuario: ")
    clave = input("Contraseña: ")

    if usuario == usuario1 and clave == clave1:
        usuario_actual = usuario
        print("Bienvenido", usuario_actual)
        break

    elif usuario == usuario2 and clave == clave2:
        usuario_actual = usuario
        print("Bienvenido", usuario_actual)
        break

    elif usuario == usuario3 and clave == clave3:
        usuario_actual = usuario
        print("Bienvenido", usuario_actual)
        break

    elif usuario == usuario4 and clave == clave4:
        usuario_actual = usuario
        print("Bienvenido", usuario_actual)
        break

    else:
        print("Usuario o contraseña incorrectos.")
        intentos += 1

if intentos == 3:
    print("Sistema bloqueado")
    exit()

while True:

    print("\n========== MENÚ ==========")
    print("1. Registrar guía")
    print("2. Cambiar estado")
    print("3. Mostrar guías")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    # Registrar guía

    if opcion == "1":

        if len(lista_datos_envio) >= 20:
            print("\nYa se alcanzó el límite de 20 guías.")
            continue

        numero_guia = int(input("Ingrese el número de guía: "))
        empresa = input("Ingrese la razón social de la empresa: ")
        ruc = input("Ingrese el RUC: ")
        distrito = input("Ingrese el distrito de destino: ")
        transportista = input("Ingrese el transportista: ")

        guia = DatosEnvio(
            usuario_actual,
            numero_guia,
            empresa,
            ruc,
            distrito,
            transportista,
            "Sin procesar"
        )

        lista_datos_envio.append(guia)

        print("\nGuía registrada correctamente.")

    # Cambiar estado

    elif opcion == "2":
        print("\n===== GUÍAS DISPONIBLES =====")

        for guia in lista_datos_envio:
            print(f"Guía N° {guia.numero_guia} - Estado: {guia.estado}")
            numero = int(input("\nSeleccione el número de guía: "))

            print("\n===== CAMBIAR ESTADO =====")

        print("1. En almacén")
        print("2. En camino")
        print("3. Entregada")
        print("4. Cancelar")

        opcion_estado = input("Seleccione una opción: ")

        if opcion_estado == "1":
            guia.estado = "En almacén"

        elif opcion_estado == "2":
            guia.estado = "En camino"

        elif opcion_estado == "3":
            guia.estado = "Entregada"

        elif opcion_estado == "4":
            print("Volviendo al menú principal.")
        

        else:
             print("Opción inválida.")

        

    # Mostrar guías

    elif opcion == "3":

        if len(lista_datos_envio) == 0:

            print("\nNo existen guías registradas.")

        else:

            print("\n===== GUÍAS REGISTRADAS =====")

            for guia in lista_datos_envio:

                print("--------------------------------")
                print("Usuario        :", guia.usuario)
                print("Número de guía :", guia.numero_guia)
                print("Empresa        :", guia.empresa)
                print("RUC            :", guia.ruc)
                print("Distrito       :", guia.distrito)
                print("Transportista  :", guia.transportista)
                print("Estado         :", guia.estado)

    # Salir

    elif opcion == "4":

        print("\nGracias por usar el sistema.")
        break

    # Opción inválida

    else:

        print("\nOpción inválida.")
