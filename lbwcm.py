import pygame
import time

pygame.init()

font = pygame.font.SysFont(None, 50)
pygame.display.set_caption("Linux Background With Circle Movement System")
def text(msg, color):
 mesg = font.render(msg, True, color)
 screen.blit(mesg, (0, 450))
screen = pygame.display.set_mode((750,500))
background = pygame.image.load('images.jpg')
circleimg = pygame.image.load('ok.png').convert()
x = 100
y = 250
clock = pygame.time.Clock()
running = True
while(running):
    clock.tick(60)
    keys = pygame.key.get_pressed()
    screen.fill((0, 0, 0))
    transformwidth = pygame.transform.scale(background, (1000, 1000))
    screen.blit(background, (300, 200))
    screen.blit(transformwidth, (0, 0))
    screen.blit(circleimg, (y, x))
    text("W,A,S,D To Move", (0,255,0))
    pygame.display.flip()
    for event in pygame.event.get():
        if keys[pygame.K_d]:
           y += 30
        elif keys[pygame.K_a]:
           y -= 30
        elif keys[pygame.K_s]:
           x += 30
        elif keys[pygame.K_w]:
           x -= 30
        if event.type == pygame.QUIT:
          running = False

pygame.quit()