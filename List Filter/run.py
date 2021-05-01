def filter_list(l):
    for x in l[:]:
        if(isinstance(x,str)):
            l.remove(x)
    return l