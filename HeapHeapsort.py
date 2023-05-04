#HEAP

def Heap (lista):

    for i in range (1,len(lista)):
   
        Padre = (i-1)//2
        nuevaLlave = lista[i]

        while i>0 and lista[Padre] < nuevaLlave:

            lista[i] = lista[Padre]           
            i = Padre
            Padre = (i-1)//2

        lista[i] = nuevaLlave


    print (f"El valor del heap creado es de {lista}")
    return lista
 



def heapsort(lst):

    heap = Heap(lst)
    n = len(heap)

    for i in range(n-1, 0, -1):

        heap[0], heap[i] = heap[i], heap[0] #Intercambia la primera posicion a la ultima posicion
        j = 0

        while True:

            left = 2 * j + 1        #Saca las posiciones salientes de cada padre
            right = 2 * j + 2

            if left < i and heap[left] > heap[j]:
                largest = left
                                                                #largest define si left es mas grande que right y viceversa
            else:
                largest = j

            if right < i and heap[right] > heap[largest]:
                largest = right

            if largest != j:
                heap[j], heap[largest] = heap[largest], heap[j]
                j = largest

            else:
                break
            
    print (heap)


