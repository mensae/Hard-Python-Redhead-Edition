# Abbiamo appreso che i programmi vengono eseguiti in ordine, riga per riga
# esistono però dei modi per modificare quali istruzioni vengono eseguite e quali no (e anche il loro ordine, come vedremo nel futuro) 
# Si parla di "Control Flow"

# Un comportamento tipico dei programmi consiste nel verificare una qualche condizione ed eseguire un blocco di codice anziché un altro. Un esempio tipico è il login: SE la password è giusta, ALLORA mostro il profilo utente, altrimenti segnalo che la password è sbagliata
# Si fa uso della istruzione IF. Ecco un esempio:


# SE la password inserita è uguale a quella inserita stampare "benvenuto", altrimenti dire che la password è sbagliata
psw_salvata = 8
psw_inserita = 7

if psw_salvata == psw_inserita:
	# blocco di codice seguito se la condizione è vera
	print("Benvenuto")
	# altre righe "se vero"
else:
	# blocco di codice seguito se la condizione è falsa
	print("Password sbagliata")
	# altre righe "se vero"

# Osserviamo alcune cose importanti:
# - "psw_salvata == psw_inserita" è la CONDIZIONE dell'if, è la cosa che viene controllata per stabilire quale parte del codice dell'if deve essere eseguito
# - Usiamo == per esprimere l'uguaglianza, perché il singolo uguale ha già la semantica dell'assegnazione di variabili
# - I blocchi "vero" e "falso" sono indentati, ossia con una tablatura (TAB)
# - if e else sono keyword riservate, speciali
# - attenzione ai due punti!
# terminato l'if, tutto prosegue come sempre

# --------------------------------------

# Le condizioni possono essere varie, ad esempio fra due numeri
num1 = 2
num2 = 3

if num1 > num2:
	print("Il secondo numero è maggiore")
else:
	print("Il primo numero è minore o uguale")

# altre varianti possono essere minore (<) maggiore uguale (>=) o minore uguale (<=)

# --------------------------------------

# Ma cosa è veramente una condizione? Proviamo a vederne il tipo

psw_salvata = 8
psw_inserita = 7

x = psw_salvata == psw_inserita
tipo_di_x = type(x)
print(tipo_di_x)

# Il tipo BOOLEAN (bool)! Nel mondo della programmazione è necessario definire in maniera formale dei VALORI DI VERITA'. Un valore booleano può essere solo True (vero) o False (falso). 
# Le condizioni di un if, quindi, vengono valutate e producono un valore booleano e quindi verranno ridotte in

# if True:
# ...

# oppure 

# if False:
# ...

# --------------------------------------

# Esattamente come coi numeri o le stringhe, anche le varibili booleane hanno degli operatori che si possono usare per combinare valori booleani. Ce ne sono diversi, vediamo i tre principali

val1 = True
val2 = False

val1 and val2
val1 or val2
not val1  
# and e or sono binari, not è unario


# TABELLE DI VERITA' 

# and => tutte variabili devono essere vere per avere valore vero (quindi ne basta una falsa per avere falso)
True and False # False
False and True # False
True and True # True
False and False # False

# and => tutte variabili devono essere false per avere valore falso (quindi ne basta una vera per avere vero)
True or False # True
False or True # True
False or False # False
True or True # True 

# il not semplicemente inverte il valore di verità
not True # False
not False # True

# --------------------------------------

# Esempi d'uso

# Condizione che è vera se e solo se  
# password e nome utente corrispondono
# e la posizione è conosciuta

nome_utente = "x"
password = "y"
nome_utente_inserito = "y"
password_inserita ="x"
posizione_conosciuta = True

nome_utente == nome_utente_inserito and password == password_inserita and posizione_conosciuta


# Condizione che è vera se e solo se  
# password e nome utente corrispondono
# e la posizione è conosciuta

nome_utente = "x"
password = "y"
nome_utente_inserito = "y"
password_inserita ="x"
posizione_sconosciuta = True

nome_utente == nome_utente_inserito and password == password_inserita and not posizione_sconosciuta

# Scrivere una condizione che sia vera se e solo se
# x e y sono uguali oppure uno è il doppio dell'altro
x = 5
y = 10

x == y or (x == y*2 or y == x*2)

# --------------------------------------
# È anche possibile inserire if dentro altri if. Si chiamano if ANNIDATI. Si osservi l'uso delle tablature
c1 = True
c2 = True
c3 = False

if c1:
	#vera c1
	print("c1 è vera")
	if c2: 
		#vera c1 (ovviamente vera c1)
		print("c2 è vera")
		if c3:
			#vera c3 (ovviamente vera c1 e c2)
			print("c3 è vera")
		else:
			#falsa c3 (ovviamente vera c1 e c2)
			print("c3 è falsa")
	else: 
		#falsa c2 (ovviamente vera c1)
		print("c2 è falsa")
else:
	#falsa c1
	print("c1 è falsa")

# Si osservi che se c1 è falsa, c2 e c3 non verranno mai verificate, se c1 è vera ma c2 è falsa, c3 non verrà mai verificata


#aiuto compito
if c1:
#vera c1
  if c2: 
    #vera c2 (ovviamente vera c1)
  else: 
    #falsa c2 (ovviamente vera c1)
else:
  #falsa c1


#prova compito 1
if nome_utente == user1 or nome_utente == user2:
  password = input("Inserisci password\n")
  if password == user2 and psw2 or password == user1 and psw1:
    print(bilancio1 or bilancio2)
  else: 
	  input("Password errata.")
else: 
	print("Nome utente invalido o inesistente.")

#prova compito 2
password == psw1 or psw2
nome_utente == user1 or user2

bilancio1 = user1 and psw1
bilancio2 = user2 and psw2


if nome_utente = user1 or user2:
	print("Inserisci "password"\n")
  if password = psw1 or psw2:
  print("Benvenuto! Questo è il tuo bilancio:")
else: 
	print("Nome utente invalido o inesistente.")