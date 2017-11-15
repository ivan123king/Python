__author__ = 'lenovo'
#coding=utf-8
class Settings():
    def __init__(self):
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230,230,230)
        self.ship_limit = 3#玩家拥有飞船数生命值）
        #子弹设置

        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3 #子弹限制，最多同屏存在子弹数目
        #外星人设置
        self.fleet_drop_speed = 10 # 垂直移动速度


        #以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        #外星人点数的提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """
        初始化随游戏进行而变化的设置
        :return:
        """
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1# 水平移动速度
        self.fleet_direction = 1 #fleet_direction为1表示向右移动，为-1表示向左移动
        #计分
        self.alien_points = 50

    def increase_speed(self):
        """
        提高速度设置
        :return:
        """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points*self.score_scale)