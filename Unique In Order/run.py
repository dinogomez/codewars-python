def unique_in_order(iterable):
    if iterable is '':
        return []
    if isinstance(iterable,str):
        iterable = list(iterable)
    arr = [iterable[0]]
    for i in iterable:
        if i != arr[-1]:
            arr.append(i)            
    return arr
    