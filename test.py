import pygame
pygame.init()
win = pygame.display.set_mode((800,800))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    img = pygame.image.load(".\\asset\\playagain.png")
    win.blit(img,(0,0))
    pygame.display.update()