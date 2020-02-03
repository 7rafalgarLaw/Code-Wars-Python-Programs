def components(grid):
    
    print(grid)
    print('Number of points (+) : '+str(len([x for x in grid if x == '+'])))
    print('Number of edges (| and --) : '+str(len([x for x in grid if x == '|']) + \
                                    len([x for x in grid if x == '-'])//2))
                                    
    #Use edges and vertices on graph to solve this problem.
    '''Graph
        edgeslist - [( (0,0)(1,0) ), ( (1,0)(2,0) ), ...]
        
    '''                                                                  
    #print('+ : '+str(len([x for x in grid if x == '  '])))