import pygame
from random import randint
from pygame.surface import Surface

init_direction = 'right'

class vector2:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class snake:
    def __init__(self, head_xy: vector2, body: list):
        self.head = head_xy
        self.body = body

    def draw_snake(self, head_img, color, screen: Surface, blocksize: int):
        for part in self.body[:-1]:
            pygame.draw.rect(screen, color, \
              [part.x * blocksize, part.y * blocksize,\
               blocksize - 1, blocksize - 1])
        screen.blit(head_img, (self.head.x * blocksize, self.head.y * blocksize))

class gameplay:
    def __init__(self, max_step: list, blocksize: int, gameover = False):
        self.difficulty = 10
        self.score = 0
        self.level = 0
        self.gameover = gameover
        self.steps = max_step
        self.blocksize = blocksize
        head_pos = vector2(max_step[0] // 2, max_step[1] // 2)
        self.slither = snake(head_pos, [head_pos])
        self.velocity = vector2(1, 0)
        self.direction = init_direction
        self.apple = vector2(randint(0, self.steps[0] - 1),\
                             randint(0, self.steps[1] - 1))

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and self.direction != "right":
                    self.direction = "left"
                    self.velocity = vector2(-1, 0)
                elif event.key == pygame.K_d and self.direction != "left":
                    self.direction = "right"
                    self.velocity = vector2(1, 0)
                elif event.key == pygame.K_w and self.direction != "down":
                    self.direction = "up"
                    self.velocity = vector2(0, -1)
                elif event.key == pygame.K_s and self.direction != "up":
                    self.direction = "down"
                    self.velocity = vector2(0, 1)

        if self.slither.head.x == self.steps[0] - 1 and self.direction == "right":
            self.slither.head.x = - 1
        elif self.slither.head.x == 0 and self.direction == "left":
            self.slither.head.x = self.steps[0]
        elif self.slither.head.y == self.steps[1] - 1 and self.direction == "down":
            self.slither.head.y = - 1
        elif self.slither.head.y == 0 and self.direction == "up":
            self.slither.head.y = self.steps[1]

        self.slither.head = vector2(self.slither.head.x + self.velocity.x, \
                                    self.slither.head.y + self.velocity.y)

        self.slither.body.append(vector2(self.slither.head.x, self.slither.head.y))

        if (self.slither.head.x, self.slither.head.y) \
                                            == (self.apple.x, self.apple.y):

            self.apple = vector2(randint(0, self.steps[0] - 1), \
                                 randint(0, self.steps[1] - 1))

            self.slither.body.insert(0, self.slither.body[0])
            self.score += 1

            if self.score % self.difficulty == 0:
                self.level+= 1

        if len(self.slither.body) > 1:
            self.slither.body = self.slither.body[1:]

        for part in self.slither.body[:-1]:
            if (self.slither.head.x, self.slither.head.y) == (part.x, part.y):
               self.gameover = True

    def draw(self, snake_head, snake_color, apple_img, screen: Surface):
        if self.direction == 'right':
            head = pygame.transform.rotate(snake_head, 270)
        if self.direction == 'left':
            head = pygame.transform.rotate(snake_head, 90)
        if self.direction == 'up':
            head = snake_head
        if self.direction == 'down':
            head = pygame.transform.rotate(snake_head, 180)
        self.slither.draw_snake(head, snake_color, screen, self.blocksize)
        screen.blit(apple_img, (self.apple.x * self.blocksize, self.apple.y * self.blocksize))
