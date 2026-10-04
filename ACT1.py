import pygame
import random
pygame.init()
WIDTH, HEIGHT = 500,400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Collision")
bg = pygame.transform.scale(pygame.image.load("Mario.png"), (WIDTH, HEIGHT))
font = pygame.font.SysFont("Comic Sans", 72)
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.Surface((30,20))
        self.image.fill(color)
        self.rect = self.image.get_rect(x = random.randint(0,WIDTH-30), y = random.randint(0, HEIGHT-20))
    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y
        self.rect.clamp_ip(screen.get_rect())
sprite_1 = Sprite("Black")
sprite_2 = Sprite("Red")
sprites = pygame.sprite.Group(sprite_1, sprite_2)
clock = pygame.time.Clock()
won = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            running = False
    if not won:
        keys = pygame.key.get_pressed()
        x = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT] * 5)
        y = (keys[pygame.K_DOWN] - keys[pygame.K_UP] * 5)
        sprite_1.move(x,y)
        if sprite_1.rect.colliderect(sprite_2.rect):
            sprites.remove(sprite_2)
            won = True
    screen.blit(bg, (0,0))
    sprites.draw(screen)
    if won:
        text = font.render("You Win!", True, "Black")
        screen.blit(text, text.get_rect(center=screen.get_rect().center))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
