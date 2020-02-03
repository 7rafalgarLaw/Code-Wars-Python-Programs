from collections import Counter
import re 

//sample tests passed
def top_3_words(text):
    print('text : '+text)
    text = ''.join([x for x in text if x.isalpha() or x == "'" or x == ' '])
    print('removed special chars : '+text)
    
    text = [x for x in text.lower().split() if any([y.isalpha() for y in x])]
    print('only words : '+str(text))
    
    words_count = Counter(text)
    print(words_count.most_common(3))
    
    return [x for x, y in words_count.most_common(3)]
    
