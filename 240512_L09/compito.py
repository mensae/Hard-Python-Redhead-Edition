# Date due liste l1 l2 di lunghezza randomica ma uguale e valori randomici 
from random import randrange, sample

r_len = randrange(1,10)
l1 = sample(range(1, 50), r_len)
l2 = sample(range(1, 50), r_len)

print(f"Lista 1: {l1}")
print(f"Lista 2: {l2}")
print(f"Le due liste hanno lunghezza {r_len}")


### USARE I WHILE ###

# Costruire una l3 che contenga in posizione i-esima il minimo fra l'i-esimo elemento di l1 e l'i-esimo elemento di l2.


# Costruire una l3 che contenga in posizione i-esima il l'i-esimo valore di l1 solo se l'i-esimo valore di l2 è maggiore di 3, 0 altrimenti


# Costruire una l3 che contenga tutti e soli i valori comuni fra l1 e l2