import random
import string
class Word:
    key = ""
    isBomb = False
    speed = 0
    x = 0
    y = 0
    length = 0
    assistant = 1
    def __init__(self,speed,x,y,length,isBomb):
        self.speed = speed
        self.x = x
        self.y = y
        self.length = length
        for i in range(self.length):
            self.key = self.key + random.choice(string.ascii_uppercase)  
        if random.randrange(1,100) <= 20:
            isBomb = True
        
        print(self.isBomb)
        print(self.key)
        print(self.x)
        print(self.y)
        print(self.speed)
    def rand(self):
        self.assistant = 1
        self.key = ""
        for i in range(self.length):
            self.key = self.key + random.choice(string.ascii_uppercase)
        if random.randrange(1,100) <= 20:
            self.isBomb = True
        else:
            self.isBomb = False
        
    def move(self):
        self.y += self.speed
