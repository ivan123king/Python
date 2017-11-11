__author__ = 'lenovo'
#coding=utf-8
import pygame
from pygame.sprite import Sprite

class Ball(Sprite):
    def __init__(self,ai_settings,screen):
        """ 初始化并设置球的位置 """
        super(Ball,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/ball.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)

    def blitme(self):
        '''在指定位置绘制球'''
        self.screen.blit(self.image,self.rect)

     #更新坐标
    def update(self):
        '''向右移动外星人'''
        self.y +=self.ai_settings.ball_speed
        self.rect.y = self.y

