#Luis Mario Cervantes Ortz
#Uso de listas 2


def extraerPares(lista):
    listaP=[]
    for x in lista:
        if x % 2 == 0: #ver cuales son los pares
            listaP.append(x)
    return listaP


def intercambiarParejas(lista):
    listaPP=[]
    for x in range(1,len(lista),2):
        listaPP.append(lista[x])        #Regresar los valores de la posicion y a su posicion a la izquierda
        listaPP.append(lista[x-1])

    if len(lista) % 2 !=0:
        x=len(lista)-1
        listaPP.append(lista[x]) #entre corchetes el valor
    return listaPP


def extraerMayoresPrevio(lista):
    listaM=[]
    for x in range (1,len(lista)):
        if lista[x] > lista[x-1]: #Mostrar cuales son los valores previos
            listaM.append(lista[x])
    return listaM


def promediarCentro(lista):
    lista.sort()
    for x in range(0,len(lista)):
        if lista[x] == max(lista):
            lista.remove(max(lista)) #Remover el valor maximo
    for x in range(0, len(lista)):
        if lista[x] == min(lista): #remover el valor minimo
            lista.remove(min(lista))
            break
    if len(lista) >= 2:
        promedio = sum(lista) / len(lista) #haccer el promedio
    if len(lista) == 0:
        return 0
    return promedio


def intercambiarMM(lista):
    a=0
    for x in range(0,len(lista)):
        if lista[x] == max(lista):   #lista [un valor] te da la posicion de ese valor
            a=lista[x]
            lista[x]= min(lista)

    for x in range(0,len(lista)):
        if lista[x] ==min(lista):
            lista[x]=a #Cambiar la posicion
            break
    return lista


def calcularEstadistica(lista):
    listaE=[]
    if len(lista) >= 2:
        promedio= sum(lista)/len(lista) #Saber el promedio

        for x in range(0,len(lista)):
                listaE.append((lista[x] - promedio) ** 2) #agregarlo a una lista
        desviacion = ((((sum(listaE)) / (len(lista) - 1)) ** (1 / 2))) #usar la lista para calcular la suma de los valores
        return promedio , desviacion
    elif len(lista)==1:
        promedio = sum(lista) / len(lista)
        return promedio,0
    else:
        return (0,0)


def main():
    print("Problema 1. Regresa una lista con los valores de la lista original")
    lista1 = [1,2,3,2,4,60,5,8,3,22,44,55]
    print("La lista", lista1, "regresa", extraerPares(lista1))
    lista2 = []
    print("La lista", lista1, "regresa", extraerPares(lista2))
    lista3 =  [5,7,3]
    print("La lista", lista1, "regresa", extraerPares(lista3))
    print()
    print("Problema 2. Regresa una lista con valores cambiados mayores al previo")
    lista4 =  [1,2,3,2,4,60,5,8,3,22,44,55]
    print("La lista original", lista4, "regresa", extraerMayoresPrevio(lista4))
    lista5 =  [5,4,3,2]
    print("La lista original", lista5, "regresa", extraerMayoresPrevio(lista5))
    lista6 = []
    print("La lista original", lista6, "regresa", extraerMayoresPrevio(lista6))
    print()
    print("Problema 3. Regresa una lista con los valores en parejas y cambiados de posicion entre ellas")
    lista7 = [1,2,3,2,4,60,5,8,3,22,44,55]
    print("La lista", lista7, "regresa ", intercambiarParejas(lista7))
    lista8 =  [1,2,3]
    print("La lista", lista8, "regresa ", intercambiarParejas(lista8))
    lista9 = [7]
    print("La lista", lista9, "regresa", intercambiarParejas(lista9))
    print()
    print("Problema 4. Intercambiar los valores mayor y menor que hay en una lista ")
    lista10 = [5,9,3,22,19,31,10,7]
    print("La lista", lista10, "regresa", intercambiarMM(lista10))
    lista11 = [1,2,3]
    print("La lista", lista11, "regresa", intercambiarMM(lista11))
    lista12= [ ]
    print("La lista", lista12, "regresa", intercambiarMM(lista12))
    print()
    print("Problema 5. Calcular el promedio centro sin tomar en cuenta el mayor y menor de la lista")
    lista13 = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]
    print("La lista", lista13, "recibe", promediarCentro(lista13))
    lista14 = [5, 8]
    print("La lista", lista14, "recibe", promediarCentro(lista14))
    lista15 =  []
    print("La lista", lista15, "recibe", promediarCentro(lista15))
    print("Promblema 6.De una lista de valores regresar lo que es el promedio y la desviación estandar")
    lista16 =  [2,3]
    print("La lista", lista16, "regresa", calcularEstadistica(lista16))
    lista17 =  [95,21,73,24,15,69,71,80,49,100,85]
    print("La lista", lista17, "regresa", calcularEstadistica(lista17))
    lista18 = []
    print("La lista", lista18, "regresa", calcularEstadistica(lista18))
main()