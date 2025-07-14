#Esta parte del codigo importa las librerias para descargar el archivo de internet y cuenta las palabras
import urllib.request
from collections import Counter

#Descargar el archivo y lo lee y convierte los bytes del texto a texto normal
url = "https://www.py4e.com/code3/mbox.txt"
respuesta = urllib.request.urlopen(url)
texto = respuesta.read().decode()

#Aca van los caracteres que se van a verificar
vocales = 'aeiouAEIOU'
consonantes = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

#Aca se cuentan las vocales y las consonantes
cantidad_vocales = sum(1 for letra in texto if letra in vocales)
cantidad_consonantes = sum(1 for letra in texto if letra in consonantes)

#Busca las palabras mas repetidas
palabras = texto.split()
conteo = Counter(palabras)

#Muestra los resultados
print("Cantidad de vocales:", cantidad_vocales)
print("Cantidad de consonantes:", cantidad_consonantes)
print("Las 50 palabras mas repetidas:")
for palabra, freq in conteo.most_common(50):
    print(f"{palabra}: {freq}")