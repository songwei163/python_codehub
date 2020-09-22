import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_setting, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_setting = ai_setting

        # 加载外星人图像，并设置rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都出现在左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
