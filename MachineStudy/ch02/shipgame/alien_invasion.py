__author__ = 'lenovo'
#coding=utf-8
import pygame;
from pygame.sprite import  Group

from ch02.shipgame import settings
from ch02.shipgame.ship import Ship
from ch02.shipgame.game_stats import GameStats
from ch02.shipgame.button import Button
from ch02.shipgame.scoreboard import Scoreboard
from ch02.shipgame import game_functions as gf


#运行游戏，此飞船游戏入口
def run_game():
    pygame.init();
    ai_settings = settings.Settings();
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height));#set window size
    pygame.display.set_caption('Alien Invasion')#set window title
    #创建play按钮
    play_button = Button(ai_settings,screen,"Play")
    #创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    ship = Ship(ai_settings,screen)
    #创建一个用于存储子弹的编组
    bullets = Group()
    #创建一个用于存储外星人的编组
    aliens = Group()
    #创建一个外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens);

    #创建存储游戏统计信息的实例，并创建计分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)

    while True:
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)#按键等事件检查
        if stats.game_active:
            ship.update()#不断更新飞船的位置坐标
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)#不断更新子弹坐标，已经将不在屏幕内的子弹从组内删除
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)#不断重绘屏幕，飞船，子弹

run_game()

# write by myself, just want test the pygame's key code
# def event_code():
#     pygame.init();
#     ai_settings = settings.Settings();
#     screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height));
#     pygame.display.set_caption('Alien Invasion')
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.KEYDOWN:
#                 print(event.key)
#
#             if event.type == pygame.QUIT:
#                 sys.exit()
#         pygame.display.flip()
# event_code();