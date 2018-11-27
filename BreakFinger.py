import random
import string
import pygame
import Class_Word






width = 800
height = 700
blue = (147,179,151)
black = (0,0,0)
white = (255,255,255)
# Biến kiểm tra có chạy hay không
Finish = True


pygame.init()
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Break Finger")


clock = pygame.time.Clock()

# Hàm vẽ text
def drawText(text,x,y,color,size):
    font = pygame.font.Font(".\\font\\good times rg.ttf",size)
    font.set_bold(5)
    surface = font.render(text,False,color)
    win.blit(surface,(x,y))

# Hàm cập nhật level
def updateLevel(listOfWord,level,length,speed):
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
    pygame.mixer.music.load(".\\sound\\menu.mp3")
    pygame.mixer.music.set_endevent(pygame.USEREVENT)
    pygame.mixer.music.play()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Finish = True
                return
            # Load music
            elif event.type == pygame.USEREVENT:
                pygame.mixer.music.load(".\\sound\\menu.mp3")
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
        

# Play again menu
def playAgain():
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousePoint = pygame.mouse.get_pos()
                if mousePoint[1] >= 415 and mousePoint[1] <= 442:
                    # Nếu người dùng chọn Yes
                    if mousePoint[0] >= 201 and mousePoint[0] <= 292:
                        return True
                    # Nếu người dùng chọn No
                    elif mousePoint[0] >= 500 and mousePoint[0] <= 591:
                        return False


# Hàm Run chạy game
# return true nếu người chơi win hoặc muốn chơi lại
# return false nếu người chơi thoát game hoặc không muốn chơi lại
def Run(Finish):
    # Tọa độ của đường kẻ ngang
    yLine = height - 100
    # Ký tự gõn
    typeCharacter = None
    # Tốc độ của từ
    speed = [20,18,13,14,15]
    # Biến hit saw
    hitSaw = False
    # Biến gameover
    gameover = False
    # Link to Background
    linkBackground = ".\\asset\\backgroundtrue.png"
    # Chuỗi ký tự người dùng nhập vào
    type = ""
    #Sử dụng 2 biến về saw
    # Tọa độ của saw và hướng di chuyển từ trái sang phải
    xSaw = 0
    SawDirection = True 
    # Điểm của người chơi
    score = 0
    # Level của người chơi
    level = 1
    # Game Loop Sound
    linkSound = ".\\sound\\gameloop1.mp3"
    # Length độ dài ký tự
    length = 1
    # Khởi tạo cho level 1
    listOfWord = []
    for i in range(4):
        temp = Class_Word.Word(speed[level-1],(i+1)*width//5,0,length,False)
        listOfWord.append(temp)
    # Biến kiểm tra người chơi nhập đúng hay không
    typeTrue = False
    # Load music
    pygame.mixer.music.load(linkSound)
    pygame.mixer.music.set_endevent(pygame.USEREVENT)
    pygame.mixer.music.play()
    while Finish == False: 
        # Đưa chuỗi của người dùng nhập vào type
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False             
            elif event.type == pygame.USEREVENT:
                pygame.mixer.music.load(linkSound)
                pygame.mixer.music.play()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    linkBackground = ".\\asset\\backgroundtrue.png"
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
                    if (score == 500):
                        gameover = True
                        break
                    level += 1
                    length += 1
                    if (length > 3):
                        length = 3
                    updateLevel(listOfWord,level,length,speed) 
                    # Cập nhật lại sound 
                    if level > 3:
                        linkSound = ".\\sound\\gameloop2.mp3"
                    pygame.mixer.music.load(linkSound)
                    pygame.mixer.music.set_endevent(pygame.USEREVENT)
                    pygame.mixer.music.play()   
                #======================Kết thúc cập nhật level===================    
                item.y = 0
                item.rand()
                break
            # Nếu người chơi nhập sai
            else:
                typeTrue = False
                max = 58
                if level == 3:
                    max = 40
                elif level == 4:
                    max = 44
                elif level == 5:
                    max = 40
                if item.y >= yLine - max:
                    if item.isBomb == True:
                        score -= 2 + level / 2
                        if score < 0:
                            score = 0
                        item.y = 0
                        item.rand()
                    else:
                        hitSaw = True
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
        
        
        

        scoreAchieve = "SCORE: " + str(score)
        typingString = "TYPE: " + type
        levelText = "LEVEL: " + str(level)

        #==========================Gọi hàm vẽ======================#
        # Tạo hình nền
        if typeTrue == True:
            linkBackground = ".\\asset\\backgroundtrue.png"
        elif type != "" and len(type) == length:
            linkBackground = ".\\asset\\backgroundwrong.png"
        ingameImg = pygame.image.load(linkBackground)
        win.blit(ingameImg,(0,0))
        # Ve saw
        saw = pygame.image.load(".\\asset\\saw.png")
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
        # Vẽ gameover
        if gameover == True:
            gameover_img = pygame.image.load(".\\asset\\gameover.png")
            win.blit(gameover_img,(200,250))
        
        # Nếu có từ nào trúng phải Saw
        if hitSaw == True:
            playAgainWindow = pygame.image.load(".\\asset\\playagain.png")
            win.blit(playAgainWindow,(160,200))
        #==========================Kết thúc vẽ=======================#

        pygame.display.update()

        # Kiểm tra có phải là gameover hay không => Người chơi win
        if gameover == True:
            pygame.time.delay(3000)
            return True
        # Kiểm tra xem người chơi có để từ đụng phải Saw hay không
        if hitSaw == True:
            return playAgain()
        # Kiểm tra xem người chơi nhập đúng hay không
        if typeTrue == True:
            typeTrue = False
            type = ""
        clock.tick(60)
    return False

while True:
    Menu()
    if Run(Finish) == False:
        break