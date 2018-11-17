import pygame
pygame.init()
display_width = 800
display_height = 800
image = pygame.image.load('character.png')
black = (0,0,0)
white = (255,255,255)
def img(x,y):
    gameDisplay.blit(image,(x,y))

x = (display_width * 0)
y = (display_height * 0)
x_change = 0
y_change = 0
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Break Finger")
clock = pygame.time.Clock()
crash = False

while not crash:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crash = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
            elif event.key == pygame.K_DOWN:
                y_change = 5
            elif event.key == pygame.K_UP:
                y_change = -5


    x += x_change
    y += y_change
    gameDisplay.fill((255,255,255)) 
    img(x,y)
    x_change = y_change = 0
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()