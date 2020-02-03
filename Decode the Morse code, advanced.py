def decodeBits(bits):
    ''' Accept 0's and 1's -> return dots, dashes and spaces
  '''
    bits = bits.strip('0')
    #transmission rate - Get the minimum length of consecutive 1's or 0's
    r = min([len(x) for x in bits.split('0') if x != ''] + [len(x) for x in bits.split('1') if x != ''])
    
    #Replace 0's and 1's with respect to the transmission rate
    return bits.replace('0000000'*r, '   ').replace('111'*r, '-').replace('000'*r, ' ').replace('1'*r, '.').replace('0'*r, '')
    
def decodeMorse(morseCode):
    ''' Accept dots, dashes and spaces -> return human-readable message
    '''    
    decoded_text = ''
    for word in (morseCode.strip()).split('   '):
        decoded_text += ''.join([MORSE_CODE[x] for x in word.split(' ')]) + ' '
        
    return decoded_text.rstrip()