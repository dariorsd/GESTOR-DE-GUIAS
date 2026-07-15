# Clase

class DatosEnvio:

    def __init__( self, usuario, numero_guia, empresa, ruc, ciudad, transportista):

        self.usuario = usuario
        self.numero_guia = numero_guia
        self.empresa = empresa
        self.ruc = ruc
        self.ciudad = ciudad
        self.transportista = transportista


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
            usuario_actual,
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
                print("Usuario        :", guia.usuario)
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
