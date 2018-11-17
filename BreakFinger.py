import random
import string
import pygame
import time
class Word:
    key = ""
    isBomb = False
    speed = 0
    x = None
    y = 0
    length = 0
    def __init__(self,speed = 0,x = 0,y = 0,length = 0,isBomb = False):
        self.speed = speed
        self.x = x
        self.y = y
        self.length = length
        for i in range(self.length):
            self.key = self.key + random.choice(string.ascii_uppercase)  
        if random.randrange(1,100) <= 20:
            isBomb = True
        
    def compare(self,type):
        if self.key == type:
            return True
        return False
    
    def out(self):
        print(self.isBomb)
        print(self.key)
        print(self.x)
        print(self.y)
        print(self.speed)
    def rand(self):
        self.key = ""
        for i in range(self.length):
            self.key = self.key + random.choice(string.ascii_uppercase)
        if random.randrange(1,100) <= 20:
            self.isBomb = True
        else:
            self.isBomb = False
        
    def move(self):
        self.y += self.speed

listOfWord = []
typeTrue = False
type = ""
score = 0
speed = [8,10,13,15,20]
length = 1
level = 1
width = 800
height = 700
black = (0,0,0)
white = (255,255,255)
# Tọa độ của đường kẻ ngang
yLine = height - 100
pygame.init()
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Break Finger")

for i in range(5):
    temp = Word(speed[level-1],(i+1)*width//5,0,length)
    listOfWord.append(temp)


clock = pygame.time.Clock()
def drawText(text,x,y,color,size):
    font = pygame.font.SysFont("",size,1)
    surface = font.render(text,False,color)
    win.blit(surface,(x,y))
    
while 1:
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                type = ""
            elif event.key >= 97 and event.key <= 122:
                # Kiểm tra xem người chơi nhập đúng hay không
                if typeTrue == True:
                    typeTrue = False
                    type = ""
                type += chr(event.key)
                if len(type) == 10:
                    type = ""
                else:
                    type = type.upper()
    
    
    win.fill((238,221,130))
    # Vẽ đường thẳng ngăn cách
    pygame.draw.line(win,(0,0,0),(0,height-100),(width,height-100),2)
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Kiểm tra các từ trong listOfWord có qua height
    # Nếu qua thì cập nhật lại y và random lại
    for item in listOfWord:
        # Nếu người dùng nhập đúng
        if item.key == type:
            typeTrue = True
            score += 1
            item.y = 0
            item.rand()
        # Nếu người chơi nhập sai
        else:
            if item.y > yLine - 40:
                if item.isBomb == True:
                    score -= 2
                    if score < 0:
                        score = 0
                    item.y = 0
                    item.rand()
                else:
                    # Thua nhưng tạm thời để như thế này
                    item.y = 0
                    item.rand()
            else:
                item.move()

        if item.isBomb == True:
            drawText(item.key,item.x,item.y,black,60)
        else:
            drawText(item.key,item.x,item.y,white,60)
        
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    scoreAchieve = "SCORE: " + str(score)
    typingString = "TYPE: " + type
    drawText(scoreAchieve,width - 185,height - 50,black,40)
    drawText(typingString,width/2 - 150,height - 50,black,40)
    pygame.display.update()

    
    clock.tick(30)


    