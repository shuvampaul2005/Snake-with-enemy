import pygame, sys, random
from pygame.math import Vector2
from pygame import mixer


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_Block = False
        self.erase_Block = False

        self.head_up = pygame.image.load('requirements/Images/head_up.png')
        self.head_down = pygame.image.load('requirements/Images/head_down.png')
        self.head_left = pygame.image.load('requirements/Images/head_left.png')
        self.head_right = pygame.image.load('requirements/Images/head_right.png')

        self.tail_up = pygame.image.load('requirements/Images/tail_up.png')
        self.tail_down = pygame.image.load('requirements/Images/tail_down.png')
        self.tail_right = pygame.image.load('requirements/Images/tail_right.png')
        self.tail_left = pygame.image.load('requirements/Images/tail_left.png')

        self.body_tr = pygame.image.load('requirements/Images/body_tr.png')
        self.body_tl = pygame.image.load('requirements/Images/body_tl.png')
        self.body_br = pygame.image.load('requirements/Images/body_br.png')
        self.body_bl = pygame.image.load('requirements/Images/body_bl.png')

        self.body_horizontal = pygame.image.load('requirements/Images/body_horizontal.png')
        self.body_vertical = pygame.image.load('requirements/Images/body_vertical.png')
        self.bite_sound = pygame.mixer.Sound('requirements/Music/Bite.wav')

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            # Create a rectangle
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            # Draw Rectangle
            # pygame.draw.rect(screen, (183, 191, 122), block_rect)

            # Facing the head
            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)

            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)

                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)

            # else:
            # pygame.draw.rect(screen,(150,100,100),block_rect)

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]

    def move_snake(self):
        if self.new_Block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_Block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_Block(self):
        self.new_Block = True


class SNAKE2:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(2, 0)
        self.new_Block = False

        self.head_up = pygame.image.load('Snake_crawler/Enemy/head_up.png')
        self.head_down = pygame.image.load('Snake_crawler/Enemy/head_down.png')
        self.head_left = pygame.image.load('Snake_crawler/Enemy/head_left.png')
        self.head_right = pygame.image.load('Snake_crawler/Enemy/head_right.png')

        self.tail_up = pygame.image.load('Snake_crawler/Enemy/tail_up.png')
        self.tail_down = pygame.image.load('Snake_crawler/Enemy/tail_down.png')
        self.tail_right = pygame.image.load('Snake_crawler/Enemy/tail_right.png')
        self.tail_left = pygame.image.load('Snake_crawler/Enemy/tail_left.png')

        self.body_tr = pygame.image.load('Snake_crawler/Enemy/tr.png')
        self.body_tl = pygame.image.load('Snake_crawler/Enemy/tl.png')
        self.body_br = pygame.image.load('Snake_crawler/Enemy/br.png')
        self.body_bl = pygame.image.load('Snake_crawler/Enemy/bl.png')

        self.body_horizontal = pygame.image.load('Snake_crawler/Enemy/horizontal.png')
        self.body_vertical = pygame.image.load('Snake_crawler/Enemy/vertical.png')
        self.bite_sound = pygame.mixer.Sound('Snake_crawler/Music/Bite.wav')

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down

    def draw_snake2(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            # Create a rectangle
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            # Draw Rectangle
            # pygame.draw.rect(screen, (183, 191, 122), block_rect)

            # Facing the head
            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)

            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)

                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)

            # else:
            # pygame.draw.rect(screen,(150,100,100),block_rect)

    def move_snake2(self):
        if self.new_Block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_Block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_Block2(self):
        self.new_Block = True

    def reset2(self):
        self.body = [Vector2(8, 10), Vector2(9, 10), Vector2(10, 10)]


class FRUIT:
    def __init__(self):
        self.randomize()

    def randomize(self):
        # Create an X and Y pos
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        # Create a square
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        # Create a rectangle
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(apple, fruit_rect)
        # Draw the rectangle
        # pygame.draw.rect(screen, (126, 166, 114), fruit_rect)


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.snake2 = SNAKE2()

    def update(self):
        self.snake2.move_snake2()
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.draw_soil()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()
        self.snake2.draw_snake2()

    def check_collision(self):
        if self.fruit.pos == self.snake2.body[0]:
            # reposition the fruit
            # add another block to snake
            self.fruit.randomize()
            self.snake2.add_Block2()

        if self.fruit.pos == self.snake.body[0]:
            # reposition the fruit
            # add another block to snake
            self.fruit.randomize()
            self.snake.add_Block()
            self.snake.bite_sound.play()
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_fail(self):
        # checks if snake touches the wall. Will change to infinity later.
        # checks if it touches itself
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
            elif block == self.snake2.body[0]:
                self.game_over()
        for block in self.snake2.body[1]:
            if block == self.snake.body[0]:
                self.game_over()
        if not 0 <= self.snake2.body[0].x <= cell_number or not 0 <= self.snake2.body[0].y <= cell_number:
            self.snake2.reset2()

    def game_over(self):
        self.snake.reset()
        self.snake2.reset2()

    def draw_soil(self):
        soil_color = (167, 209, 61)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        soil_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, soil_color, soil_rect)

            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        soil_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, soil_color, soil_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 60)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        apple_rect = apple.get_rect(midright=(score_rect.left, score_rect.centery))

        screen.blit(score_surface, score_rect)
        screen.blit(apple, apple_rect)


pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
game_font = pygame.font.Font('Snake_crawler/Font/Baby Chipmunk.ttf', 25)
# Apple Img
apple = pygame.image.load('Snake_crawler/Images/apple.png').convert_alpha()
# Bad Image
eagle = pygame.image.load('Snake_crawler/Images/apple.png').convert_alpha()
# Background Music
mixer.music.load('Snake_crawler/Music/background.wav')
mixer.music.play(-1)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)
main_game = MAIN()
options = ('up', 'down', 'left', 'right')

while True:
    path = random.choice(options)
    path_times = random.randint(0, 5)
    # colorx = random.randint(0,255)
    # colory = random.randint(0,255)
    # colorz = random.randint(0,255)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)

        if path == 'up':
            for i in range(path_times):
                if main_game.snake2.direction.y != 1:
                    main_game.snake2.direction = Vector2(0, -1)
        if path == 'down':
            for i in range(path_times):
                if main_game.snake2.direction.y != -1:
                    main_game.snake2.direction = Vector2(0, 1)
        if path == 'left':
            for i in range(path_times):
                if main_game.snake2.direction.x != 1:
                    main_game.snake2.direction = Vector2(-1, 0)
        if path == 'right':
            for i in range(path_times):
                if main_game.snake2.direction.x != -1:
                    main_game.snake2.direction = Vector2(1, 0)
    screen.fill((175, 215, 70))
    # fruit.draw_fruit()
    # snake.draw_fruit()
    main_game.draw_elements()

    pygame.display.update()
    clock.tick(60)
