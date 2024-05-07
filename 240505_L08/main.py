#####################################################
# Questi esercizi NON sono generici. Non sappiamo ancora trattare le liste con generalità e dinamicità, ma vogliamo allenarci a scrivere codice che coinvolga le liste.

# Modificare l1 in modo che l'i-esimo elemento di l1 risulti sé stesso meno l'i-esimo elemento di l2.
l1 = [2, 3, 4] #lunghezza fissa, valori variabili
l2 = [2, 2, 2, 5] #lunghezza fissa, valori variabili

l1[0] = l1[0] - l2[0]
l1[1] = l1[1] - l2[1]
l1[2] = l1[2] - l2[2]

l1 = [l1[0] - l2[0], l1[1] - l2[1], l1[2] - l2[2]]

# Modificare l1. Raddoppiare l'i-esimo elemento di l1 se e solo se l'i-esimo elemento di l2 è uguale a 1
l1 = [2, 3, 4] #lunghezza fissa, valori variabili
l2 = [1, 0, 0] #lunghezza fissa, valori variabili


if l2[0] == 1:
  l1[0] = l1[0]*2
if l2[1] == 1:
  l1[1] = l1[1]*2
if l2[2] == 1:
  l1[2] = l1[2]*2

# Creare una lista l3 che contenga tutti e soli gli elementi comuni sia a l1 che a l2
l1 = [2, 3, 4] #lunghezza fissa, valori variabili
l2 = [4, 2, 5] #lunghezza fissa, valori variabili

l3 = []

if l1[0] in l2:
	l3.append(l1[0])
  
if l1[1] in l2:
  l3.append(l1[1])

if l1[2] in l2:
  l3.append(l1[2])

# Costruire la lista l3 che è la somma elemento per elemento delle liste l1 ed l2. Mettere a zero l'i-esimo elemento di l3 se l'i-esimo elemento di l2 è 1.
l1 = [7, 8, 9]
l2 = [0, 1, 0]

# Soluzione 1
l3 = [0]*3

l3[0] = l1[0] + l2[0]
l3[1] = l1[1] + l2[1]
l3[2] = l1[2] + l2[2]

if l2[0] == 1:
  l3[0] = 0

if l2[1] == 1:
  l3[1] = 0

if l2[2] == 1:
  l3[2] = 0

# Soluzione 2 usare append e non puoi usare l'assegnamento

l3 = []

if l2[0] == 1:
  l3.append(0)
else:
  l3.append(l2[0] + l1[0])

if l2[1] == 1:
  l3.append(0)
else:
  l3.append(l2[1] + l1[1])

if l2[2] == 1:
  l3.append(0)
else:
  l3.append(l2[2] + l1[2])



# La variable "parola" contiene una lista di tre parole a caso.
# La variabile 'indice' è un valore casuale da 0 a 2.
import requests
from random import randrange
parole = requests.get("https://random-word-api.herokuapp.com/word?lang=it&number=3").json()
indice = randrange(0,3)


print("Parole", parole)
print("Indice", indice)

# Modificare la lista parole di modo che ogni elemento di parole sia quello in posizione indice. 
# Esempio: parole = ["ciao", "come", "stai"] e indice = 1
# Risultato: ["come", "come", "come"]

parole[0] = parole[indice]
parole[1] = parole[indice]
parole[2] = parole[indice]




