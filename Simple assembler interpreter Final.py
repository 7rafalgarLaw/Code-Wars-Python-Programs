# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 16:36:12 2020

@author: simasurk
"""

def simple_assembler(program):
    register = dict()
    
    run_instructions(program, 0, len(program), register)
            
    return register

def run_instructions(program, start, end, register):
    '''
    Used to run instructions in a recursive way.
    '''
    skip_instructions = 0
    
    for i in range(start, end):
        
        if skip_instructions:
            skip_instructions -= 1
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
                    skip_instructions = offset - 1
            else:
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