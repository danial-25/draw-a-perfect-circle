import pygame, sys
from pygame.locals import *
import time
import math
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

mouse_position = (0, 0)
drawing = False
screen = pygame.display.set_mode((600, 800), 0, 32)
screen.fill(WHITE)
last_pos = None
circle_color = (0, 0, 255)  
circle_radius = 20
center_x = 600 // 2
center_y = 800 // 2
pygame.font.init() 
my_font = pygame.font.SysFont('SF Pro', 40)
close_text=my_font.render('Too close', False, (0, 0, 0))
time_out=my_font.render('Too slow', False, (0, 0, 0))
fail_text=my_font.render('Draw a full circle', False, (0, 0, 0))
screen.fill(WHITE)
pygame.draw.circle(screen, circle_color, (center_x, center_y), circle_radius)
pygame.display.update()
f=c_n=percent=0
start_time = time.time()
x4=y4=x1=y1=i=k=angle=0
while True:
    for event in pygame.event.get():
        elapsed_time = time.time() - start_time
        seconds = int(elapsed_time % 60)
        if k!=0:
            start_time=time.time()
        if seconds>=7:
            mouse_position = (0, 0)
            drawing = False
            last_pos = None
            screen.fill(pygame.Color("white"), (center_x/1.25, 0, 600, 40))
            screen.blit(time_out, (center_x/1.25,0))
            f=1
            start_time=time.time()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            if (drawing):
                mouse_position = pygame.mouse.get_pos()
                th_x,th_y=mouse_position
                if(c_n==0):
                    x_c, y_c=mouse_position
                    l=math.sqrt(pow(x_c-center_x,2)+pow(y_c-center_y,2))
                    c_n+=1
                if(c_n==2):
                    x1,y1=mouse_position
                if f!=0:
                    screen.fill(WHITE)
                    pygame.draw.circle(screen, circle_color, (center_x, center_y), circle_radius)
                    pygame.display.update()
                    drawing = True
                    f=0
                if last_pos is not None:
                    i=100-percent
                    pygame.draw.line(screen, (2*abs(int(i)),0,0), last_pos, mouse_position, 4)
                    #coords of ideal circle 

                    if(x_c<center_x):#starting position: left corner
                        if(x1!=0 and y1!=0):      
                            if(y1<y_c):#if line goes down
                                angle=math.atan(-1*(y_c-center_y)/(x_c-center_x))+math.pi-0.7*c_n*math.pi/180
                                th_y=l*math.sin(angle) 
                                th_x=l*math.cos(angle)
                            if(y1>y_c):#if line goes up
                                angle=math.atan(-1*(y_c-center_y)/(x_c-center_x))+math.pi+0.7*c_n*math.pi/180
                                th_y=l*math.sin(angle) 
                                th_x=l*math.cos(angle)
                    if(x_c>center_x):#starting position: right corner
                        if(x1!=0 and y1!=0):      
                            if(y1>y_c):#if line goes down
                                angle=math.atan(-1*(y_c-center_y)/(x_c-center_x))+math.pi-0.7*c_n*math.pi/180
                                th_y=l*math.sin(angle) 
                                th_x=l*math.cos(angle)
                            if(y1<y_c):#if line goes up
                                angle=math.atan(-1*(y_c-center_y)/(x_c-center_x))+math.pi+0.7*c_n*math.pi/180
                                th_y=l*math.sin(angle)
                                th_x=l*math.cos(angle)
                    c_n+=1
                last_pos = mouse_position
                x,y=last_pos
                percent=100-100*(abs(((center_x+th_x)-x)/x)+abs(((center_y-th_y)-y)/y))/2 #how similiar th. values to practical
                if(percent<0):
                    percent=0
                screen.fill(pygame.Color("white"), (center_x/1.25, 0, 600, 40))
                percentage=my_font.render(f'{round(percent,1)}%', False, (0, 0, 0))
                screen.blit(percentage, (center_x/1.25,0))
                #fail in case mouse is out of range of screen
                if(x>600 or y>800 or x<0 or y<0):
                    mouse_position = (0, 0)
                    drawing = False
                    last_pos = None
                    screen.fill(pygame.Color("white"), (center_x/1.25, 0, 600, 40))
                    screen.blit(fail_text, (center_x/1.25,0))
                    f=1
                elif(pow((x-center_x),2)+pow((y-center_y),2)<pow(4*circle_radius,2)):
                    mouse_position = (0, 0)
                    drawing = False
                    last_pos = None
                    screen.fill(pygame.Color("white"), (center_x/1.25, 0, 600, 40))
                    screen.blit(close_text, (center_x/1.25,0))
                    f=1
                    c_n=0
        elif event.type == MOUSEBUTTONUP:
            mouse_position = (0, 0)
            drawing = False
            last_pos = None
            k=f=1
            c_n=0
        elif event.type == MOUSEBUTTONDOWN:
            drawing = True
            if k==1:
                screen.fill(WHITE)
                pygame.draw.circle(screen, circle_color, (center_x, center_y), circle_radius)
                pygame.display.update()
                k=0
    pygame.display.update()
