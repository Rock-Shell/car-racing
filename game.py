import pygame
import time
import random

pygame.init() #initialises pygame
display_width=1000#width of game window
display_height=800#height of gfame window

gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
dgreen=(0,200,0)
dred=(200,0,0)


clock = pygame.time.Clock()
carImg=pygame.image.load('car.jpg')

def car(x,y):
    gameDisplay.blit(carImg,(x,y))
  
def text_objects(text,font):#3RD
    textSurface=font.render(text,True,black)
    return textSurface,textSurface.get_rect()

def message_display(text):#2ND
    largeText=pygame.font.Font("freesansbold.ttf",115)#creates new file object
    textSurf,textRect=text_objects(text,largeText)
    textRect.center=((display_width/2),(display_height/2))
    gameDisplay.blit(textSurf,textRect)

    pygame.display.update()
    time.sleep(1)
    game_intro()
    
    
def crash():# READ 1ST
    message_display("you crashed")

def things(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])

def things_dodged(count):
    font=pygame.font.SysFont(None,25)
    text=font.render("Dodged :"+str(count),True,black)
    gameDisplay.blit(text,(0,0))

def buttons(msg,x,y,w,h,ic,ac,action=None):
    
    mouse=pygame.mouse.get_pos() #gives pointer location
    click=pygame.mouse.get_pressed()
    #print(click)
        
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))
        if click[0]==1 and action!=None:
            action()
##            if action=='play':
##                game_loop()
##            elif action=='quit':
##                pygame.quit()
##                quit()
        
            
    else:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))

    smallText=pygame.font.Font('freesansbold.ttf',20)
    textSurf,textRect=text_objects(msg,smallText)
    textRect.center=((x+(w/2)),(y+(h/2)))
    gameDisplay.blit(textSurf,textRect)

    
def quitgame():
    pygame.quit()
    quit()
def game_intro():
    intro=True
    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            
        gameDisplay.fill(white)     

        largeText=pygame.font.Font("freesansbold.ttf",115)
        textSurf,textRect=text_objects("Dodge if u can",largeText)
        textRect.center=((display_width/2),(display_height/2))
        gameDisplay.blit(textSurf,textRect)

        buttons('Go!',150,450,100,50,dgreen,green,game_loop)
        buttons('Quit',550,450,100,50,dred,red,quitgame)

        pygame.display.update()
        clock.tick(90)

#def pause():
    
   
def game_loop():
    x=int((display_width*0.35))
    y=int((display_height* 0.5))
    gameExit=False
    xc=0
    yc=0

    thingx=random.randrange(0,display_width-250)
    thingy=-600
    thingw=100
    thingh=100
    thing_speed=5

    dodged=0
    
    while not gameExit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

        ################################
                
            if event.type==pygame.KEYDOWN :
                if event.key==pygame.K_LEFT:
                    xc=-10
                elif event.key==pygame.K_RIGHT:
                    xc=+10
                elif event.key==pygame.K_UP:
                    yc=-5
                    
                elif event.key==pygame.K_DOWN:
                    yc=+5
                

            elif event.type==pygame.KEYUP:
                xc=0
                yc=0

        x+=xc
        y+=yc

        gameDisplay.fill(white)
        ####for blocks
        #things(thingx,thingy,thingw,thingh,color):
        things(thingx,thingy,thingw,thingh,red)
        thingy+=thing_speed
        ############
        car(x,y)
        things_dodged(dodged)
        
        ##doubt thingy is always less than display height
        if thingy>display_height :
            thingy=0-thingh
            thingx=random.randrange(0,display_width-250)
            dodged+=1
            if dodged%2==0:
                thing_speed+=1

        ##for crash
        if x<0 or x>display_width-250 :
            crash()
            
        else:
            for i in range(x,x+250):
                if i in range(thingx,thingx+100):
                    for j in range(y,y+320):
                        if j in range(thingy,thingy+100):
                            crash()


        pygame.display.update()
        clock.tick(90)
game_intro()
pygame.quit()
quit()

#to comment multiple lines select those lines and press alt3
# to uncomment press alt 4
