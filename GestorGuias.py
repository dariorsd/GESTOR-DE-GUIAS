class datos_envio:
    def __init__(self, empresa, ruc, numero_guia, ciudad, transportista):
        self.empresa = empresa
        self.ruc = ruc
        self.numero_guia = numero_guia
        self.ciudad = ciudad
        self.transportista = transportista

lista_datos_envio = []

def main():
  numero_guia = 00

  while numero_guia < 20:
    #DATOS DE ENTRADA

    numero_guia = int(input("Ingrese el numero de guia: "))
    
    #SECUENCIA DE PASOS

    if numero_guia > 00 and numero_guia < 20:
      empresa =  input("Ingrese la empresa: ")
      ruc = input("Ingrese el RUC: ")
      ciudad = input("Ingrese la ciudad: ")
      transportista = input("Ingrese el transportista: ")

    data = datos_envio(empresa, ruc, numero_guia, ciudad, transportista)
    lista_datos_envio.append(data)

# input

numero_guia = int(input("Ingrese el numero de guia: "))

#output
for datos in lista_datos_envio:
    print(f"En la guia {datos.numero_guia}, la empresa {datos.empresa} con RUC {datos.ruc}, envio a la ciudad de {datos.ciudad} con el transportista {datos.transportista}")