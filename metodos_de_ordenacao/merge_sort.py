def merge_sort(lista, ini, fim):
    if fim - ini > 1: # se o tamanho for maior que 1
        meio = (fim + ini) // 2
        merge_sort(lista, ini, meio)
        merge_sort(lista, meio, fim)
        merge(lista, ini, meio, fim)

def merge(lista, ini, meio, fim):
    left = lista[ini:meio]
    right = lista[meio:fim]


    es = 0
    di = 0
    for k in range(ini, fim):
        if es >= len(left):
            lista[k] = right[di]
            di += 1

        elif di >= len(right):
            lista[k] = left[es]
            es += 1

        elif left[es] < right[di]:
            lista[k] = left[es]
            es += 1
        else:
            lista[k] = right[di]
            di += 1


lista = [10, 4, 2, 6, 8, 1, 11, 12, 3, 5, 7, 9]

merge_sort(lista, 0, len(lista))
print(lista)
