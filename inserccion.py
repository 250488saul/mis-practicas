lista = [4,2,6,8,5,7,0]
for i in range (i,len(lista)):
    aux = lista[i]
    j= i-1
    while j>=0 and aux<lista[i]:
        lista[j+1]=lista[j]
        lista[j]=aux
        j-=1
        print(lista)
