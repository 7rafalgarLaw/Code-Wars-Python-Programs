#import pdb

def simple_assembler(program):
    '''
	Needs to be optimized. Execution taking more than 12 seconds.
    '''
    print(program)
    #return
    register = dict()
		
    run_instructions(program, 0, len(program), register)
            
    print('Executed : '+str(register))
    return register

def run_instructions(program, start, end, register):
    
    #Logging
    #if register.get('a', None) == 100:
    #    return
    
    skip_instructions = 0
    
    for i in range(start, end):
        #print(i)
        
        if skip_instructions:
            skip_instructions -= 1
            #print('skipped')
            continue
        
        instruction = program[i].split()

        if instruction[0] == 'mov':
            mov(register, instruction[1], instruction[2])
        elif instruction[0] == 'inc':  
            inc(register, instruction[1])
        elif instruction[0] == 'dec':
            dec(register, instruction[1])
        # jnz
        else:
            #pdb.set_trace();
            a  = instruction[1]
            offset = int(instruction[2])
            if register.get(a, None) or a.lstrip('-').isdigit():
                if offset < 0:
                    while register[a]:
                        run_instructions(program, i + offset, i, register)
                elif offset > 1:
                    skip_instructions = offset - 1 #fix
            else:
                #print('skipped')
                continue
                                
def inc(register, a):
    print('inc '+a)
    register[a] += 1
    print(register)

def dec(register, a):
    print('dec '+a)
    register[a] -= 1
    print(register)

def mov(register, a, b):
    print('mov '+b+' to '+a)
    if b.isalpha():
        register[a] = register[b]
    else:
        register[a] = int(b)
    print(register)
		
		
