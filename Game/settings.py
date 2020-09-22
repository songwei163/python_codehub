# 用于设置的类

class Settings:
    def __init__(self):
        # 窗口宽度
        self.screen_width = 1200
        # 窗口高度
        self.screen_height = 800
        # 窗口背景颜色
        self.bg_color = (230, 230, 230)
        # 飞船设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        # 子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3  # 限制子弹数量
        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 50
        # 1表示右移，-1表示左移
        self.fleet_direction = 1
        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        # 外星人点数提高的速度
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction为1向右，-1向左
        self.fleet_direction = 1

        # 计分
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)
