import math

#recur 
def recur(d, list_squares = list()):
    if d in (0, 1): 
        if d == 1: 
            list_squares.append(d)
        print(list_squares)
        return

    min_sqrt = math.floor(d**0.5)
    x = d - min_sqrt**2
    list_squares.append(min_sqrt)
    
    recur(x, list_squares)