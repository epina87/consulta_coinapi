
from criptoexchange.models import Cambio,TodoCoinApiIO,ModelError
from config import apiKey
from criptoexchange.views import pideCripto,mostrarTipoCambio,mostrarError

class Exchanger:
    def ejecuta(self):

        todas = TodoCoinApiIO()
        todas.trae(apiKey)

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
