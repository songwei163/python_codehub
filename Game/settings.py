# 用于设置的类

class Settings:
    def __init__(self):
        # 窗口宽度
        self.screen_width = 1200
        # 窗口高度
        self.screen_height = 800
        # 窗口背景颜色
        self.bg_color = (230, 230, 230)
        # 飞船速度设置
        self.ship_speed_factor = 1.5
        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3  # 限制子弹数量
        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # 1表示右移，-1表示左移
        self.fleet_direction = 1
