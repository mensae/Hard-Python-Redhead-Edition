# Scrivere un programma chiamato numerator
# Il programma deve:
# - Scrivere un messaggio di benvenuto al lancio, indicando il suo nome
# - Chiedere all'utente quattro numeri 
# - Sommare i numeri e stamparli a video
# - Chiedere un quinto numero
# - Sottrarlo dalla somma precedente e stamparlo a video

# Usare se necessario delle stampe per spiegare i valori che vengono mostrati all'utente


# chiedo il nome utente
nome_utente = input("Benvenuto coglioncello! Come ti chiami?\n")

# chiedo i quattro numeri
num1 = input("Bene, " + nome_utente + ", ora dimmi quattro numeri!\n")
num2 = input()
num3 = input()
num4 = input()

# casto i numeri a float
num1 = float(num1)
num2 = float(num2)
num3 = float(num3)
num4 = float(num4)

risultato1 = num1 + num2 + num3 + num4
print("Somma dei tuoi numeri è:", risultato1)

num5 = input("Bravo stupido, ora dammi un altro numero... \n")
num5 = float(num5)

risultato2 = risultato1 - num5

print("Il risultato finale è", risultato2)