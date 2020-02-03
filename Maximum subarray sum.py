def maxSequence(arr):
    if arr:
        #Check if all are positive
        if all([x > 0 for x in arr]):
            return sum(arr)
        #Check if all are negative
        if all([x < 0 for x in arr]):
            return 0
            
        maxsum = 0
        la = len(arr)
        for i in range(la):
            for j in range(i+1, la):
                sumofsubarray = sum(arr[i:j+1])
                if sumofsubarray > maxsum:
                    maxsum = sumofsubarray
        return maxsum
        
    else:
        return 0            
		
		
		
		
		
		
Solution @codewars
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
def maxSequence(arr):
    max,curr=0,0
    for x in arr:
        curr+=x
        if curr<0:curr=0
        if curr>max:max=curr
    return max
maxSequence(arr)