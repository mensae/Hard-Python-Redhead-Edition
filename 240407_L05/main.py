# *** precisazione importante ***
# funzioni chiamate su variabili e funzioni non chiamate su variabili
testo = "Bellissimo testo"
testo.startswith("x") # chiamata sulla variabile (uso del punto)
len(testo) # chiamata generica 
# non c'è una regola precisa per cui è len(x) e non x.len()... 
# i motivi esistono, ma sono troppo approfonditi per la nostra conoscenza
# quindi limitiamoci a imparare a memoria quali funzioni si applicano su una variabile e quali no. un indicazione può essere che funzioni "generiche" sono senza variabile

# ---------------------------------------------------------
# Esempio di software. Detector di parole bannabili, implementato in una chat di Twitch
# Ogni messaggio viene controllato e se contiene una parola bannabile viene scartata
# Chiedere messaggio all'utente e stampare il messaggio se non è bannabile, un messaggio di alert se lo è

p1 = "pandoro"
p2 = "balocco"
p3 = "fidanzato"
p4 = "pubblicità"
p5 = "adv"
p6 = "onlyfans"
p7 = "piedi"
p8 = "divorzio"
p9 = "separazione"
p10 = "sesso"

# prendo in input una parola

messaggio = input("Scrivi messaggio\n")

# controllo se è bannabile e restituisco il risultato

if p1 == messaggio.lower() or p2 == messaggio.lower() or p3 == messaggio.lower() or p4 == messaggio.lower() or p5 == messaggio.lower() or p6 == messaggio.lower() or p7 == messaggio.lower() or p8 == messaggio.lower() or p9 == messaggio.lower() or p10 == messaggio.lower():
  print("Sei bannato!")
else:
  print(messaggio)

# Dovendo cambiare questo codice osserviamo come sia necessario cambiare LA LOGICA. Dobbiamo aggiungere una condizione all'if. 

# Ci sarà un modo più comodo di memorizzare un insieme di valori? Sì. LE LISTE
# Dichiarazione di una lista
l = [1, 2, 3]
# è di tipo list, dentro ci possono stare valori di tutti i tipi anche mischiati
# gli elementi hanno un INDICE, che parte da zero. si può accedere ad un elemento indicando l'indice fra quadre
# #NOME_DELLA_LISTA[INDICE]
print(l[1]) # stampa 2
# ed è come una variabile a sé, possiamo cambiare valore
l[1] = 2000
# è possibile usare anche len() per sapere quanti elementi ci sono
len(l) # 3
# possiamo aggiungere o rimuovere elementi
l.append(4) # aggiunge quattro alla lista
l.pop(0) # toglie il primo elemento (indice zero)

# Osserviamo anche un comportamento interessante. Possiamo accedere alle stringhe come fossero liste! 
testo = "ciao"
print(testo[2]) # lettera a

# Ulteriore aggiunta in merito alle stringhe:

# - le stringhe possono essere suddivise basandosi su una stringa di divisione. Ad esempio data la frase
t = "ciao come stai"
# posso ottenere le singole parole splittando per spazio 
parole = t.split(" ")
print(parole) # lista di tre elementi


# --------------------------------

# Ora riprendiamo l'esercizio di prima ma usiamo le liste, 
bannabili = ["pandoro", "balocco", "fidanzato", "pubblicità", "adv", "onlyfans", "piedi", "divorzio", "separazione", "sesso"]

messaggio = input("Scrivi messaggio\n")

# controllo se è bannabile e restituisco il risultato

if messaggio in bannabili:
  print("Sei bannato!")
else:
  print(messaggio)

# È molto meglio! Ora la logica non cambia MAI, basta aggiungere parole alla lista di parole bannabili