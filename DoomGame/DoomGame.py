import pygame, sys
from pygame.locals import *
pygame.init()

win = pygame.display.set_mode((1400,480))

pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('prawo10.png'), pygame.image.load('prawo11.png'), pygame.image.load('prawo12.png'), pygame.image.load('prawo13.png')]
walkLeft = [pygame.image.load('lewo10.png'), pygame.image.load('lewo11.png'), pygame.image.load('lewo12.png'), pygame.image.load('lewo13.png')]
tło = pygame.image.load('tło.jpg')


clock = pygame.time.Clock()

bulletSound = pygame.mixer.Sound('boom.wav')
hitSound = pygame.mixer.Sound('auc.wav')
winSound = pygame.mixer.Sound('win.wav')
loseSound = pygame.mixer.Sound('lose.wav')

music = pygame.mixer.music.load('doom.mp3')
pygame.mixer.music.play(-1)

score = 0


class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 7
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, win):
        if self.walkCount + 1 >= 12:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def hit(self):
        self.isJump = False
        self.jumpCount = 8
        self.x = 100
        self.y = 410
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('-5', 1, (255,0,0))
        win.blit(text, (250 - (text.get_width()/2),200))
        pygame.display.update()
        i = 0
        while i < 200:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 201
                    pygame.quit()
                    
     
                


class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 15 * facing

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)


class enemy(object):
    walkRight = [pygame.image.load('wrog7.png'), pygame.image.load('wrog8.png'), pygame.image.load('wrog9.png'), pygame.image.load('wrog10.png')]
    walkLeft = [pygame.image.load('wrog1.png'), pygame.image.load('wrog2.png'), pygame.image.load('wrog3.png'), pygame.image.load('wrog4.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True


       

        
        

    def draw(self,win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 12:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            #pygame.draw.rect(win, (255,0,0), self.hitbox,2)


    

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
            if self.health == 0:
                print("smierc")
                wrog.visible = False
                wrog3.visible = False
                
                wrog2.visible = True
                
                wrog2.vel = 7
                wrog2.health = 15
                
                
                
            
                
    def hit2(self):
        
        if self.health > 0:
            self.health -= 1
            if self.health == 0:
                print("smierc")
                
                wrog2.visible = False
                wrog3.visible = True
                wrog3.vel = 20
                wrog3.health = 25

    def hit3(self):
        
        
        if self.health > 0:
            self.health -= 1
            if self.health == 0:
                print("smierc")
                wrog3.visible = False
                napis2()
                
               
                
        
            
        
        

def redrawGameWindow():
    win.blit(tło, (0,0))
    text = font.render('Score: ' + str(score), 1, (255,255,255))
    win.blit(text, (350, 10))
    man.draw(win)
    wrog.draw(win)
    wrog2.draw(win)
    wrog3.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    
    pygame.display.update()


#mainloop
font = pygame.font.SysFont('comicsans', 30, True)
man = player(100, 410, 64,64)
wrog = enemy(300, 410, 64, 64, 450)
wrog2 = enemy(800, 410, 64 , 64, 1300)
wrog3 = enemy(100, 410, 64 , 64, 1300)
shootLoop = 0
bullets = []
run = True
wrog2.visible = False
wrog3.visible = False


def napis():
    skrn = pygame.display.set_mode((1400,480))
    
    skrn.fill((0,0,0))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            sys_font = pygame.font.SysFont("None", 60)
            rendered = sys_font.render("Przegrałeś, twój wynik to: " + str(score) ,0,(255, 200, 100))
            skrn.blit(rendered, (180, 100))
            pygame.display.update()
            pygame.mixer.music.stop()
            
            
            loseSound.play()
            
def napis2():
        skrn = pygame.display.set_mode((1440,480))
        pygame.display.set_caption("ggsgs")
        skrn.fill((0,0,0))

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                sys_font = pygame.font.SysFont("None", 60)
                rendered = sys_font.render("WYGRAŁES, twój wynik to: " + str(score + 1) ,0,(255, 200, 100))
                skrn.blit(rendered, (180, 100))
                pygame.mixer.music.stop()
                winSound.play()
                pygame.display.update()

                

                
            
        

while run:
    clock.tick(27)

    if wrog.visible == True:
        if man.hitbox[1] < wrog.hitbox[1] + wrog.hitbox[3] and man.hitbox[1] + man.hitbox[3] > wrog.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > wrog.hitbox[0] and man.hitbox[0] < wrog.hitbox[0] + wrog.hitbox[2]:
                
                
                napis()
                
                
    if wrog2.visible == True:
        
        if man.hitbox[1] < wrog2.hitbox[1] + wrog2.hitbox[3] and man.hitbox[1] + man.hitbox[3] > wrog2.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > wrog2.hitbox[0] and man.hitbox[0] < wrog2.hitbox[0] + wrog2.hitbox[2]:
                
                napis()
    if wrog3.visible == True:
        
        if man.hitbox[1] < wrog3.hitbox[1] + wrog3.hitbox[3] and man.hitbox[1] + man.hitbox[3] > wrog3.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > wrog3.hitbox[0] and man.hitbox[0] < wrog3.hitbox[0] + wrog3.hitbox[2]:
                
                napis()     
                

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 14:
        shootLoop = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    for bullet in bullets:
        if wrog.visible == True:
            if bullet.y - bullet.radius < wrog.hitbox[1] + wrog.hitbox[3] and bullet.y + bullet.radius > wrog.hitbox[1]:
                if bullet.x + bullet.radius > wrog.hitbox[0] and bullet.x - bullet.radius < wrog.hitbox[0] + wrog.hitbox[2]:
                    hitSound.play()
                    wrog.hit()
                    score += 1
                    bullets.pop(bullets.index(bullet))
                  
    for bullet in bullets:
       
        if wrog2.visible == True:
            if bullet.y - bullet.radius < wrog2.hitbox[1] + wrog2.hitbox[3] and bullet.y + bullet.radius > wrog2.hitbox[1]:
                if bullet.x + bullet.radius > wrog2.hitbox[0] and bullet.x - bullet.radius < wrog2.hitbox[0] + wrog2.hitbox[2]:
                    hitSound.play()
                    wrog2.hit2()
                    score += 1
                    bullets.pop(bullets.index(bullet))
        if wrog3.visible == True:
            if bullet.y - bullet.radius < wrog3.hitbox[1] + wrog3.hitbox[3] and bullet.y + bullet.radius > wrog3.hitbox[1]:
                if bullet.x + bullet.radius > wrog3.hitbox[0] and bullet.x - bullet.radius < wrog3.hitbox[0] + wrog3.hitbox[2]:
                    hitSound.play()
                    wrog3.hit3()
                    score += 1
                    bullets.pop(bullets.index(bullet))
                    
     
              
                    
                   

                    
                
        if bullet.x < 1400 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
            

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        bulletSound.play()
        if man.left:
            facing = -1
        else:
            facing = 1
            
        if len(bullets) < 100:
            bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//3), 4, (0,0,0), facing))

        shootLoop = 1

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 1400 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0
        
    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
            
    redrawGameWindow()

pygame.quit()
