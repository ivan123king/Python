__author__ = 'lenovo'
#coding=utf-8
import sys
import pygame
from time import sleep
from ch02.shipgame.bullet import  Bullet
from ch02.shipgame.alien import  Alien

#监听按键事件
def check_keydown_events(event,ai_settings,stats,sb,screen,ship,aliens,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,stats,screen,ship,bullets)#发射子弹
    elif event.key == pygame.K_q:#按Q退出程序
        sys.exit()
    elif event.key == pygame.K_p and not stats.game_active:#按P开始游戏
        start_game(ai_settings,screen,stats,sb,ship,aliens,bullets)


#发射子弹的方法
def fire_bullet(ai_settings,stats,screen,ship,bullets):
    '''如果还没有达到限制，就发射一颗子弹'''
    #创建一颗子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed and stats.game_active:#and stats.game_active 这个是为了解决游戏还没有开始按下空格键绘制了子弹的bug
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

#监听松开键事件
def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
#监听事件
def check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,stats,sb,screen,ship,aliens,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)

def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    """ 在玩家单击Play时开始游戏"""
    button_checked = play_button.rect.collidepoint(mouse_x,mouse_y);
    if button_checked and not stats.game_active:#位置检测（案例第三种碰撞检测）
        start_game(ai_settings,screen,stats,sb,ship,aliens,bullets)

def start_game(ai_settings,screen,stats,sb,ship,aliens,bullets):
     #重置游戏设置
     ai_settings.initialize_dynamic_settings()
      #隐藏光标
     pygame.mouse.set_visible(False)
     stats.game_active = True
     #重置游戏统计信息
     stats.reset_stats()
     #重置计分牌图像
     sb.prep_score()#解决重新开始游戏时，玩家得分不重绘，导致需要击中一个外星人才会重绘score_image
     sb.prep_high_score()
     sb.prep_level()
     sb.prep_ships()
     #清空外星人列表和子弹列表
     aliens.empty()
     bullets.empty()
     #创建一群新外星人，并让飞船居中
     create_fleet(ai_settings,screen,ship,aliens)
     ship.center_ship()

#不断更新屏幕内容，即不断重绘屏幕
def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):
    screen.fill(ai_settings.bg_color)#绘制屏幕背景色
    #在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()#在屏幕上绘制飞船
    aliens.draw(screen)#让编组自动绘制编组内每个外星人，绘制位置由元素rect决定
    #显示得分
    sb.show_score()
    #如果游戏处于非活动状态，绘制play按钮
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()#让最近绘制的屏幕可见


def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
    '''更新子弹的位置，并删除已消失的子弹'''
    #更新子弹位置
    bullets.update()
    #删除已消失子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
     #检查是否有子弹击中外星人
    check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets)

def check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets):
    #检查是否有子弹击中外星人
    # 如果击中外星人，删除相应子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)#第一True表示子弹在碰到外星人后消失，第二个True表示外星人消失
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points*len(aliens)
            sb.prep_score()
        check_high_score(stats,sb)
    if len(aliens)==0:
        #删除现有子弹并新建一群外星人
        bullets.empty()
        ai_settings.increase_speed()
        #提高等级
        stats.level +=1
        sb.prep_level()
        create_fleet(ai_settings,screen,ship,aliens)

def check_high_score(stats,sb):
    """ 检查是否诞生了新的最高得分
    :param stats:
    :param sb:
    :return:
    """
    if stats.score>stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

#计算屏幕可以容纳多少行外星人
def get_number_rows(ai_settings,ship_height,alien_height):
    available_space_y = (ai_settings.screen_height-(3*alien_height)-ship_height)
    number_rows = int(available_space_y/(2*alien_height))#距离飞船留出一定空白以便射击
    return number_rows

#计算一行可以容纳多少外星人   返回一行外星人数量
def get_number_aliens_x(ai_settings,alien_width):
    available_space_x = ai_settings.screen_width - 2*alien_width#可用空间
    number_aliens_x = int(available_space_x/(2*alien_width))#容纳外星人数量
    return number_aliens_x

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    #创建一个外星人并将其加入当前行
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width+2*alien_width*alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height+2*alien.rect.height*row_number
    aliens.add(alien)

#创建外星人群
def create_fleet(ai_settings,screen,ship,aliens):
    '''创建外星人群 '''
   #创建一个外星人，并计算每行可以容纳多少个外星人
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)

    #创建外星人群
    #多少行
    for row_number in range(number_rows):
        #每行多少外星人
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)


def update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets):
    '''检查是否有外星人位于屏幕边缘，更新外星人群中所有外星人位置'''
    check_fleet_edges(ai_settings,aliens)
    aliens.update()#调用组中update会自动调用每一个alien中继承实现的update方法
    #检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)
    #检查是否有外星人到达屏幕底端
    check_aliens_bottom(ai_settings,screen,stats,sb,ship,aliens,bullets)

def ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """响应被外星人撞到的飞船"""
    if stats.ships_left > 0:
        #将ships_left减1
        stats.ships_left -= 1
        #更新计分牌
        sb.prep_ships()
        #清空外星列表和子弹列表
        aliens.empty()
        bullets.empty()
        #创建一群新的外星人，并将飞船放到屏幕底端中央
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
        #暂停 单位秒
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


#检查外星人群是否撞到了屏幕边缘
def check_fleet_edges(ai_settings,aliens):
    '''有外星人到达边缘时采取相应的措施'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def check_aliens_bottom(ai_settings,screen,stats,sb,ship,aliens,bullets):
    '''检查是否有外星人到达了屏幕底端'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #像飞船被撞到一样处理
            ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)
            break

def change_fleet_direction(ai_settings,aliens):
    '''将整群外星人下移，并改变它们的方向'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

