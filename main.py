# ==========================================
# SISTEMA DE GESTIÓN DE GUÍAS DE ENVÍO
# Programa Principal
# ==========================================
# Este archivo controla la ejecución del sistema.
# Desde aquí se muestra el menú principal y se llama
# a las funciones de cada módulo.

# Se importan las funciones del módulo Clientes.
from clientes import registrar_cliente
from clientes import buscar_cliente
from clientes import mostrar_clientes

# Se importan las funciones del módulo Transportistas.
from transportistas import registrar_transportista
from transportistas import mostrar_transportistas

# Se importan las funciones del módulo Destinatarios.
from destinatarios import registrar_destinatario
from destinatarios import buscar_destinatario
from destinatarios import mostrar_destinatarios

# Se importan las funciones del módulo Guías.
from guias import generar_guia
from guias import buscar_guia
from guias import mostrar_guias
from guias import modificar_guia

# Se importan las funciones del módulo Reportes.
from reportes import total_guias
from reportes import guias_registradas
from reportes import buscar_por_cliente

# Variable que almacena la opción seleccionada por el usuario.
opcion = 0

# Mensaje de inicio del sistema.
print("Programa iniciado correctamente")

# while mantiene el programa ejecutándose
# hasta que el usuario seleccione la opción 12.
while opcion != 12:

    print("\n========================================")
    print(" SISTEMA GESTIÓN DE GUÍAS DE ENVÍO")
    print("========================================")
    print("1. Registrar Cliente")
    print("2. Buscar Cliente")
    print("3. Mostrar Clientes")
    print("4. Registrar Destinatario")
    print("5. Buscar Destinatario")
    print("6. Mostrar Destinatarios")
    print("7. Registrar Transportista")
    print("8. Generar Guía")
    print("9. Buscar Guía")
    print("10. Modificar Estado")
    print("11. Reportes")
    print("12. Salir")
    print("========================================")

    # input() recibe la opción del usuario.
    # int() convierte el dato ingresado de texto a número.
    opcion = int(input("Seleccione una opción: "))

    # Cada opción llama a una función específica
    # utilizando una estructura if - elif - else.

    if opcion == 1:

        # Llama a la función para registrar un cliente.
        registrar_cliente()

    elif opcion == 2:

        print("Entró a buscar cliente")

        # Busca un cliente mediante su RUC.
        buscar_cliente()

    elif opcion == 3:

        print("Entró a mostrar clientes")

        # Muestra todos los clientes registrados.
        mostrar_clientes()

    elif opcion == 4:

        # Registra un destinatario.
        registrar_destinatario()

    elif opcion == 5:

        # Busca destinatarios asociados a un cliente.
        buscar_destinatario()

    elif opcion == 6:

        # Muestra todos los destinatarios registrados.
        mostrar_destinatarios()

    elif opcion == 7:

        # Registra un transportista.
        registrar_transportista()

    elif opcion == 8:

        # Genera una nueva guía de envío.
        generar_guia()

    elif opcion == 9:

        # Busca una guía mediante su número.
        buscar_guia()

    elif opcion == 10:

        # Permite modificar el estado de una guía.
        modificar_guia()

    elif opcion == 11:

        # Menú secundario para los reportes.
        print("\n========== REPORTES ==========")
        print("1. Total de Guías")
        print("2. Guías Registradas")
        print("3. Buscar por Cliente")

        # Se solicita la opción del reporte.
        reporte = int(input("Seleccione una opción: "))

        if reporte == 1:

            # Muestra el total de guías registradas.
            total_guias()

        elif reporte == 2:

            # Cuenta únicamente las guías
            # con estado REGISTRADA.
            guias_registradas()

        elif reporte == 3:

            # Busca todas las guías
            # pertenecientes a un cliente.
            buscar_por_cliente()

        else:

            # Se ejecuta cuando la opción
            # del reporte no existe.
            print("Opción incorrecta.")

    elif opcion == 12:

        # Finaliza el programa.
        print("Gracias por utilizar el sistema.")

    else:

        # Se ejecuta cuando el usuario
        # ingresa una opción inválida.
        print("Opción incorrecta.")