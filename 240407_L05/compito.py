# Creare un programma che analizzi tre interi forniti dall'utente. 

# PARTE 1 #
# Prima di tutto chiedere il nome dell'utente. Se l'utente non ha scritto il nome con la maiuscola nella prima lettera, sostituirla. PS: x.isupper() controlla se una variabile è maiuscola. 
# Stampare un messaggio di benvenuto usando il nome utente eventualmente corretto


# PARTE 2 #
# Poi, in un solo input, chiedere due numeri separati da virgola Esempio: 3,2
# In un successivo input, chiedere il terzo intero

# Ospitare tutti i numeri in una lista,
# - stamparli uno per uno
# - stampare la media

# Eseguire i controlli (per ogni controllo dare un feedback all'utente tramite una stampa)
# - Verificare se il terzo numero sia maggiore della somma degli altri due
# - Verificare se i tre numeri sono tutti diversi fra loro
# - Verificare se la somma dei tre numeri è maggiore o minore al numero di caratteri nel nome dell'utente


# PARTE 1 #

nome_utente = input("Inserisci nome utente:\n")
print("")

# Enrico
nome_utente = nome_utente.capitalize()

print("Benvenuto",nome_utente)


# PARTE 2 #

due_numeri = input("Dammi 2 numeri separati da una virgola, senza spazi\n")
terzo_numero = input("Dammi un terzo numero\n")

lista = due_numeri.split(",") # "4,5" => ["4", "5"]
lista.append(terzo_numero) # ["4", "5", "9"]

lista[0] = int(lista[0])
lista[1] = int(lista[1])
lista[2] = int(lista[2])
print("")

# [4, 5, 9]

print("Primo numero:", lista[0])
print("Secondo numero:", lista[1])
print("Terzo numero:", lista[2])


print("La media dei tre numeri è:", sum(lista) / len(lista))

# Verifico se i tre numeri sono diversi fra loro
if lista[0] == lista[1] or lista[0] == lista[2] or lista[1] == lista[2]:
  print("No, sono tutti uguali")
elif lista[0] == lista[1]:
  print("No, i primi due numeri sono uguali")
elif lista[0] == lista[2]:
  print("No, il primo e il terzo numero sono uguali")
elif lista[1] == lista[2]:
  print("No, il secondo e il terzo numero sono uguali")
else:
  print("Si")

# Verifico se la somma è maggiore ai caratteri del nome
print("3. La somma dei numeri è maggiore ai caratteri del nome?")
if sum(lista) > len(nome_utente):
  print("Si")
else:
  print("No")

> < =

# - Verificare se il terzo numero sia maggiore della somma degli altri due

if lista[2] > lista[1] + lista[0]:
  print("Il terzo numero è maggiore della somma degli altri due")