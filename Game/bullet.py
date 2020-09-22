import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        # 在0，0处绘制子弹
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        # 将位置调整到飞船顶部的中间位置
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储高度，用小数
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    # 更新子弹的位置，向上移动
    def update(self):
        # 屏幕左上角坐标(0,0)
        # 屏幕右下角坐标(x,y)
        self.y -= self.speed_factor  # 更新表示子弹位置的小数值
        self.rect.y = self.y  # 实际更改属性

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
