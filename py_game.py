import pygame
from PIL import Image
import time 
import random
import itertools

img=Image.open('quit.jpg')
n=80
w=90
img = img.resize((n,w), Image.ANTIALIAS)
img.save('quit1.jpg')
pygame.init()
disp_width=800
disp_height=600
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)

gameDisp=pygame.display.set_mode((disp_width,disp_height))

pygame.display.set_caption('race game')

clock=pygame.time.Clock()
car_img=pygame.image.load('out.png')
rock=pygame.image.load('rock_t.png')
rock2= pygame.image.load('rock_t2.png')
new_game= pygame.image.load('new_game.jpg')
quit1= pygame.image.load('quit.jpg')
myfunc=itertools.cycle([rock,rock2])
def game_intro():
	intro=True
	while(intro):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisp.fill(white)
		disp=pygame.font.Font('freesansbold.ttf',30)
		text="race car game"
		surf , rect = rend(text,disp)
		rect.center=((disp_width*0.5),(disp_height*0.5))
		gameDisp.blit(surf, rect)
		mouse= pygame.mouse.get_pos()
		click=pygame.mouse.get_pressed()
		gameDisp.blit(new_game,((disp_width*0.08),(disp_height*0.6)))
		gameDisp.blit(quit1,((disp_width*0.6),(disp_height*0.6)))
		if (disp_width*0.08 + 287 > mouse[0] >disp_width*0.08) and (disp_height*0.6 +33 > mouse[1] > disp_height*0.6):
			if click[0]==1:
				game_loop()
		elif (disp_width*0.6 + 287 > mouse[0] >disp_width*0.6) and (disp_height*0.6 +33 > mouse[1] > disp_height*0.6):
			if click[0]==1:
				pygame.quit() 
			quit()


		pygame.display.update()
		clock.tick(15)
		



def score(count):
	disp=pygame.font.Font('freesansbold.ttf',30)
	text="Dodged:" + str(count)
	surf , rect = rend(text,disp)
	rect.center=((disp_width*0.85),(disp_height*0.1))
	gameDisp.blit(surf, rect)
	clock.tick(500)

def rend(txt,font):
	txt_surf=font.render(txt,True,black)
	return txt_surf,txt_surf.get_rect()
def message_disp(text):
	disp=pygame.font.Font('freesansbold.ttf',100)        
	surf,rect =rend(text,disp)
	rect.center= ((disp_width/2),(disp_height/2))
	gameDisp.blit(surf, rect)
	pygame.display.update()
	time.sleep(2)
	game_loop()
def crash():
	message_disp('You Crashed')
def car(x,y):
	gameDisp.blit(car_img,(x,y))
def game_loop():
	x=(disp_width*0.45)
	y=(disp_height*0.8)
	exit=False
	x_change=0
	t_startx=random.randrange(0,disp_width-50)
	t_starty= -800
	t_speed=1
	t_width=100
	t_height=100
	counter=0
	flag=0
	img=next(myfunc)
	while not exit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change= -1
				elif event.key == pygame.K_RIGHT:
					x_change= 1
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change=0

		x+=x_change

		gameDisp.fill(white)
	
		score(counter)
		
		
		gameDisp.blit(img,(t_startx,t_starty))
		#elif flag==0 :
			#gameDisp.blit(rock2,(t_startx,t_starty))

		t_starty=t_speed+t_starty
		car(x,y)
		if x > disp_width - 90 or x < 0:
			crash()
		
		if t_starty > disp_height:
			t_starty=-80
			t_startx=random.randrange(0,disp_width)
			counter= counter+1
			t_speed= t_speed + 0.08
			img=next(myfunc)
		
		if y < t_starty + 90:
			if x+ 70 > t_startx and x < t_startx +70:
				crash()
		
		pygame.display.update()
		clock.tick(500)
game_intro()
game_loop()
pygame.quit() 
quit()
