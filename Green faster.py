#This is accurate but takes a lot of time to compute.
def green(n):

    dict_7 = {1:1, 2:5, 3:6, 4:25, 5:76, 6:376, 7:625}

    if n in dict_7:
        return dict_7[n]

    num1 = '376'
    num2 = '625'
    n1 = 7
    while n1 != n+1:
        z=''
        numFound = False
        if int(num1)<int(num2):
            while not numFound:
                for i in range(1,10):
                    num = str(i) + z + num1
                    if str(int(num)**2).endswith(num):
                        num1 = num
                        n1 += 1
                        print(n1)
                        numFound = True
                        break
                if numFound == False:
                    z += '0'
        else:
            while not numFound:
                for i in range(1,10):    
                    num = str(i) + z + num2
                    if str(int(num)**2).endswith(num):
                        num2 = num
                        n1 += 1
                        print(n1)
                        numFound = True
                        break
                if numFound == False:
                    z += '0'
    else:
        return int(num1) if int(num1)<int(num2) else int(num2)
        
    #n+1.Just to make sure we get the lowest green number. Hence sorting.
    #if len(list_values) >= n+5:  
    #print(list_values)
    #return sorted(list_values)[n-1]
        
green(13)
