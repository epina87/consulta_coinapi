from criptoexchange.models import Cambio,TodoCoinApiIO,ModelError
from config import apiKey

todas = TodoCoinApiIO()
todas.trae(apiKey)

print("{} de {}".format(len(todas.criptos),len(todas.criptos)+len(todas.no_criptos)))

cripto = input("Introduzca una cripto conocida: ").upper()
while cripto != "":
    if cripto in todas.criptos:
        tipoCambio = Cambio(cripto)
        try:
            tipoCambio.actualiza(apiKey)

            print("{:.2f}€".format(tipoCambio.tasa))

        except ModelError as variable:
            print("Se ha producido un error {}".format(variable))

    cripto = input("Introduzca una cripto conocida: ").upper()


