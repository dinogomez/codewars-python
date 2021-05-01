def digital_root(n):
    if len(str(n)) == 1:
        return n
    else:
        n = [int(i) for i in str(n)]
        print(n)
        print("length: " + str(len(n)))
        while(len(n)>1):
            n = sum(n)
            n = [int(i) for i in str(n)]
        return n[0]