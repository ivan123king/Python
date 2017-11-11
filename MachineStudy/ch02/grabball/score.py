__author__ = 'lenovo'
#coding=utf-8
import pygame
from pygame.sprite import Sprite

class Score(Sprite):
    def __init__(self,ai_settings,screen):
        super(Score,self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0,0,ai_settings.score_width,ai_settings.score_height)