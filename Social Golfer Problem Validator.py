def valid(solution):
    """
    Check if the list of lists provided is valid.
    """
    rows = len(solution)
    columns = len(solution[0])
    sizeofgroup = len(solution[0][0])

    #Check if player plays once a day and the number of groups played each day is same.
    for row in solution:
        golfers = [l for x in row for l in x]
        if len(golfers) != len(set(golfers)) or len(row) != columns:
            return False
            
    #Check if the groups are unique.
    for row in solution:
        if solution.index(row) == rows-1:
            pass
        for x in row:
            if sizeofgroup != len(x) or len(set(x).difference(set(golfers)))>0:
                return False
            for i in range(solution.index(row)+1, rows):
                for j in range(columns):
                    if len(set(x).intersection(set(solution[i][j]))) > 1:
                        return False
    
    return True
        
