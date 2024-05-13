# Aggiungere ad ogni elemento di l1 il valore x
# l1 ha lunghezza fissa e valori variabili
x = 10
l1 = [10, 20, 30]

l1[0] = l1[0] + x 
l1[1] = l1[1] + x 
l1[2] = l1[2] + x 

# Aggiungere ad ogni elemento di l1 il valore x
# l1 ha lunghezza VARIABILE e valori variabili

l1 = [10, 20, 30, 40]
# Non si può fare. Abbiamo bisogno di costruire il nostro primo loop!

x = 10
i = 0
while i < len(l1):
	l1[i] = l1[i] + x 
	i = i + 1

# costruire una lista l3 che contenga nella posizione i-esima la somma degli i-esimi elementi di l1 e l2.
# l1 e l2 sono di UGUALE lunghezza (variabile) e valori variabili
l1 = [10, 20, 30, 20]
l2 = [3, 2, 1, 1]

l3 = [1]*len(l1)
i = 0
while i < len(l1):
  l3[i] = l1[i] + l2[i]
  print(l3[i])
  i = i +1

