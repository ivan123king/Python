__author__ = 'lenovo'
#coding=utf-8
class Settings():
    def __init__(self):
        self.screen_width = 900
        self.screen_height = 500
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1.5
        self.ship_limit = 3#玩家拥有飞船数生命值）
        #子弹设置
        self.bullet_speed_factor=1
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3 #子弹限制，最多同屏存在子弹数目
        #外星人设置
        self.alien_speed_factor = 6 # 水平移动速度
        self.fleet_drop_speed = 10 # 垂直移动速度
        self.fleet_direction = 1 #fleet_direction为1表示向右移动，为-1表示向左移动