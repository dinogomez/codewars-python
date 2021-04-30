import math
def comp(array1, array2): 
    print("unparsed Array 1:" + str(array1))
    print("unparsed Array 2:" + str(array2))
    if array1 is None or array2 is None:
        return False
    if(len(array1) == 0 and len(array2) == 0):
        return True
    elif(len(array1) == 0 or len(array2) == 0):
        return False
    counter = 0;
    for i in array1[:]:
        x = i*i
        print(i)
        print(x)
        if(x in array2):
            array2.remove(x)
            array1.remove(i)
        print(array1)
        print(array2)
    if(len(array1) and len(array2)):
        return False
    else:
        return True