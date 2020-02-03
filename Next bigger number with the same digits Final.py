def next_bigger(number):
    str_number = str(number)
    prev_number = '0'
    
    for i in range(len(str_number)-1, -1, -1):
        n = str_number[i]
        if n < prev_number:
            print(n)
            print(prev_number)
            sort_string = str_number[i+1:]
            print(sort_string)
            smallest_number = min(sort_string)
            print(smallest_number)
        #swap numbers
            print('sorted : '+''.join(sorted(str_number[i+1:])))
            
            result = str_number[:i] + smallest_number + ''.join(sorted(sort_string.replace(smallest_number, n)))
            print(result)
            return int(result)
        prev_number = n
        
    return -1