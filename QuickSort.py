def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivo = array[0]
        menores = [i for i in array[1:] if i <= pivo]
        maiores = [i for i in array[1:] if i > pivo]
        return quick_sort(menores) + [pivo] + quick_sort(maiores)


print(quick_sort([10, 1, 1, 9, 100, 1, 2, 5, 78, 39, 65, 451, 2, 7, 3, 6, 1, 5, 7, 98, 69]))
