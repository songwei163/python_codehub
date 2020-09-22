import pygame


# 飞船类
class Ship:
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')  # 加载图像
        self.rect = self.image.get_rect()  # 获取飞船的属性
        self.screen_rect = screen.get_rect()  # 存储屏幕的属性

        self.rect.centerx = self.screen_rect.centerx  # 将飞船放到x轴中间
        self.rect.bottom = self.screen_rect.bottom  # 将飞船放到屏幕下边缘

        # center属性用小数
        self.center = float(self.rect.centerx)

        # 左移标志
        self.moving_left = False
        # 右移标志
        self.moving_right = False

    # 如果右移标志打开，就向右移动
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # 根据self.center的值更新x轴坐标
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)  # 根据飞船的属性绘制图像

    def center_ship(self):
        # 让飞船在屏幕上居中
        self.center = self.screen_rect.centerx