#Codewars - Execution took more than 12 seconds.	
all_programs = '''\
['mov a 5', 'inc a', 'dec a', 'dec a', 'jnz a -1', 'inc a']
['mov a -10', 'mov b a', 'inc a', 'dec b', 'jnz a -2']
['mov a 1', 'mov b 1', 'mov c 0', 'mov d 26', 'jnz c 2', 'jnz 1 5', 'mov c 7', 'inc d', 'dec c', 'jnz c -2', 'mov c a', 'inc a', 'dec b', 'jnz b -2', 'mov b c', 'dec d', 'jnz d -6', 'mov c 18', 'mov d 11', 'inc a', 'dec d', 'jnz d -2', 'dec c', 'jnz c -5']
['mov d 100', 'dec d', 'mov b d', 'jnz b -2', 'inc d', 'mov a d', 'jnz 5 10', 'mov c a']
['mov c 12', 'mov b 0', 'mov a 200', 'dec a', 'inc b', 'jnz a -2', 'dec c', 'mov a b', 'jnz c -5', 'jnz 0 1', 'mov c a']
['mov i 35', 'mov n 31', 'mov a 40', 'mov h 35', 'mov z 0', 'jnz z 5', 'jnz i 3', 'dec i', 'dec i', 'dec i', 'inc i', 'inc n', 'inc n', 'inc n', 'inc a', 'inc a', 'inc h', 'inc h']
['mov q 24', 'mov o 23', 'mov b 22', 'mov a 35', 'mov e 40', 'mov z 0', 'jnz z 4', 'jnz q 3', 'dec q', 'dec q', 'inc q', 'inc q', 'dec o', 'inc o', 'inc b', 'inc b', 'inc a', 'dec a', 'inc a', 'inc a', 'inc e', 'inc e', 'dec e', 'dec e']
['mov c 23', 'mov g 20', 'mov u 29', 'mov o 37', 'mov q 25', 'mov a 28', 'mov z 2', 'jnz z 4', 'jnz c 2', 'dec c', 'inc c', 'dec c', 'dec c', 'inc g', 'dec g', 'inc g', 'inc u', 'dec u', 'inc u', 'inc u', 'inc u', 'dec o', 'inc o', 'inc o', 'inc o', 'inc o', 'dec q', 'inc q', 'inc q', 'inc q', 'dec q', 'inc a', 'inc a', 'dec a', 'dec a']
['mov i 32', 'mov u 30', 'mov z 2', 'jnz z 5', 'jnz i 3', 'inc i', 'inc i', 'inc i', 'dec i', 'inc u', 'dec u', 'inc u', 'inc u', 'inc u']
['mov i 38', 'mov h 37', 'mov a 39', 'mov z 2', 'jnz z 3', 'jnz i 2', 'inc i', 'inc i', 'dec i', 'inc i', 'inc h', 'inc h', 'inc h', 'dec a', 'dec a', 'inc a']
['mov b 38', 'mov e 25', 'mov g 24', 'mov z 0', 'jnz z 5', 'jnz b 5', 'inc b', 'inc b', 'inc e', 'dec e', 'inc e', 'inc e', 'inc g', 'inc g', 'inc g']
['mov i 20', 'mov h 22', 'mov a 31', 'mov d 22', 'mov c 21', 'mov q 22', 'mov z 2', 'jnz z 3', 'jnz i 3', 'dec i', 'dec i', 'inc i', 'dec i', 'inc i', 'dec h', 'dec h', 'dec h', 'inc h', 'inc a', 'inc a', 'inc a', 'inc a', 'inc a', 'dec d', 'dec d', 'inc c', 'inc c', 'inc c', 'dec c', 'dec c', 'dec q', 'dec q']
['mov g 27', 'mov h 24', 'mov k 34', 'mov q 24', 'mov a 25', 'mov z 1', 'jnz z 3', 'jnz g 2', 'inc g', 'inc g', 'inc h', 'dec h', 'inc k', 'inc k', 'inc q', 'inc q', 'inc q', 'inc q', 'inc a', 'inc a', 'inc a']
['mov s 37', 'mov q 39', 'mov g 29', 'mov a 29', 'mov i 29', 'mov z 2', 'jnz z 4', 'jnz s 3', 'inc s', 'inc s', 'inc s', 'dec q', 'dec q', 'inc q', 'inc g', 'dec g', 'inc g', 'inc g', 'dec a', 'inc a', 'inc i', 'inc i']
['mov g 34', 'mov s 32', 'mov z 2', 'jnz z 5', 'jnz g 3', 'inc g', 'dec g', 'dec g', 'inc s', 'inc s', 'inc s', 'inc s', 'inc s']
['mov h 33', 'mov e 20', 'mov q 37', 'mov z 0', 'jnz z 5', 'jnz h 5', 'inc h', 'dec h', 'inc h', 'dec e', 'inc e', 'inc e', 'inc e', 'inc e', 'inc q', 'inc q', 'inc q', 'inc q']
['mov i 27', 'mov o 36', 'mov h 21', 'mov d 26', 'mov q 24', 'mov m 20', 'mov z 0', 'jnz z 3', 'jnz i 2', 'dec i', 'dec i', 'inc i', 'inc i', 'inc o', 'inc o', 'dec o', 'dec o', 'inc o', 'inc h', 'inc h', 'dec h', 'inc d', 'inc d', 'dec d', 'dec d', 'dec q', 'inc q', 'inc q', 'dec m', 'inc m', 'inc m']
['mov q 24', 'mov i 39', 'mov b 22', 'mov c 22', 'mov z 0', 'jnz z 3', 'jnz q 4', 'inc q', 'dec q', 'dec q', 'dec q', 'inc q', 'inc i', 'inc i', 'inc b', 'dec b', 'dec b', 'inc b', 'inc c', 'inc c', 'inc c', 'inc c', 'inc c']
['mov o 22', 'mov u 23', 'mov d 39', 'mov s 22', 'mov i 22', 'mov h 30', 'mov z 0', 'jnz z 3', 'jnz o 3', 'inc o', 'inc o', 'inc o', 'inc u', 'dec u', 'inc u', 'dec d', 'dec d', 'inc s', 'inc s', 'dec s', 'dec i', 'inc i', 'dec i', 'inc i', 'dec h', 'inc h', 'inc h', 'dec h']
['mov g 32', 'mov e 37', 'mov h 40', 'mov z 0', 'jnz z 3', 'jnz g 2', 'dec g', 'inc g', 'inc g', 'inc g', 'inc e', 'dec e', 'inc e', 'inc e', 'inc e', 'dec h', 'inc h']
['mov m 40', 'mov d 23', 'mov h 22', 'mov a 24', 'mov z 0', 'jnz z 2', 'jnz m 4', 'dec m', 'dec m', 'dec m', 'inc m', 'dec m', 'dec d', 'inc d', 'inc d', 'inc d', 'inc h', 'dec h', 'dec h', 'inc a', 'inc a', 'inc a', 'dec a']
['mov a 20', 'mov q 31', 'mov m 29', 'mov o 38', 'mov h 25', 'mov z 1', 'jnz z 3', 'jnz a 4', 'inc a', 'inc a', 'inc a', 'dec q', 'inc q', 'inc q', 'inc q', 'inc q', 'inc m', 'dec m', 'inc m', 'inc m', 'inc m', 'inc o', 'inc o', 'inc o', 'inc h', 'dec h', 'inc h', 'inc h']
['mov b 24', 'mov t 36', 'mov u 37', 'mov z 0', 'jnz z 2', 'jnz b 4', 'inc b', 'inc b', 'inc t', 'inc t', 'inc t', 'inc u', 'inc u', 'dec u', 'dec u']
['mov g 34', 'mov m 40', 'mov z 1', 'jnz z 4', 'jnz g 3', 'inc g', 'inc g', 'dec m', 'dec m', 'inc m']
['mov m 29', 'mov i 23', 'mov u 23', 'mov z 1', 'jnz z 5', 'jnz m 3', 'inc m', 'inc m', 'inc m', 'inc m', 'inc m', 'inc i', 'dec i', 'dec i', 'inc u', 'inc u', 'inc u', 'inc u']
['mov n 25', 'mov u 22', 'mov q 27', 'mov a 40', 'mov s 27', 'mov i 24', 'mov z 1', 'jnz z 2', 'jnz n 4', 'dec n', 'inc n', 'inc n', 'inc u', 'inc u', 'inc u', 'inc u', 'inc q', 'dec q', 'inc a', 'dec a', 'inc a', 'inc a', 'inc s', 'inc s', 'inc i', 'dec i', 'inc i', 'inc i']
['mov q 32', 'mov k 35', 'mov z 0', 'jnz z 5', 'jnz q 3', 'inc q', 'inc q', 'dec q', 'inc q', 'inc k', 'dec k']
['mov o 24', 'mov g 30', 'mov q 31', 'mov c 38', 'mov z 0', 'jnz z 2', 'jnz o 5', 'inc o', 'inc o', 'dec o', 'inc o', 'dec o', 'inc g', 'dec g', 'dec g', 'inc g', 'inc q', 'dec q', 'dec q', 'inc q', 'dec q', 'inc c', 'dec c', 'inc c', 'dec c', 'inc c']
['mov q 22', 'mov h 30', 'mov b 25', 'mov m 21', 'mov g 24', 'mov z 1', 'jnz z 4', 'jnz q 5', 'inc q', 'inc q', 'dec h', 'inc h', 'inc b', 'dec b', 'inc b', 'dec b', 'inc m', 'dec m', 'inc m', 'dec g', 'dec g', 'inc g', 'dec g', 'dec g']
['mov n 35', 'mov g 27', 'mov c 37', 'mov b 40', 'mov z 2', 'jnz z 3', 'jnz n 4', 'inc n', 'inc n', 'inc g', 'inc g', 'dec c', 'inc c', 'inc c', 'dec c', 'inc c', 'inc b', 'inc b', 'inc b']
['mov d 26', 'mov k 39', 'mov z 2', 'jnz z 3', 'jnz d 2', 'inc d', 'dec d', 'inc d', 'inc d', 'inc k', 'dec k', 'inc k']
['mov s 35', 'mov d 24', 'mov m 34', 'mov e 37', 'mov z 2', 'jnz z 4', 'jnz s 5', 'dec s', 'inc s', 'inc s', 'inc d', 'inc d', 'inc d', 'inc d', 'inc m', 'dec m', 'dec m', 'dec e', 'inc e']
['mov t 38', 'mov c 32', 'mov k 39', 'mov g 34', 'mov s 22', 'mov i 22', 'mov z 1', 'jnz z 3', 'jnz t 4', 'inc t', 'inc t', 'inc t', 'dec t', 'inc t', 'inc c', 'dec c', 'inc c', 'inc k', 'dec k', 'inc g', 'dec g', 'inc s', 'inc s', 'inc i', 'dec i', 'inc i', 'dec i', 'inc i']
['mov h 37', 'mov o 28', 'mov t 30', 'mov a 37', 'mov d 21', 'mov z 0', 'jnz z 3', 'jnz h 3', 'inc h', 'inc h', 'inc h', 'inc h', 'inc h', 'inc o', 'inc o', 'inc t', 'dec t', 'dec t', 'inc t', 'dec a', 'inc a', 'dec a', 'inc a', 'inc d', 'inc d', 'dec d']
['mov a 39', 'mov i 27', 'mov b 31', 'mov u 36', 'mov h 24', 'mov e 28', 'mov z 0', 'jnz z 5', 'jnz a 2', 'inc a', 'inc a', 'inc a', 'inc a', 'dec i', 'inc i', 'inc i', 'dec b', 'dec b', 'inc b', 'inc b', 'inc b', 'dec u', 'dec u', 'dec u', 'inc u', 'dec u', 'inc h', 'dec h', 'inc h', 'inc e', 'dec e', 'dec e', 'dec e', 'inc e']
['mov g 26', 'mov b 25', 'mov c 31', 'mov q 39', 'mov k 40', 'mov z 0', 'jnz z 4', 'jnz g 5', 'inc g', 'inc g', 'dec b', 'inc b', 'inc c', 'inc c', 'dec c', 'inc c', 'inc c', 'inc q', 'inc q', 'dec k', 'inc k', 'dec k', 'inc k']
['mov c 40', 'mov q 37', 'mov t 32', 'mov n 39', 'mov o 23', 'mov u 27', 'mov z 2', 'jnz z 2', 'jnz c 2', 'dec c', 'dec c', 'inc c', 'inc c', 'inc q', 'inc q', 'inc q', 'dec t', 'inc t', 'inc n', 'dec n', 'inc n', 'inc n', 'dec o', 'inc o', 'dec o', 'inc o', 'dec u', 'dec u', 'inc u', 'inc u', 'inc u']
['mov g 29', 'mov i 40', 'mov z 1', 'jnz z 5', 'jnz g 4', 'dec g', 'dec g', 'inc g', 'inc i', 'inc i', 'inc i']
['mov h 24', 'mov a 21', 'mov t 38', 'mov m 32', 'mov n 35', 'mov z 2', 'jnz z 3', 'jnz h 5', 'dec h', 'dec h', 'inc h', 'inc h', 'inc a', 'inc a', 'inc a', 'dec t', 'dec t', 'inc t', 'inc t', 'dec m', 'inc m', 'dec m', 'inc m', 'inc m', 'inc n', 'inc n']
['mov o 32', 'mov q 22', 'mov d 35', 'mov s 34', 'mov i 26', 'mov n 33', 'mov z 1', 'jnz z 5', 'jnz o 3', 'dec o', 'inc o', 'inc o', 'inc o', 'inc q', 'inc q', 'inc q', 'inc q', 'inc d', 'dec d', 'inc d', 'dec s', 'inc s', 'dec s', 'inc s', 'dec i', 'inc i', 'dec i', 'inc i', 'dec i', 'inc n', 'dec n', 'dec n', 'inc n']
 '''
  

#import ast

# Run above programs
#for x in all_programs.splitlines():
#    simple_assembler(ast.literal_eval(x))
    
#Issue in 3rd
i = ['mov a 1', 'mov b 1', 'mov c 0', 'mov d 26', 'jnz c 2', 'jnz 1 5', 'mov c 7', 'inc d', 'dec c', 'jnz c -2', 'mov c a', 'inc a', 'dec b', 'jnz b -2', 'mov b c', 'dec d', 'jnz d -6', 'mov c 18', 'mov d 11', 'inc a', 'dec d', 'jnz d -2', 'dec c', 'jnz c -5']
simple_assembler(i)