from time import sleep

import pygame

class BaseSprite():
    def __init__(self,x,y,texture, w,h,speed):
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, [w,h])
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed


    def draw(self,window):
        window.blit(self.texture, self.hitbox)

class Gold(BaseSprite):
    def update(self):
        pass


class Hero(BaseSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_i]:
            self.hitbox.x += self.speed
        if keys[pygame.K_u]:
            self.hitbox.x -= self.speed
        if keys[pygame.K_l]:
            self.hitbox.y -= self.speed
        if keys[pygame.K_k]:
            self.hitbox.y += self.speed

class Enemy(BaseSprite):
    def __init__(self, x1, y1, texture, speed, w, h, x2, y2):
        super().__init__(x1,y1,texture,speed, w, h)
        self.direction = "forward"
        self.x1 = x1
        self.x2 = x2
        self.y2 = y2

    def update(self):
        if self.direction == "forward":
            self.hitbox.x += self.speed
            if self.hitbox.x > self.x2:
                self.direction= "back"
        else:
            self.hitbox.x -= self.speed
            if self.hitbox.x < self.x1:
                self.direction = "forward"


class Wall():
    def __init__(self, x, y, color, w, h):
        self.hitbox = pygame.Rect(x,y,w,h)
        self.hitbox.x = x
        self.hitbox.y = y
        self.color = color

    def draw(self,window):
        pygame.draw.rect(window, self.color, self.hitbox)
pygame.init()

window = pygame.display.set_mode([700,500])
clock = pygame.time.Clock()

background_img = pygame.image.load("background.jpg")
background_img = pygame.transform.scale(background_img, [700,500])
hero = Hero(150,111,"hero.png", 50,50,2)
enemy = Enemy(534,110,"cyborg.png",50,50,1,604,110)
gold = Gold(615,42,"treasure.png",50,50,0)
game = True

walls = [
    Wall(115,80, [255,0,0], 100,20),
    Wall(115,99,[255,0,0], 20,100),
    Wall(115,199,[255,0,0], 20,100),
    Wall(115,299,[255,0,0], 20,100),
    Wall(115,398,[255,0,0], 100,20),
    Wall(215,398,[255,0,0], 100,20),
    Wall(314,398,[255,0,0], 100,20),
    Wall(215,80,[255,0,0], 20,100),
    Wall(215, 178, [255, 0, 0], 20, 100),
    Wall(215, 278, [255, 0, 0], 20, 50),
    Wall(215, 325, [255, 0, 0], 100, 20),
    Wall(314, 245, [255, 0, 0], 20, 100),
    Wall(314, 238, [255, 0, 0], 100, 20),
    Wall(400, 238, [255, 0, 0], 20, 100),
    Wall(414, 398, [255, 0, 0], 100, 20),
    Wall(400, 162, [255, 0, 0], 20, 100),
    Wall(235, 80, [255, 0, 0], 100, 20),
    Wall(328, 80, [255, 0, 0], 100, 20),
    Wall(314, 162, [255, 0, 0], 20, 100),
    Wall(414, 80, [255, 0, 0], 100, 20),
    Wall(494, 99, [255, 0, 0], 20, 100),
    Wall(494, 197, [255, 0, 0], 20, 100),
    Wall(494, 238, [255, 0, 0], 20, 100),
    Wall(513, 398, [255, 0, 0], 100, 20),
    Wall(593, 307, [255, 0, 0], 20, 100),
    Wall(593, 209, [255, 0, 0], 20, 100),



]

pygame.mixer.init()
pygame.mixer.music.load("jungles.ogg")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

gold_sound = pygame.mixer.Sound("money.ogg")
kick_sound = pygame.mixer.Sound("kick.ogg")
text = pygame.font.Font(None, 170).render("Перемога!", True, [0, 0, 0])
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())

    gold.update()
    enemy.update()
    hero.update()

    for wall in walls:
        if hero.hitbox.colliderect(wall.hitbox):
            hero.hitbox.x = 150
            hero.hitbox.y = 111
            kick_sound.play()




    if hero.hitbox.colliderect(gold.hitbox):
        window.fill([0, 123, 0])
        window.blit(text, [50,194])
        gold_sound.play()
        pygame.display.flip()
        sleep(5)

    if hero.hitbox.colliderect(enemy.hitbox):
        hero.hitbox.x = 150
        hero.hitbox.y = 111
        kick_sound.play()

    window.fill([123,123,123])
    window.blit(background_img,[0,0])
    gold.draw(window)
    hero.draw(window)
    enemy.draw(window)

    for wall in walls:
        wall.draw(window)
    pygame.display.flip()

    clock.tick(60)