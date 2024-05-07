# La variabile parole contiene una lista di 5 parole 
# La variabile lista_maiuscole è una lista di 5 interi che possono essere solo 0 o 1.
import requests
from random import randrange, sample

parole = requests.get("https://random-word-api.herokuapp.com/word?lang=it&number=5").json()

print("Parole", parole)

lista_maiuscole = [0]*3 + [1]*2
random.shuffle(lista_maiuscole)
print("Lista maiuscole", lista_maiuscole)

# Modificare la lista parole rendendo maiuscolo l'i-esimo elemento se l'i-esimo elemento di lista_maiuscole è 1

# Costruire poi due liste separate che contengono rispettivamente solo gli elementi maiuscoli e solo gli elementi minuscoli di parole
