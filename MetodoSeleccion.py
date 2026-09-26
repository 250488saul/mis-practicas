lista = [4,2,6,8,5,7,8]
for i in range(len(lista)):
minimo= i
for X in range (i,len(lista)):
if lista [X] < lista[minimo]:
    minimo = X
    aux  = lista[i]
    lista[i] = lista[minimo]
    lista[minimo] = aux
    print(f"paso{i+1}: {lista}")


    print("resultado lista",lista)