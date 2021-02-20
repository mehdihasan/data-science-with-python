import string
from collections import Counter

###
# Learning Objectives
# 1. Conditions and Branching
# 2. Loops
# 3. Functions
# 4. Objects and Classes
###


# While Loop Example

dates = [1982, 1980, 1973, 2000]

i = 0
year = dates[0]

while(year != 1973):    
    print(year)
    i = i + 1
    year = dates[i]
    

print("It took ", i ,"repetitions to get out of loop.")


class Rectangle(object):

    def __init__(self, color, height, width):
        super().__init__()
        self.height = height
        self.width = width
        self.color = color

    def getSize(self):
        return (self.height * self.width)


redRectangle = Rectangle("red", 2, 24)

print(redRectangle.color)
print(redRectangle.height)
print(redRectangle.width)
print(redRectangle.getSize())



class analysedText(object):
    
    def __init__ (self, text):
        self.text = text.lower()
        self.fmtText = self.text.translate(str.maketrans('', '', string.punctuation))
    
    def freqAll(self):        
        return Counter(self.fmtText.split())
    
    def freqOf(self,word):
        return Counter(self.fmtText.split())[word]


at = analysedText("This, is. the? TEXT!! is it? really is it?")
print(at.text)
print(at.fmtText)
print(at.freqAll())
print(at.freqOf('is'))



x=1

if(x!=1):
    print('Hello')
else:
    print('Hi')
print('Mike')


A=['1','2','3']
for a in A:
    print(2*a)


def Delta(x):
    if x==0:
        y=1;
    else:
        y=0;
    return(y)


print(Delta(0))

