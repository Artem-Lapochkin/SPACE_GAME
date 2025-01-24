import math
import pygame
from pygame.locals import *
import time


# Класс для создания синего шарика
class BlueBall(pygame.sprite.Sprite):
    def __init__(self, x, y, direction_x, direction_y, speed=8):
        super().__init__()
        self.image = pygame.Surface((5, 5))  # Размер шарика
        self.image.fill(pygame.Color('blue'))  # Красный цвет
        self.rect = self.image.get_rect(center=(x, y))
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.speed = speed

    def update(self):
        self.rect.move_ip(self.direction_x * self.speed, self.direction_y * self.speed)

        # Удаляем шарик, когда он выходит за пределы экрана
        if not pygame.display.get_surface().get_rect().contains(self.rect):
            self.kill()


# Класс для создания 1 игрока
class Player_1(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5  # Скорость перемещения спрайта
        self.balls = pygame.sprite.Group()  # Группа для хранения выпущенных шариков
        self.last_shot_time = 0  # Время последнего выстрела

        self.direction_x = 1
        self.direction_y = 0

    def rotate(self, angle):
        """Поворачивает изображение персонажа на заданный угол."""
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        keys = pygame.key.get_pressed()
        weight, height = self.image.get_size()
        if keys[K_LEFT]:
            self.rect.x -= self.speed
            self.direction_x = -1
            self.direction_y = 0
            self.rotate(math.degrees(math.atan2(self.direction_y, self.direction_x)))
        elif keys[K_RIGHT]:
            self.rect.x += self.speed
            self.direction_x = 1
            self.direction_y = 0
            self.rotate(math.degrees(math.atan2(self.direction_y, self.direction_x)))
        elif keys[K_UP]:
            self.rect.y -= self.speed
            self.direction_x = 0
            self.direction_y = -1
            self.rotate(math.degrees(math.atan2(-self.direction_y, -self.direction_x)))
        elif keys[K_DOWN]:
            self.rect.y += self.speed
            self.direction_x = 0
            self.direction_y = 1
            self.rotate(math.degrees(math.atan2(-self.direction_y, -self.direction_x)))

        current_time = time.time()  # Текущее время
        if keys[K_RETURN] and current_time - self.last_shot_time >= 1:  # Пространство для стрельбы
            ball = BlueBall(self.rect.centerx, self.rect.centery,
                            self.direction_x, self.direction_y)
            self.balls.add(ball)
            self.last_shot_time = current_time  # Обновляем время последнего выстрела


# Класс для создания красного шарика
class RedBall(pygame.sprite.Sprite):
    def __init__(self, x, y, direction_x, direction_y, speed=8):
        super().__init__()
        self.image = pygame.Surface((5, 5))  # Размер шарика
        self.image.fill(pygame.Color('red'))  # Красный цвет
        self.rect = self.image.get_rect(center=(x, y))
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.speed = speed

    def update(self):
        self.rect.move_ip(self.direction_x * self.speed, self.direction_y * self.speed)

        # Удаляем шарик, когда он выходит за пределы экрана
        if not pygame.display.get_surface().get_rect().contains(self.rect):
            self.kill()


# Класс для создания 2 игрока
class Player_2(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5  # Скорость перемещения спрайта
        self.balls = pygame.sprite.Group()  # Группа для хранения выпущенных шариков
        self.last_shot_time = 0  # Время последнего выстрела

        self.direction_x = 1
        self.direction_y = 0

    def rotate(self, angle):
        """Поворачивает изображение персонажа на заданный угол."""
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        keys = pygame.key.get_pressed()
        weight, height = self.image.get_size()
        if keys[K_a]:
            self.rect.x -= self.speed
            self.direction_x = -1
            self.direction_y = 0
            self.rotate(math.degrees(math.atan2(self.direction_y, self.direction_x)))
        elif keys[K_d]:
            self.rect.x += self.speed
            self.direction_x = 1
            self.direction_y = 0
            self.rotate(math.degrees(math.atan2(self.direction_y, self.direction_x)))
        elif keys[K_w]:
            self.rect.y -= self.speed
            self.direction_x = 0
            self.direction_y = -1
            self.rotate(math.degrees(math.atan2(-self.direction_y, -self.direction_x)))
        elif keys[K_s]:
            self.rect.y += self.speed
            self.direction_x = 0
            self.direction_y = 1
            self.rotate(math.degrees(math.atan2(-self.direction_y, -self.direction_x)))

        current_time = time.time()  # Текущее время
        if keys[K_SPACE] and current_time - self.last_shot_time >= 1:  # Пространство для стрельбы
            ball = RedBall(self.rect.centerx, self.rect.centery,
                            self.direction_x, self.direction_y)
            self.balls.add(ball)
            self.last_shot_time = current_time  # Обновляем время последнего выстрела

def terminate():
    pygame.quit()

def start_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 160 <= x <= 300 and 230 <= y <= 370:
                    return True
        pygame.display.flip()

def main():
    pygame.init()
    pygame.display.set_caption('SPACE_GAME_BETA')
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    Player1_image = 'Player1(32x32).png'
    Player2_image = 'Player2(32x32).png'
    counter = -1
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (255, 0, 0), (160, 230, 140, 140), 0)
    pygame.draw.rect(screen, (0, 255, 0), (320, 230, 140, 140), 0)
    pygame.draw.rect(screen, (0, 0, 255), (480, 230, 140, 140), 0)
    running = start_screen()
    font = pygame.font.Font(None, 30)
    vivedenie_texta = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and counter < 0:  # Левая кнопка мыши
                    counter += 1
                    player1 = Player_1(700, 300, Player1_image)
                    all_sprites.add(player1)
                    player2 = Player_2(100, 300, Player2_image)
                    all_sprites.add(player2)
                    vivedenie_texta = 1
                    print(all_sprites.sprites())
                elif event.button == pygame.BUTTON_RIGHT and counter >= -1:  # деспавн игроков, правая кнопка мыши
                    all_sprites.remove(all_sprites.sprites()[0])
                    counter -= 1
                    print(all_sprites.sprites())
        screen.fill(pygame.Color('white'))
        if vivedenie_texta == 0:
            screen.blit(font.render("Для начала игры нажмите ЛКМ", 1, pygame.Color('black')), (50, 50))
        all_sprites.update()
        all_sprites.draw(screen)
        # Обновляем и рисуем все красные шарики
        for sprite in all_sprites.sprites():
            sprite.balls.update()
            sprite.balls.draw(screen)
        pygame.display.flip()
        clock.tick(60)



if __name__ == "__main__":
    main()
