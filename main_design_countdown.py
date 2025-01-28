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


# Класс для создания 1 игрока
class Player_1(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, wall_sprites):
        super().__init__()
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5  # Скорость перемещения спрайта
        self.balls = pygame.sprite.Group()  # Группа для хранения выпущенных шариков
        self.last_shot_time = 0  # Время последнего выстрела

        self.direction_x = 1
        self.direction_y = 0

        self.wall_sprites = wall_sprites

    def rotate(self, angle):
        """Поворачивает изображение персонажа на заданный угол."""
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        keys = pygame.key.get_pressed()
        original_rect = self.rect.copy()  # Сохраняем оригинальное положение

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

        # Проверяем на столкновение с стенами
        if pygame.sprite.spritecollideany(self, self.wall_sprites):
            self.rect = original_rect  # Возвращаем к оригинальному положению, если произошло столкновение

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


# Класс для создания 2 игрока
class Player_2(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, wall_sprites):
        super().__init__()
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5  # Скорость перемещения спрайта
        self.balls = pygame.sprite.Group()  # Группа для хранения выпущенных шариков
        self.last_shot_time = 0  # Время последнего выстрела

        self.direction_x = 1
        self.direction_y = 0

        self.wall_sprites = wall_sprites

    def rotate(self, angle):
        """Поворачивает изображение персонажа на заданный угол."""
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        keys = pygame.key.get_pressed()
        original_rect = self.rect.copy()  # Сохраняем оригинальное положение

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

        # Проверяем на столкновение с стенами
        if pygame.sprite.spritecollideany(self, self.wall_sprites):
            self.rect = original_rect  # Возвращаем к оригинальному положению, если произошло столкновение

        current_time = time.time()  # Текущее время
        if keys[K_SPACE] and current_time - self.last_shot_time >= 1:  # Пространство для стрельбы
            ball = RedBall(self.rect.centerx, self.rect.centery,
                           self.direction_x, self.direction_y)
            self.balls.add(ball)
            self.last_shot_time = current_time  # Обновляем время последнего выстрела


class Wall(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2, width=5):
        super().__init__()
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.width = width
        self.image = pygame.Surface((abs(x2 - x1) + width, abs(y2 - y1) + width))
        self.image.fill(pygame.Color('white'))
        self.rect = self.image.get_rect(topleft=(x1, y1))


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
    # возможность сделать полный экран
    #screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    wall_sprites = pygame.sprite.Group()

    Player1_image = 'Player1(32x32).png'
    Player2_image = 'Player2(32x32).png'

    screen.fill((0, 6, 17))

    counter = -1

    pygame.draw.rect(screen, (255, 0, 0), (160, 230, 140, 140), 0)
    pygame.draw.rect(screen, (0, 255, 0), (320, 230, 140, 140), 0)
    pygame.draw.rect(screen, (0, 0, 255), (480, 230, 140, 140), 0)

    running = start_screen()

    font = pygame.font.Font(None, 30)

    # Начальное значение счетчика
    countdown_value = 999
    # Создаём пользовательское событие для таймера
    COUNTDOWN_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(COUNTDOWN_EVENT, 1000)  # Таймер срабатывает каждые 1000 мс (1 секунда)

    vivedenie_texta = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == COUNTDOWN_EVENT: # игра выключается, если время заканчивается
                countdown_value -= 1
                if countdown_value <= 0:
                    print("Время вышло!")
                    running = False

            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and counter < 0:  # Левая кнопка мыши

                    countdown_value = 60

                    counter += 1

                    wall_sprites.add(Wall(0, 0, 800, 0))
                    wall_sprites.add(Wall(0, 595, 800, 595))
                    wall_sprites.add(Wall(0, 0, 0, 600))
                    wall_sprites.add(Wall(795, 0, 795, 600))

                    wall_sprites.add(Wall(200, 200, 200, 400))
                    wall_sprites.add(Wall(600, 200, 600, 400))

                    wall_sprites.add(Wall(300, 400, 300, 600))
                    wall_sprites.add(Wall(300, 500, 400, 500))
                    wall_sprites.add(Wall(500, 0, 500, 200))
                    wall_sprites.add(Wall(400, 100, 500, 100))

                    wall_sprites.add(Wall(300, 290, 350, 290))
                    wall_sprites.add(Wall(450, 310, 500, 310))

                    wall_sprites.add(Wall(350, 175, 350, 200))
                    wall_sprites.add(Wall(450, 400, 450, 425))

                    wall_sprites.add(Wall(75, 75, 300, 75))
                    wall_sprites.add(Wall(500, 525, 725, 525))

                    wall_sprites.add(Wall(150, 400, 200, 400))
                    wall_sprites.add(Wall(600, 200, 650, 200))

                    wall_sprites.add(Wall(100, 500, 200, 500))
                    wall_sprites.add(Wall(600, 100, 700, 100))

                    player1 = Player_1(700, 300, Player1_image, wall_sprites)
                    all_sprites.add(player1)
                    player2 = Player_2(100, 300, Player2_image, wall_sprites)
                    all_sprites.add(player2)

                    vivedenie_texta = 1
                    print(all_sprites.sprites())

        screen.fill((0, 6, 17))

        if vivedenie_texta == 0:
            screen.blit(font.render("Для начала игры нажмите ЛКМ", 1, pygame.Color('white')), (50, 50))

        # Отображение значения счетчика
        text_surface = font.render(str(countdown_value), True, (255, 255, 255))
        screen.blit(text_surface, (400, 5))

        for sprite in all_sprites.sprites():
            for balls in sprite.balls.sprites():
                if sprite.balls.sprites():
                    if pygame.sprite.spritecollideany(balls, wall_sprites):
                        print("Ball/Wall collision detected!")
                        balls.kill()

        all_sprites.update()
        all_sprites.draw(screen)
        wall_sprites.update()
        wall_sprites.draw(screen)

        # Обновляем и рисуем все красные шарики
        for sprite in all_sprites.sprites():
            sprite.balls.update()
            sprite.balls.draw(screen)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
