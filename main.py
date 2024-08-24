import random

import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("nombre de membre du serv discord = nombre de ligne de code")
running = True
moving_platform = []
clock = pygame.time.Clock()
game_started = False
font = pygame.font.Font(None, 40)
text = font.render("appuiyez sur espace pour commencer", False, "black")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 5
        self.start_rect = pygame.Rect(390, 200, 20, 30)
        self.rect = self.start_rect
        self.vel_y = 0
        self.jump_power = 11
        self.gravity = 0.6

    def reset(self):
        global game_started
        self.rect.y = 200
        self.vel_y = 0
        game_started = False

    def jump(self):
        self.vel_y = -self.jump_power

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_q]:
            self.rect.x -= self.speed
        if game_started:
            self.vel_y += self.gravity
            self.rect.y += self.vel_y
        for sprite in pygame.sprite.spritecollide(self, moving_platform, False):
            moving_platform.remove(sprite)
            self.jump()
        if self.rect.y > screen.get_height():
            self.reset()


class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.rect = pygame.Rect(-100, random.randint(300, 500), 100, 20)

    def move(self):
        self.rect.x += 6


player = Player()
while running:
    screen.fill("skyblue")
    pygame.draw.rect(screen, "red", player.rect)
    player.update()
    if not game_started:
        screen.blit(text, (152, 20))
    if random.randint(0, 10) == 0:
        moving_platform.append(Platform())
    for mplat in moving_platform:
        pygame.draw.rect(screen, mplat.color, mplat.rect)
        mplat.move()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_started = True
    clock.tick(60)
