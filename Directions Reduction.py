import ast, re

def dirReduc(arr):
    """
    Used array as a string to substitute directly opposite directions with nothing.
    """
    strarr = str(arr).replace(' ', '').replace(']', ',]')
    
    needlessEffort = "'NORTH','SOUTH',|'SOUTH','NORTH',|'EAST','WEST',|'WEST','EAST',"
        
    while (re.search(needlessEffort, strarr)): 
        strarr = re.sub(needlessEffort, '', strarr)
    else:
        return ast.literal_eval(strarr.replace(',]', ']'))