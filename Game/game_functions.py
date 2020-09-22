import sys
import pygame

def check_keydown_events(event, ship):
    if event.key == pygame.K_RIGHT:
        # 按下右键时，打开右移标志
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 按下左键时，打开左移标志
        ship.moving_left = True


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        # 松开右键时，关闭右移标志
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # 松开左键时，关闭左移标志
        ship.moving_left = False


# 监测事件
def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship):
    # 每次循环时，都会重绘屏幕
    # 填充背景色
    screen.fill(ai_settings.bg_color)

    # 绘制飞船
    ship.blitme()

    # 让最近绘制的屏幕可见，不断更新屏幕
    pygame.display.flip()
