import random
import string
import pygame
import time
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

listOfWord = []
typeTrue = False
type = ""
score = 0
typeCharacter = None
speed = [3,4,5,6,8]
#speed = [1,2,3,4,5]
length = 1
level = 1
width = 800
height = 800
black = (0,0,0)
white = (255,255,255)
# Tọa độ của đường kẻ ngang
yLine = height - 100
pygame.init()
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Break Finger")

for i in range(4):
    temp = Word(speed[level-1],(i+1)*width//5,0,length,False)
    listOfWord.append(temp)


clock = pygame.time.Clock()
def drawText(text,x,y,color,size):
    #font = pygame.font.SysFont("",size,1)
    font = pygame.font.Font("good times rg.ttf",size)
    font.set_bold(2)
    surface = font.render(text,False,color)
    win.blit(surface,(x,y))

def updateLevel(listOfWord,level,length):
    if length == 2:
        temp = length*70
    elif length == 3:
        temp = length*50
    for i in range(4):
        listOfWord[i] = Word(speed[level - 1],(i + 1) * width//4 - temp,0,length,False)

Finish = False
while not Finish: 

    # Đưa chuỗi của người dùng nhập vào type
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                type = ""
            elif event.key >= 97 and event.key <= 122:
                typeCharacter = chr(event.key)                
                type += chr(event.key)
                if len(type) == 10:
                    type = ""
                else:
                    type = type.upper()
    
    # Tô màu nền
    win.fill((238,221,130))

    # Vẽ đường thẳng ngăn cách
    pygame.draw.line(win,(0,0,0),(0,height-100),(width,height-100),6)


    # Duyệt so sánh type với các từ có trong danh sách
    for item in listOfWord:
        # Nếu người dùng nhập đúng
        if item.key == type:
            typeTrue = True
            score += 1       
            #======================Cập nhật level===================
            if score % 100 == 0:
                # Nếu đạt 600 điểm thì dừng game và chúc mừng người chơi
                if (score == 600):
                    print("Bạn đã hoàn thành trò chơi")
                    Finish = True
                    break
                level += 1
                length += 1
                if (length > 3):
                    length = 3
                updateLevel(listOfWord,level,length)           
            #======================Cập nhật level===================    
            item.y = 0
            item.rand()
        # Nếu người dùng nhập có ký tự thuộc trong chuỗi, mỗi chuỗi được sử dụng quyền này
        # assistant lần
        elif item.assistant != 0 and item.key.find(type) == 0 and type != "":
            item.assistant -= 1
            item.y -= item.speed
        # Nếu người chơi nhập sai
        else:
            if item.y > yLine - 60:
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
            drawText(item.key,item.x,item.y,black,40)
        else:
            drawText(item.key,item.x,item.y,white,40)

    if Finish == True:
        break

    scoreAchieve = "SCORE: " + str(score)
    typingString = "TYPE: " + type
    levelText = "LEVEL: " + str(level)
    drawText(scoreAchieve,width - 185,height - 50,black,20)
    drawText(typingString,width/2 - 150,height - 50,black,20)
    drawText(levelText,0,height - 50,black,20)
    pygame.display.update()
    # Kiểm tra xem người chơi nhập đúng hay không
    if typeTrue == True:
        typeTrue = False
        type = ""
    
    clock.tick(60)


    