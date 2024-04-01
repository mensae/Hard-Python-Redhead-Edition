# ----------------------------------
# Ignorare questa parte di codice, serve per generare 
# cinque numeri casuali (num1, num2, num3, num4, num5)
# E un utente casuale (name, gender, email password)
# Usiamo questi dati per fare esercizi
import requests

num1, num2, num3, num4, num5 = requests.get("http://www.randomnumberapi.com/api/v1.0/random?min=1&max=1000&count=5").json()

namejs = requests.get("https://randomuser.me/api/?results=1").json()["results"][0]
gender = namejs["gender"]
name = namejs["name"]["first"]
email = namejs["email"]
password = namejs["login"]["password"]

# ----------------------------------

print("Numeri generati:")
print(num1, num2, num3, num4, num5)

print("Persona generata:")
print(name, gender, email, password)

print("")

# Alcune funzionalità utili per quando si ha a che fare con le stringhe

# usando le funzioni x.lower() e x.upper() 
# posso rendere la stringa x tutta minuscola o tutta maiuscola
tuttominuscolo = name.lower()
tuttomaiuscolo = name.upper()
print(tuttominuscolo)
print(tuttomaiuscolo)
# si noti che per la prima volta una funzione è richiamata con il punto dopo la variabile
# e la variabile non viene data come parametro alla funzione
# cioè, non scriviamo lower(x) ma x.lower()

# la funzione len() restituisce la lunghezza della stringa
if len(password) > 5: 
	print("Password lunga 6 o più caratteri")

# Usando la keyword "in" possiamo verificare se una stringa è dentro un altra
# stringa. Qui combiniamo anche l'uso di lower()
if "r" in name.lower():
	c = name.lower().count("r") # e contiamo quante volte c'è la r
	print("Il nome ha dentro una r e ne ha", c)

# Possiamo, usando x.endswith(y) controllare se la stringa x finisce in y
if name.endswith("ia"):
	print("IL nome finisce con ia")

# Possiamo, usando x.startswith(y) controllare se la stringa x inizia con y
if name.startswith("Ca"):
	print("IL nome inizia con Ca")





