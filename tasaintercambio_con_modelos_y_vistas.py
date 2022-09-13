
from criptoexchange.models import Cambio,TodoCoinApiIO,ModelError
from config import apiKey
from criptoexchange.views import pideCripto,mostrarTipoCambio,mostrarError

todas = TodoCoinApiIO()
todas.trae(apiKey)

print("{} de {}".format(len(todas.criptos),len(todas.criptos)+len(todas.no_criptos)))

cripto = pideCripto()

while cripto != "":
    if cripto in todas.criptos:
        tipoCambio = Cambio(cripto)
        try:
            tipoCambio.actualiza(apiKey)            
            mostrarTipoCambio(tipoCambio.tasa)


        except ModelError as variable:
            mostrarError(variable)           
            

    cripto = pideCripto()


