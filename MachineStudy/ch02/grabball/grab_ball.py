__author__ = 'lenovo'
#coding=utf-8
import pygame
from pygame.sprite import Group
import sys
from ch02.grabball.settings import Settings
from ch02.grabball.hand import Hand
from ch02.grabball.ball import Ball
from ch02.grabball import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height));#set window size
    pygame.display.set_caption('Grab Ball')#set window title

    hand = Hand(ai_settings,screen)
    balls = Group()
    gf.create_ball(ai_settings,screen,balls)
    while True:
        gf.check_events(ai_settings,screen,hand)
        hand.update()#不断更新飞船的位置坐标
        gf.update_ball(ai_settings,screen,hand,balls)
        gf.update_screen(ai_settings,screen,hand,balls)#不断重绘屏幕，飞船，子弹

run_game()