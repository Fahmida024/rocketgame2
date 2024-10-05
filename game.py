import pygame
import os
screen=pygame.display.set_mode((800,500))
playing=True
fp=60
VELOCITY=5
clock=pygame.time.Clock()
bgimage=pygame.image.load('background.png')
redimage=pygame.image.load('rocket1.png')
yellowimage=pygame.image.load('rocket2.png')
redimage1=pygame.transform.rotate(pygame.transform.scale(redimage,(50,50)),270)
yellowimage1=pygame.transform.rotate(pygame.transform.scale(yellowimage,(50,50)),90)

yellow=pygame.Rect(150,200,40,40)
red=pygame.Rect(600,200,40,40)

border=pygame.Rect(400,0,10,500)

maxbullets=3
bulletvelocity=7
def handle_bullets(yellowbullets,redbullets,yellow,red):
    for b in yellowbullets:
        b.x=b.x+bulletvelocity
    for b1 in redbullets:
        b1.x=b1.x-bulletvelocity
redbullets=[]
yellowbullets=[]
    
    

while playing:
    def redmove(keypressed,red):
        if keypressed[pygame.K_UP] and red.y>0 :
            red.y=red.y-5
        if keypressed[pygame.K_DOWN] and red.y<460:
            red.y=red.y+5
        if keypressed[pygame.K_LEFT] and red.x>400:
            red.x=red.x-5
        if keypressed[pygame.K_RIGHT] and red.x<760:
            red.x=red.x+5
    def yellowmove(keypressed,yellow):
        if keypressed[pygame.K_w] and yellow.y>0:
            yellow.y=yellow.y-5
        if keypressed[pygame.K_s] and yellow.y<460:
            yellow.y=yellow.y+5
        if keypressed[pygame.K_a] and yellow.x>0:
            yellow.x=yellow.x-5
        if keypressed[pygame.K_d] and yellow.x<360:
            yellow.x=yellow.x+5
    

    clock.tick(fp)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            playing=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_c:
                bullet=pygame.Rect(yellow.x,yellow.x,10,5)
                yellowbullets.append(bullet)
            if event.key==pygame.K_SPACE:
                bullet4=pygame.Rect(red.x,red.y,10,5)
                redbullets.append(bullet4)


    screen.fill('dark blue')
    screen.blit(yellowimage1,(yellow.x,yellow.y))
    screen.blit(redimage1,(red.x,red.y))
    pygame.draw.rect(screen,(19, 242, 213),border)
    keypressed=pygame.key.get_pressed()
    redmove(keypressed,red)
    yellowmove(keypressed,yellow)
    handle_bullets(yellowbullets,redbullets,yellow,red)
    for b in redbullets:
        pygame.draw.rect(screen,(79, 63, 20),b)
    for b in yellowbullets:
        pygame.draw.rect(screen,(79, 63, 20),b)
    pygame.display.update()





