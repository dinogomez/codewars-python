    def comp2(array1, array2):
        
        for x in array2:
            if x is None:
                return False
            y = math.sqrt(x)
            if((y) in array1):
                print(str(y) + ", exist in Array 1")
            else:
                return False
        return True
        
    
        
    # Parsing the first array    
    def comp1(array1, array2):
        for x in array1:     
            if x is None:
                return False
            y = x*x
            if((y) in array2):
                print(str(y) + ", exist in Array 2")
            else:
                return False
            
        return True  
               
    
    try:
        
        if(comp1(array1, array2) and comp2(array1, array2)):
            return True
        else:
            return False
    except:
        
        return False