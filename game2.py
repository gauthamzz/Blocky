import random
import pygame
import math
from pygame.locals import *

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
window_size=screenx,screeny=1090,700
window = pygame.display.set_mode(window_size)

def message_to_screen(window,msg,colour=WHITE,x=0,y=0,fontsize=25,bold=False,italic = False ):
    message_font = pygame.font.SysFont("Century Gothic",fontsize,bold,italic)
    screen_text = message_font.render(msg,True,colour)
    window.blit(screen_text,[x,y])

class Ball(pygame.sprite.Sprite):

    def __init__(self):
        super(Ball, self).__init__()
        #The image of the main char
        self.image = pygame.image.load("smiley.png").convert()

        self.effect=pygame.mixer.Sound("tap.wav")

        self.rect=self.image.get_rect()

        #velocityg
        self.change_x=0
        self.change_y=0
        #list of sprites to bumb aganist
        self.Blocks=None
    def update(self):

	if self.rect.x < 0:
		self.change_x=+1
	if self.rect.x>1090:
		self.change_x=-1
        self.rect.x=self.rect.x+self.change_x


    def hit(self):
        self.change_x=0




    def go_left(self):
        #magnitude of change
 
        self.change_x=-5
        self.effect.play()
    def go_right(self):
        self.change_x=5
        self.effect.play()

    def stop(self):
        self.change_x=0


class Blocks(pygame.sprite.Sprite):
    #this class contains the falling objects
    def __init__(self,i):
        self.block_list=pygame.sprite.Group()
        pos=[30,40]
        super(Blocks, self).__init__()
        #change this image to change the object
        self.image = pygame.image.load("block.jpg").convert()
        self.rect=self.image.get_rect()


        self.changey=1
        #these values denote the pixel they are falling down
        if i==0:
            self.rect.x=0
        elif i==1:
            self.rect.x=180
        elif i==2:
            self.rect.x=360
        elif i==3:
            self.rect.x=540
        elif i==4:
            self.rect.x=720
        elif i==5:
            self.rect.x=900



    def update(self):
        self.block_list.update()
        self.rect.y+=self.changey
def main():
    pygame.init()
    #screen size and intilization
    screen=pygame.display.set_mode([screenx,screeny])
    pygame.display.set_caption("Blocky")
    ball=Ball()

    block_list=[]



    active_sprite_list=pygame.sprite.Group()

    ball.rect.x=400
    ball.rect.y=300
    x=2020
    score=0
    tick=300
    done =False
    print("Score")
    clock=pygame.time.Clock()
    while not done:
        x+=1
        v=0
        if x%500==0:

            block_list[:]=[]
            k=random.randint(1,6)
            v=k
            score+=100
            print(score)
	    message_to_screen( window , "Shade : " , WHITE , 80  , 455 , 20 )
            #for randomly assingning the way the blocks fall
            for i in range(k):
                if k<4 and i<4:
                    block=Blocks(i)
                elif i<7-k:
                    block=Blocks(5-i)

                block_list.append(block)

        active_sprite_list.add(ball,block_list)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            #change these lines to change the button of moving 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ball.go_left()


                if event.key == pygame.K_RIGHT:
                    ball.go_right()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and ball.change_x < 0:
                    ball.stop()
                if event.key == pygame.K_RIGHT and ball.change_x > 0:
                    ball.stop()

            if pygame.sprite.spritecollideany(ball,block_list):
                ball.hit()
                done=True
                return score




        active_sprite_list.update()

        screen.fill(BLACK)
        #updating the screen
        active_sprite_list.draw(screen)
        tick+=5
        clock.tick(tick)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    Final_score=main()
    print(Final_score)





