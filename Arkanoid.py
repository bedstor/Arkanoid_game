import pygame

pygame.init()
def main():
    window = pygame.display.set_mode((500,500))
    back = (200,255,255)
    window.fill(back)
    clock = pygame.time.Clock()
    game = True

    class Area():
        def __init__(self, x, y, width, height, color):
            self.rect = pygame.Rect(x,y,width,height)
            self.fill_color = color
        def fill(self):
            pygame.draw.rect(window, self.fill_color, self.rect)
        def colliderect(self, rect):
            return self.rect.colliderect(rect)

    class Label(Area):
        def set_text(self,text,size,color):
            self.image = pygame.font.SysFont('Verdana',size).render(text, True, color)
        def draw(self,shift_x, shift_y):
            self.fill()
            window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

    class Picture(Area):
        def __init__(self, filename, x, y, width, height):
            super().__init__(x, y, width, height, back)
            self.image = pygame.image.load(filename)

        def draw(self):
            self.fill()
            window.blit(self.image, (self.rect.x, self.rect.y))

    platform = Picture('platform.webp', 200, 400, 100, 25)
    ball = Picture('ball.webp', 170, 270, 50, 50)
    monsters = list()
    speed_x = 3
    speed_y = 3
    x_start = 5
    y_start = 5
    n = 9
    for j in range(3):
        x = x_start + 27 * j
        y = y_start + 55 * j
        for i in range(n):
            monsters.append(Picture('enemy.webp', x, y, 50, 50))
            x += 55
        n -= 1
    move_right = False
    move_left = False

    while game:
        for m in monsters:
            m.fill()
        platform.fill()
        ball.fill()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.colliderect(platform.rect):
            speed_y = -3
        if ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x > 450 or ball.rect.x < 0:
            speed_x *= -1
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    move_right = True
                if event.key == pygame.K_LEFT:
                    move_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    move_right = False
                if event.key == pygame.K_LEFT:
                    move_left = False
        if move_right and platform.rect.x < 400:
            platform.rect.x += 3
        elif move_left and platform.rect.x > 0:
            platform.rect.x -= 3
        for m in monsters:
            m.draw()
            if m.colliderect(ball.rect):
                monsters.remove(m)
                m.fill()
                speed_y *= -1
        if len(monsters) == 0:
            win_text = Label(150, 150, 50, 50, back)
            win_text.set_text('YOU WIN', 60, (0, 255, 0))
            win_text.draw(0, 0)
            game = False
        platform.draw()
        ball.draw()
        
        if ball.rect.y > platform.rect.y + 20:
            time_text = Label(150, 170, 50, 50, back)
            time_text.set_text('YOU LOSE', 60, (255,0,0))
            time_text.draw(0, 0)
            game = False    
        pygame.display.update()
        clock.tick(40) 


if __name__ == '__main__':
    main()