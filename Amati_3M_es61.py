#Diego Amati
indice =0

nome_max = str
nome_min = str
print("questo programma dato un numero di citta ti calcola l'indice di abitnti di ogni citta e ti stampa il più basso")
numero_città = int(input("inserisci il numero  delle citta: "))
for i in range(1,numero_città+1) :
    nome_citta = input(f"nome della città {i}° città:  ")
    abitanti = int(input("quanti abitanti che ci sono :  "))
    abitanti_attivi = int(input("quanti abitanti attivi ci sono :  "))
    
    
    
    indice_abitanti =abitanti_attivi /abitanti*100
    if indice == 0 :
        indice = indice_abitanti
    if indice_abitanti >= indice : 
        indice_max = indice_abitanti
        nome_max = nome_citta
    if indice_abitanti <= indice :
        indice_min= indice_abitanti
        nome_min= nome_citta
    
print(f"La città con il maggior indice di abitanti è {nome_max} con indice {indice_max}")
print(f"La città con il minor indice di abitanti è {nome_min} con indice {indice_min}")