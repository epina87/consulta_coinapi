
import requests
from config import apiKey

cripto = input("Introduzca una cripto conocida: ")

while cripto != "":
    if cripto.isalpha():
        r = requests.get("https://rest.coinapi.io/v1/exchangerate/{}/EUR?apikey={}".format(cripto,apiKey))
        resultado = r.json()

        if r.status_code == 200:   
            print("{:.2f}€".format(resultado["rate"]))
        else:
            print(resultado["error"])

    cripto = input("Introduzca una cripto conocida: ")

