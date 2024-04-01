# Creare una applicazione bancaria che permette di effettuare un prelievo o deposito monetario. 

# 1. Effettuare il login chiedendo separatamente nome utente e password. Ci sono solo due utenti registrati. Se il nome utente o la password sono errati (la coppia non è corretta, oppure il nome utente non esiste), dare un messaggio di errore e terminare il programma.

# 2. Se il login è corretto, stampare il bilancio del conto e chiedere se l'operazione desiderata è prelievo o deposito. Qualunque altro inserimento risulta nella terminazione del programma con un messaggio di errore.
# op = input("Prelievo o deposito?") 

# 3. Se l'operazione è di deposito, chiedere la cifra (si assuma che l'utente inserisca un intero), aggiornare il totale del conto e stamparlo a video terminando così il programma.

# 4. Se l'operazione è di prelievo, chiedere la cifra (si assuma che l'utente inserisca un intero) e verificare che il bilancio sia sufficente. Se lo è detrarlo dal totale e stampare il nuovo bilancio a video terminando così il programma. Se non lo è terminare il programma con un messaggio di errore.


user1 = "Enrico"
psw1 = "latteria!"
bilancio1 = 2000

user2 = "Michelle"
psw2 = "coprofagia@"
bilancio2 = 120


nome_utente = input("Benvenuto! Effettua login, inserisci nome utente:\n")
password = input("Inserisci password:\n")

# verifichi che l'utente sia utente1 e la password corrisponda
isuser1 = nome_utente == user1 and password == psw1
isuser2 = nome_utente == user2 and password == psw2

if isuser1 or isuser2:
	print("")
	print("Benvenuto/a", nome_utente)

	# scelgo il bilancio basandomi sull'utente
	if isuser1:
		bilancio = bilancio1
	else:
		bilancio = bilancio2
	
	print("Il tuo bilancio è", bilancio)
	print("")
	print("")
	op = input("Prelievo o deposito? (inserire p o d):\n")
	
	if op == "p":
		# codice per il prelievo
		soldi = input("Quanti soldi vuoi prelevare?\n")
		soldi = float(soldi)
		if soldi <= bilancio:
			nuovobilancio = bilancio - soldi
			print(nuovobilancio)
			# aggiorno il bilancio a seconda dell'utente
			if isuser1:
				bilancio1 = nuovobilancio
			else:
				bilancio2 = nuovobilancio
		else:
			print("Sei povero.")
	elif op == "d":
		# codice deposito
		soldi = input("Quanti soldi vuoi depositare?\n")
		soldi = float(soldi)
		nuovobilancio = bilancio + soldi
		print(nuovobilancio)
		# aggiorno il bilancio a seconda dell'utente
		if isuser1:
			bilancio1 = nuovobilancio
		else:
			bilancio2 = nuovobilancio
	else: 
		print("Operazione inesistente")
  
else: 
	print("Nome utente invalido o inesistente o password sbagliata.")

print("DATABASE BANCA ALLA FINE:")
print("Enrico: ", bilancio1)
print("Michelle: ", bilancio2)