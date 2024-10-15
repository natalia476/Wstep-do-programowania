#len - dlugosc listy
#sum - dodaje wszystkie elementy z listy
#min - minimalny element listy
#max - maksymalny element listy
#append - dodaje pojedynczy element na koniec listy
#sort - sortuje rosnaco
#count - zlicza liczbe wystapien elementow w liscie
#index - indeks pierwszego wystapienia elementu
#reverse - ustawia odwrotnie liste
#remove - usuwa pierwsze wystapienie elementu
#pop - usuwa element na danej pozycji indeksu
#insert - wprowadza element na dana pozycje (pozycja, element)

lista1 = [5, 10, 15, 20, 25, 30]
lista1.append(35)
print(len(lista1))
print(lista1[1:4])
print(lista1[0:-2])
lista1.reverse()
print(lista1)
lista1.pop(3)
print(lista1)
print(max(lista1))
print(sum(lista1))
srednia = sum(lista1)/len(lista1)
print(srednia)











