import sys
import pygame

from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        # 按下右键时，打开右移标志
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 按下左键时，打开左移标志
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        # 松开右键时，关闭右移标志
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # 松开左键时，关闭左移标志
        ship.moving_left = False


# 监测事件
def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    # 每次循环时，都会重绘屏幕
    # 填充背景色
    screen.fill(ai_settings.bg_color)

    # 在飞船和为行人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 绘制飞船
    ship.blitme()

    # 让最近绘制的屏幕可见，不断更新屏幕
    pygame.display.flip()


def update_bullets(bullets):
    # 对编组调用update()相当于对每个精灵调用update()
    bullets.update()

    # 删除已消失的子弹
    # 遍历其副本，删除
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))


def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullet_allowed:
        # 创建一个子弹，并将其加入编组中
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
