######### Tipi di dati (e variabili) ########

# le variabili contengono uno e un solo dato
# questo dato ha un tipo (e quindi la variabile ha quel tipo)
a = 10.2 # float (con la virgola)
b = 10 # int (intero)
c = "ciao" # str (stringa, notare le virgolette!)

# possiamo leggere il tipo di una variabile
# con la funzione type
tipo_di_c = type(c)

# + è un operatore che si comporta diversamente
# a seconda dei tipi di variabili che ha intorno
# int + int => int
# float + float => float
# int + float => float
# str + str => str
print(c)
print(tipo_di_c)

# chiedere a un utente un dato
# input ritorna SEMPRE una stringa
# si noti l'uso di \n, un carattere speciale 
# per andare a capo
dato_da_utente = input("Metti il nome utente:\n")


######### Casting ########

# Il casting permette di convertire le variabili da un tipo
# ad un altro
# data una variabile x
# se voglio castare a str uso str(x)
# se voglio castare a int uso int(x)
# se voglio castere a float uso float(x)

# Esempio:
a = "10" # questo è una stringa
a = int(a) # questo è un intero che viene castato dalla stringa
# attenzione però!
a = "dieci"
a = int(a) # darà errore!


# Un piccolo esempio di uso del casting:
# la spesa deve essere castata
# sperando che l'utente rispetti le richieste
# vedremo nel futuro modi per trattare gli errori generati
# dall'uso improprio dell'utente
bilancio = 230
spesa = input("Inserisci spesa in euro\n")

spesa = int(spesa)
risultato = bilancio - spesa


print("Il tuo bilancio ora è:")
print(risultato)

######### Ancora esempi di casting e concatenazioni ########

a = "due"
b = 4

print(a+" "+str(b))
# si noti che la print può prendere più parametri
# uno è str, l'altro int... così non abbiamo errore
# perché la print tollera più tipi diversi
print(a,b) 

