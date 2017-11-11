__author__ = 'lenovo'
#coding=utf-8
import pygame
from pygame.sprite import Group
import sys
import random

from ch02.grabball.ball import Ball
from ch02.grabball.hand import Hand

#不断更新屏幕内容，即不断重绘屏幕
def update_screen(ai_settings,screen,hand,balls):
    screen.fill(ai_settings.bg_color)#绘制屏幕背景色
    hand.blitme()#在屏幕上绘制飞船
    balls.draw(screen)
    pygame.display.flip()#让最近绘制的屏幕可见

#监听按键事件
def check_keydown_events(event,ai_settings,screen,hand):
    if event.key == pygame.K_RIGHT:
        hand.moving_right = True
    elif event.key == pygame.K_LEFT:
        hand.moving_left = True
    elif event.key == pygame.K_q:#按Q退出程序
        sys.exit()

#监听松开键事件
def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


#监听事件
def check_events(ai_settings,screen,hand):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,hand)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,hand)

def create_ball(ai_settings,screen,balls):
     #create ball group
    ball = Ball(ai_settings,screen)
    ball.rect.x = random.random()*(screen.get_rect().width-ball.rect.width)
    balls.add(ball)

def update_ball(ai_settings,screen,hand,balls):
    '''检查是否有位于屏幕边缘，更新所有球中所有每个球位置'''
    balls.update()#调用组中update会自动调用每一个ball中继承实现的update方法
    #检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(hand,balls) or check_ball_edge(screen,balls):
        balls.empty()
        create_ball(ai_settings,screen,balls)

#检测球是否已掉落屏幕边缘
def check_ball_edge(screen,balls):
    screen_rect = screen.get_rect()
    for ball in balls.copy():
        if ball.rect.bottom > screen_rect.bottom:
            return True








