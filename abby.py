import pygame

class Abby:
    def __init__(self, ai_game):
        """Initinal position of Abby-chan"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        #load Abby-chan Image
        self.image = pygame.image.load("abbychanout.bmp")
        self.rect = self.image.get_rect() #rect stands for rectangle the x value and y values will be changed for moving
        
        #Abby-chan will be appeared at the middle-bottom
        self.rect.midbottom = self.screen_rect.midbottom
        
        # Abby won't move in the beginning
        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False
    
    def update(self):
        """Abby will move depending on which key is pressed"""
        #update coord x by settings
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 2
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 2
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 2
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 2
        
    def blitme(self):
        '''Draw Abby-chan at the desired position'''
        self.screen.blit(self.image, self.rect)