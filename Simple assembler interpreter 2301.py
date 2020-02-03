def simple_assembler(program):
    '''
	Needs to be optimized. Execution taking more than 12 seconds.
    '''
    print(program)
    #return
    register = dict()
    
    run_instructions(program, 0, len(program), register)
            
    #print(register)
    return register

def run_instructions(program, start, end, register):
    
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
            a  = instruction[1]
            offset = int(instruction[2])
            if register.get(a, None) or a.lstrip('-').isdigit():
                if offset < 0:
                    while register[a]:
                        run_instructions(program, i + offset, i, register)
                elif offset > 1:
                    skip_instructions = offset
            else:
                #print('skipped')
                continue
                                
def inc(register, a):
    register[a] += 1

def dec(register, a):
    register[a] -= 1

def mov(register, a, b):
    if b.isalpha():
        register[a] = register[b]
    else:
        register[a] = int(b)
        
#Test 
i = ['mov a 1', 'mov b 1', 'mov c 0', 'mov d 26', 'jnz c 2', 'jnz 1 5', 'mov c 7', 'inc d', 'dec c', 'jnz c -2', 'mov c a', 'inc a', 'dec b', 'jnz b -2', 'mov b c', 'dec d', 'jnz d -6', 'mov c 18', 'mov d 11', 'inc a', 'dec d', 'jnz d -2', 'dec c', 'jnz c -5']
simple_assembler(i)