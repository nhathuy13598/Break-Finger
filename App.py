import random
import pyxel
import string
class App:
    lsLetter = [None]*16
    def __init__(self):
        pyxel.init(160,120,caption="Break Finger")
        self.iHealth = 100
        self.iBomb = 2
        self.iLetterLeft = 100
        self.iGoal = 100
        self.iLetterMissed = 0
        pyxel.run(self.update,self.draw)

    def update(self,iQuality):
        for i in range(16):
            
            self.lsLetter[0] = 


print(string.ascii_uppercase)