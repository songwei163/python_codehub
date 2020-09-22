import pygame


# 飞船类
class Ship:
    def __init__(self, screen):
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')  # 加载图像
        self.rect = self.image.get_rect()  # 获取飞船的属性
        self.screen_rect = screen.get_rect()  # 存储屏幕的属性

        self.rect.centerx = self.screen_rect.centerx  # 将飞船放到x轴中间
        self.rect.bottom = self.screen_rect.bottom  # 将飞船放到屏幕下边缘

    def blitme(self):
        self.screen.blit(self.image, self.rect)  # 根据飞船的属性绘制图像
