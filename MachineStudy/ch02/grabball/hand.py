__author__ = 'lenovo'
#coding=utf-8

import pygame

class Hand():
    def __init__(self,ai_settings,screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/hand.png')
        self.rect = self.image.get_rect() # let image as a rectangle to compute it's width ,height
        self.screen_rect = screen.get_rect() # get screen's size

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.centerx = float(self.screen_rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.hand_speed
        elif self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.hand_speed
        self.rect.centerx = self.centerx

    #draw ship on screen
    def blitme(self):
        self.screen.blit(self.image,self.rect)
