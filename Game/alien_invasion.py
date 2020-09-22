import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    # 设置窗口名称
    pygame.display.set_caption('Alien Invasion')
    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    # 构造一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个外星人
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 开启游戏主循环
    while True:
        # 监测事件
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            # 更新飞船位置
            ship.update()

            # 更新子弹位置
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)

            # 更新外星人位置
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        # 绘制屏幕
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
