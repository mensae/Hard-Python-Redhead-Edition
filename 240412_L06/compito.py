# Chiedere una frase all'utente e stampare il numero di parole che contiene (consideriamo lo spazio come separatore di parola)

frase = input("Ciao, dimmi quello che vuoi.\n")
parole = frase.split(" ")

print("Hai scritto", len(parole), "parole")

# Poi chiedere all'utente quale parola vuole cambiare. L'utente fornirà la posizione della parola (verificare che sia una posizione esistente)

cambio = int(input("Quale parola vuoi cambiare?(ins. pos)\n"))

if cambio > len(parole):
	print("Non posso cambiare")
else:
	print(parole) # ["ciao", "come", "stai?"]
	print(cambio) # 2 

	sostituto = parole[cambio-1]
	parole[cambio-1] = parole[0]
	parole[0] = sostituto 

	print(" ".join(parole))

# Scambiare la prima parola della frase con la parola nella posizione fornita dall'utente.

# Esempio: 'Ciao come stai?' fornendo 2 diventa 'come Ciao stai?'
# Fare dunque attenzione alla distizione fra indici e posizioni. 




