#####################################################
# Questi esercizi NON sono generici. Non sappiamo ancora trattare le liste con generalità e dinamicità, ma vogliamo allenarci a scrivere codice che coinvolga le liste.

# Creare una lista che contenga nella posizione i-esima la somma degli elementi i-esimi di l1 e l2 
l1 = [1, 2, 3, 4] #lunghezza fissa, valori variabili
l2 = [4, 3, 2, 1] #lunghezza fissa, valori variabili

l3 = [l1[0] + l2[0], l1[1] + l2[1], l1[2] + l2[2], l1[3] + l2[3]]	


# Creare una lista che contenga la somma degli elementi i-esimi di l1 e l2 ma solo per gli i contenuti in l3
l1 = [1, 5, 10, 1] #lunghezza fissa, valori variabili
l2 = [1, 5, 10, 1] #lunghezza fissa, valori variabili
l3 = [1, 2] #lunghezza fissa, valori variabili (sempre minori di min(len(l1), len(l2))-1)

l4 = [ l1[l3[0]] + l2[l3[0]], l1[l3[1]] + l2[l3[1]] ]

# Creare una lista che contenga nell'indice i-esimo la somma degli elementi della i-esima lista => sum()
l1 = [1, 2, 3, 4] #lunghezza e valori variabili
l2 = [2, 3, 4, 5] #lunghezza e valori variabili
l3 = [3, 5, 2, 8] #lunghezza e valori variabili
l4 = [11, 5, 1]  #lunghezza e valori variabili

l5 = [sum(l1), sum(l2), sum(l3), sum(l4)]


# modificare l1 così che ad ogni suo elemento vengano sommati il massimo e il minimo trovati nella lista l2 => max e min
l1 = [100, 300] #lunghezza fissa, valori variabili
l2 = [590, 120, 102, 1] #lunghezza e valori variabili

# max(x) => il valore massimo in x
# min(x) => il valore minimo in x

l1 = [l1[0] + max(l2) + min(l2), l1[1] + max(l2) + min(l2)]


#############################
# DA FARE A CASA #

# trovare il valore massimo fra le due liste l1 e l2 => +
l1 = [1, 5, 10, 1] #lunghezza e valori variabili
l2 = [12, 3] #lunghezza e valori variabili

# creare una lista che contenga nella posizione i-esima il numero di occorrenze di i in l1, sapendo che l1 può avere solo 0, 1 e 2 come valori => count
l1 = [0, 1, 0, 0, 2, 1, 2, 0] #lunghezza variable, valori variabili ma solo nell'intervallo 0-2

# controllare che le due liste siano identiche => reverse tanto per 
l1 = [1, 5, 10, 1] #lunghezza fissa, valori variabili
l2 = [1, 5, 10, 1] #lunghezza fissa, valori variabili
