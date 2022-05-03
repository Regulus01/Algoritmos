def busca_menor(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice


def selection_sort(arr):
    novo_arr = []
    for i in range(len(arr)):
        menor = busca_menor(arr)
        novo_arr.append(arr.pop(menor))
    return novo_arr


lista = [5, 3, 6, 2, 10, 1, 40, 150, 70, 20, 30, 2, 5]
lista = selection_sort(lista)
print(lista)

