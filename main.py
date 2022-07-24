import pygame
import random
import math
# to initlaise python
pygame.init()
# to create screen
screen = pygame.display.set_mode((700,850))
pygame.display.set_caption("my game")
screen.fill((220,240,220))
pygame.display.update()
#to include vthe space ship
pimg = pygame.image.load('mess.png')
px =  300
py = 750
# to include the enemie n  enimies
#n = random.randint(2,8)
ex = []
emg =pygame.image.load('ali.png')
ey = []
exc =[]
n = random.randint(5,10)
for i in range(n):
  ex.append(random.randint(0,600))
  ey. append(random.randint(-200,-50))
  exc.append(1)
#exc1 = .3
#xc2 = .3
#exc3 = .3
eyc = 10
#ex =random.randint(0,700)
#ex2 =random.randint(0,700)
#ex3 =random.randint(0,700)
#ey = random.randint(50,150)
#ey2 = random.randint(50,150)
#ey3 = random.randint(50,150)

#def enemy

def enemy(x, y):
  screen.blit(emg,(x,y))
  #def player
def player(px,py):
	screen.blit(pimg,(px,py))
  #def bullet
bx = px 
by = 735
bullet_state ="ready"

bulle = pygame.image.load('bull.png') 
def bullet(x,y):
  global bullet_state
  bullet_state = "fire" 
  screen.blit(bulle,(x+16 ,y+4))     
#def collition
def dcollition(x1,y1,x2,y2):
  dist = math.sqrt((math.pow(x1-x2,2))+(math.pow(y1-y2,2)))
  if dist <= 27:
      return True
  else :
      return False  
# to show the score
score= 0  
font = pygame.font.Font('freesansbold.ttf', 32)
tx =10
ty= 10
def show_score(x,y):
  scorei = font.render("score : "+str(score),True,(0,0,0))
  screen.blit(scorei,(x,y))
  # game over
over = pygame.font.Font('freesansbold.ttf',64)
overscore = pygame.font.Font('freesansbold.ttf',48)
def game_over():
 over_t = over.render("GAME OVER",True,(0,0,0))
 over_s= overscore.render("YOUR SCORE : "+str(score),True,(0,0,0))
 screen.blit(over_t,(150,300))
 screen.blit(over_s,(150,400))
# enemy(ex,ey)
pygame.display.update()

player(px,py)
pygame.display.update()	
# the game 
running = True
while running:
 screen.fill((220,245,240))
 for event in pygame.event.get():
  pxc=0
  if event.type == pygame.QUIT: 
 	 running=False
  if event.type == pygame.KEYDOWN:	 
      if event.key == pygame.K_LEFT:
 	    	     pxc=-1
 	    	     print("left arrow is pressed")
      if event.key == pygame.K_RIGHT:
            pxc=1
            print("right arrow is pressed")
      if event.key == pygame.K_SPACE:
         if by == 735:
            by=735
            bx=px
            bullet(bx,by)
      
      
              
      if event.type == pygame.KEYUP:
       if event.key == K_LEFT or event.key == K_RIGHT:
      	 	 pxc=1
        
 if bullet_state is "fire" :
   bullet(bx,by)
   by-=2
 if by<=0:
   by=735
   bullet_state = "ready"
 px += pxc
 if px<=0  :
   px=0
 if px>=636:
   px=636 
 for i in range(n):
  if ey[i] >= 780:
     tx=2000
     ty=2000
     for j in range(n):
       ey[j]=2000
     game_over()
     break
  ey[i]+=.3
  #ex[i]+=exc[i]
 # if ex[i]<=0: 
  #  exc[i]=1
   # ey[i]+=40
  #elif ex[i]>=636:
   # exc[i]=-1
    #ey[i]+=40
  enemy(ex[i],ey[i])  
  col = dcollition(ex[i],ey[i],bx,by)  
  if col :
    by=735
    bullet_state = "ready"
    score+=1
    print(score)
    ex[i]= random.randint(0,600)
    ey[i]=random.randint(-200,-50)    
  enemy(ex[i],ey[i])      
 player(px,py)
 show_score(tx,ty)
