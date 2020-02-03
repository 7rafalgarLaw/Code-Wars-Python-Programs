def ifelifelse():
    """
    Multiline
    Comment
    """
    #print("Hello World") Single Line Comment
    flag = None
    if flag:
        print("Flag is 1")    
    elif flag==0:
        print("Flag is 0")
    else:
        print("Flag is defined NONE")
ifelifelse()


class TVShow:
    def __init__(self, name, genre, rating):
        self.name = name
        self.genre = genre
        self.rating = rating

    def printInfo(self):
        #print("%s is a show in %s genre. Having an IMDB rating of ") % (self.name, self.genre)
        print(self.name,"is a TV show in",self.genre, "genre. It has an IMDB rating of",self.rating)       
show1 = TVShow("Deathnote", "Detective", 9.0)
#show2 = TVShow("One Piece","Adventure", 10)
#show1.printInfo()
#show2.printInfo()
#print(repr(show1))

class String:
    #join()
    '''
    list1 = ['Siddhesh','Masurkar']
    s = '-'
    s = s.join(list1)
    print(''.join(list1))
    print(s)

    list2 = s.split("-")
    print(list2)
    '''

#map()
def calculateSquare(n):
  return n*n

numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
#print(result)

# converting map object to set
numbersSquare = set(result)
#print(numbersSquare)
# end
