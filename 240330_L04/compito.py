# Scrivi un programma in Python che chieda all'utente il suo reddito annuo e calcoli l'ammontare delle tasse dovute basandosi su semplici fasce di reddito.

# Prima di tutto chiedere all'utente il suo nome e cognome in una sola stringa (usando cioè un solo input). Se il suo nome o cognome includono "Fedez" (indipendentemente dalle maiuscole), allora stampare direttamente "Sei nulla tenente." e chiudere il programma. Altrimenti procedere come segue:

# Redditi fino a 10.000 €: esenti da tasse.
# Redditi superiori a 10.000 € e fino a 20.000 €: tassati al 10%.
# Redditi superiori a 20.000 € e fino a 30.000 €: tassati al 20%.
# Redditi superiori a 30.000 €: tassati al 30%.
# Il programma dovrebbe mostrare l'ammontare delle tasse dovute secondo queste regole.

nome_utente = input("Benvenuto! DIMMI IL TUO NOME E COGNOME ORA!!!\n")

if "fedez" in nome_utente.lower():
	print("Chill, sei nullatenente!")
else:
	soldi = float(input("Quanti soldi hai guadagnato?\n"))

	if soldi <= 10000:
		print("no tasse bro")
	elif soldi > 10000 and soldi <= 20000:
		tasse = ((soldi*10)/100)
		print("Dammi", tasse)
	elif soldi > 20000 and soldi <= 30000:
		tasse = ((soldi*20)/100)
		print("Dammi", tasse)
	else:
	  tasse = ((soldi*30)/100)
	  print("Dammi", tasse)