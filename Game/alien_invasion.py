import sys
import pygame

from settings import Settings
from ship import Ship


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    # 设置窗口名称
    pygame.display.set_caption('Alien Invasion')
    # 构造一艘飞船
    ship = Ship(screen)
    # 开启游戏主循环
    while True:
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 每次循环时，都会重绘屏幕
        # 填充背景色
        screen.fill(ai_settings.bg_color)

        # 绘制飞船
        ship.blitme()

        # 让最近绘制的屏幕可见，不断更新屏幕
        pygame.display.flip()


run_game()
