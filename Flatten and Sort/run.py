def flatten_and_sort(array):
    array2 = []
    if not array:
        return []
    for i in array[:]:
        if i is None:
            array.remove(i)
        else:
            i.sort()
            for j in i:
                array2.append(j)
    array2.sort()
    return array2