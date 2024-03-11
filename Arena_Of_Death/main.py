import pygame, sys
from setting import *
from level import Level



class Game:
    def __init__(self):
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Arena Of Death')
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill((148, 126, 98))
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()


# if __name__ == '__main__':: Это условие проверяет, запущен ли скрипт напрямую (а не импортирован как
# модуль в другом скрипте). Когда вы запускаете скрипт напрямую, переменная __name__ устанавливается
# в '__main__'.
# game = Game(): Создается объект класса Game. Это вызывает конструктор __init__ класса Game, который
# инициализирует необходимые параметры, такие как экран и часы.
# game.run(): Запускается основной игровой цикл, который находится в методе run класса Game. В этом цикле
# обрабатываются события, обновляется экран, и игра продолжает выполняться до тех пор, пока пользователь не
# закроет окно.