import random
import string
import pygame
import Class_Word
listOfWord = []



typeCharacter = None
speed = [3,4,5,6,10]
length = 3
level = 1
width = 800
height = 700
blue = (147,179,151)
black = (0,0,0)
white = (255,255,255)
# Biến kiểm tra có chạy hay không
Finish = True
# Tọa độ của đường kẻ ngang
yLine = height - 100

# Tọa độ của saw và hướng di chuyển từ trái sang phải
xSaw = 0
SawDirection = True 
# Help Message
HelpMessage = "Hello!"
pygame.init()
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Break Finger")


# Khởi tạo cho level 1
for i in range(4):
    temp = Class_Word.Word(speed[level-1],(i+1)*width//5,0,length,False)
    listOfWord.append(temp)


clock = pygame.time.Clock()

# Hàm vẽ text
def drawText(text,x,y,color,size):
    font = pygame.font.Font("good times rg.ttf",size)
    font.set_bold(5)
    surface = font.render(text,False,color)
    win.blit(surface,(x,y))

# Hàm cập nhật level
def updateLevel(listOfWord,level,length):
    if length == 2:
        temp = length*70
    elif length == 3:
        temp = length*50
    for i in range(4):
        listOfWord[i] = Class_Word.Word(speed[level - 1],(i + 1) * width//4 - temp,0,length,False)

# Menu Help
def MenuHelp():
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePoint = pygame.mouse.get_pos()
                # Nếu người dùng click vào exit
                if (mousePoint[0] >= 715 and mousePoint[0] <= 785 and 
                    mousePoint[1] >= 29 and mousePoint[1] <= 85):
                    # pygame.quit()
                    return
        win.fill(black)
        menuHelp = pygame.image.load(".\\asset\\menu_help.png")
        win.blit(menuHelp,(0,0))
        pygame.display.update()




# Menu Credit
def MenuCredit():
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePoint = pygame.mouse.get_pos()
                # Nếu người dùng click vào exit
                if (mousePoint[0] >= 715 and mousePoint[0] <= 785 and 
                    mousePoint[1] >= 29 and mousePoint[1] <= 85):
                    # pygame.quit()
                    return
        win.fill(black)
        menuCredit = pygame.image.load(".\\asset\\menu_credit.png")
        win.blit(menuCredit,(0,0))
        pygame.display.update()




# Menu
def Menu():
    global Finish
    pygame.mixer.music.load(".\\asset\\menu.mp3")
    pygame.mixer.music.set_endevent(pygame.USEREVENT)
    pygame.mixer.music.play()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Finish = True
                return
            # Load music
            elif event.type == pygame.USEREVENT:
                pygame.mixer.music.load(".\\asset\\menu.mp3")
                pygame.mixer.music.play()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousePoint = pygame.mouse.get_pos()
                # Nếu người dùng click vào Start
                if mousePoint[0] >= 273 and mousePoint[0] <= 525:
                    if mousePoint[1] >= 284 and mousePoint[1] <= 356:
                        Finish = False
                        return
                # Nếu người dùng click vào Help
                    elif mousePoint[1] >= 400 and mousePoint[1] <= 472:
                        MenuHelp()
                # Nếu người dùng click vào Credits
                    elif mousePoint[1] >= 504 and mousePoint[1] <= 576:
                        MenuCredit()        
        img = pygame.image.load(".\\asset\\menu.png")
        win.blit(img,(0,0))
        pygame.display.update()
        

# Hàm Run chạy game
def Run(Finish):
    # Chuỗi ký tự người dùng nhập vào
    type = ""
    #Sử dụng 2 biến về saw
    global xSaw
    global SawDirection
    # Điểm của người chơi
    score = 0
    # Level của người chơi
    global level
    # Biến kiểm tra người chơi nhập đúng hay không
    typeTrue = False
    # Load music
    pygame.mixer.music.load(".\\asset\\gameloop1.mp3")
    pygame.mixer.music.set_endevent(pygame.USEREVENT)
    pygame.mixer.music.play()
    while Finish == False: 
        # Đưa chuỗi của người dùng nhập vào type
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.USEREVENT:
                pygame.mixer.music.load(".\\asset\\gameloop1.mp3")
                pygame.mixer.music.play()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    type = ""
                elif event.key >= 97 and event.key <= 122:
                    typeCharacter = chr(event.key)                
                    type += chr(event.key)
                    if len(type) == 10:
                        type = ""
                    else:
                        type = type.upper()
        
        
        

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
        
        # Cập nhật lại tọa độ các object để vẽ
        if SawDirection == True and xSaw + 80 < width:
            # Chia lấy phần nguyên cho số frame
            xSaw += 40
            if xSaw + 80 >= width:
                SawDirection = False
        elif SawDirection == False:
            xSaw -= 40
            if xSaw <= 0:
                SawDirection = True
        
        
        if Finish == True:
            break

        scoreAchieve = "SCORE: " + str(score)
        typingString = "TYPE: " + type
        levelText = "LEVEL: " + str(level)

        #==========================Gọi hàm vẽ======================#
        # Tạo hình nền
        ingameImg = pygame.image.load(".\\asset\\another.png")
        win.blit(ingameImg,(0,0))
        # Ve saw
        saw = pygame.image.load(".\\asset\\image18.png")
        win.blit(saw,(xSaw,height - 140))
        # Vẽ đường thẳng ngăn cách
        pygame.draw.line(win,(0,0,0),(0,height-100),(width,height-100),6)
        # Vẽ các từ
        for item in listOfWord:
            if item.isBomb == True:
                drawText(item.key,item.x,item.y,black,40)
            else:
                drawText(item.key,item.x,item.y,blue,40)
        drawText(scoreAchieve,width - 185,height - 50,black,20)
        drawText(typingString,width/2 - 150,height - 50,black,20)
        drawText(levelText,0,height - 50,black,20)
        #==========================Kết thúc vẽ=======================#

        pygame.display.update()
        # Kiểm tra xem người chơi nhập đúng hay không
        if typeTrue == True:
            typeTrue = False
            type = ""
        
        clock.tick(60)




Menu()
Run(Finish)