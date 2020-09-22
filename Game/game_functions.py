import sys
import pygame


# 监测事件
def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, ship):
    # 每次循环时，都会重绘屏幕
    # 填充背景色
    screen.fill(ai_settings.bg_color)

    # 绘制飞船
    ship.blitme()

    # 让最近绘制的屏幕可见，不断更新屏幕
    pygame.display.flip()
