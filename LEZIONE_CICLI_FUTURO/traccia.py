
# Aggiungere ad ogni elemento di l1 il valore x
# l1 ha lunghezza VARIABILE e valori variabili
x = 10
l1 = [10, 20, 30]
# Non si può fare. Abbiamo bisogno di costruire il nostro primo loop!

i = 0
while i < len(l1):
	l1[i] = l1[i] + x 
	i = i + 1


# costruire una lista l3 che contenga nella posizione i-esima la somma degli i-esimi elementi di l1 e l2.
# l1 e l2 sono di UGUALE lunghezza (variabile) e valori variabili
l1 = [10, 20, 30]
l2 = [3, 2, 1]


# e se le liste fossero di lunghezza DIVERSA? Se l'elemento i-esimo non esiste nella lista lx, allora si consideri come se fosse zero.
# facciamo generare le liste (ignoriamo per ora il codice di generazione)
from random import randrange, sample
l1 = sample(range(1, 50), randrange(1,5))
l2 = sample(range(1, 50), randrange(1,5))

print(f"Lista 1: {l1} -> lunghezza: {len(l1)}")
print(f"Lista 2: {l2} -> lunghezza: {len(l2)}")