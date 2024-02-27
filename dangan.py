import pygame
from pygame.sprite import Sprite
#testcomment

class Dangan(Sprite):
    
    def __init__(self,ai_game):
        '''Create a bullet at the current Abby's position'''
        pygame.sprite.Sprite.__init__(self)
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = (245, 192, 113)
        
        #Create a rect at (0,0) and set the correct position
        self.rect = pygame.Rect(0,0,self.settings.dangan_width, self.settings.dangan_height)
        self.rect.topleft= ai_game.abby.rect.topleft
        
    def update(self):
        '''move bullet to the top'''
        #update position of bullets
        self.rect.y -= 4
        #display where the bullet-rect is
        
    def draw_bullets(self):
        '''draw the bullet on the screen'''
        pygame.draw.rect(self.screen, self.color, self.rect) 