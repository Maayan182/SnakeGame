import pygame
import time
import random
pygame.init()
class Snake:
    def __init__(self,fieldSize):
        self.body = [[fieldSize/2, fieldSize/2],[fieldSize/2 - 10, fieldSize/2]]
        self.direction = pygame.K_RIGHT
        self.blockSize = 10
        self.fieldSize = fieldSize

    def change_direction(self, new):
        if new == pygame.K_LEFT and self.direction == pygame.K_RIGHT:
            return
        elif new == pygame.K_RIGHT and self.direction == pygame.K_LEFT:
            return
        elif new == pygame.K_UP and self.direction == pygame.K_DOWN:
            return
        elif new == pygame.K_DOWN and self.direction == pygame.K_UP:
            return
        else:
            self.direction = new
            return

    def move(self):
        head = self.body[0][:]
        if self.direction == pygame.K_RIGHT:
            head[0] += self.blockSize
        elif self.direction == pygame.K_LEFT:
            head[0] -= self.blockSize
        elif self.direction == pygame.K_DOWN:
            head[1] += self.blockSize
        elif self.direction == pygame.K_UP:
            head[1] -= self.blockSize
        del(self.body[-1])
        self.body.insert(0, head)

    def level_up(self):
        tail = self.body[-1]
        if self.direction == pygame.K_RIGHT:
            tail[0] -= self.blockSize
        elif self.direction == pygame.K_LEFT:
            tail[0] += self.blockSize
        elif self.direction == pygame.K_DOWN:
            tail[1] -= self.blockSize
        elif self.direction == pygame.K_UP:
            tail[1] += self.blockSize
        self.body.append(tail)

    def chekLost(self):
        if self.body[0][0] > self.fieldSize or self.body[0][0] < 0:
            return True
        elif self.body[0][1] > self.fieldSize or self.body[0][1] < 0:
            return True
        for part in self.body[1:]:
            if self.body[0] == part:
                return True
        return False

    def didEat(self,point):
        if self.body[0] == point:
            self.level_up()
            return True
        else:
            return False

def generateApplePoint(fieldSize,blockSize):
    x = round(random.randrange(0, fieldSize - blockSize) / 10.0) * 10.0
    y = round(random.randrange(0, fieldSize - blockSize) / 10.0) * 10.0
    return [x,y]

def drawSnake(my_snake,display):
    for part in my_snake.body:
        if part == my_snake.body[0]:
            pygame.draw.rect(display, "red", [part[0], part[1], my_snake.blockSize, my_snake.blockSize])
        else:
            pygame.draw.rect(display, "blue", [part[0], part[1], my_snake.blockSize, my_snake.blockSize])

def game():
    fieldsize = 400
    display = pygame.display.set_mode((fieldsize, fieldsize))
    pygame.display.update()
    gameOver = False
    game_close = False
    my_snake = Snake(fieldsize)
    apple = generateApplePoint(fieldsize,my_snake.blockSize)


    while not gameOver:
        while game_close:
            display.fill("white")
            msg = pygame.font.SysFont(None, 30).render("You Lost! Press Q-Quit or P-Play Again", True, "red")
            display.blit(msg,[fieldsize/40,100])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        game_close = False
                    if event.key == pygame.K_p:
                        game()
                if event.type == pygame.QUIT:
                    gameOver = True
                    game_close = False

        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                my_snake.change_direction(event.key)

        display.fill("black")
        pygame.draw.rect(display, "green", [apple[0], apple[1], my_snake.blockSize, my_snake.blockSize])
        my_snake.move()
        drawSnake(my_snake,display)
        if my_snake.didEat(apple):
            apple = generateApplePoint(fieldsize,my_snake.blockSize)
        game_close = my_snake.chekLost()
        pygame.time.Clock().tick(15)
        pygame.display.update()



    pygame.quit()
    quit()


if __name__ == "__main__":
    game()







