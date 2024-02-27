import sys
import pygame
from settings import Settings
from abby import Abby
from dangan import Dangan

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings=Settings()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN) #set screen
        self.settings.screen_width=self.screen.get_rect().width #Because PyGame do NOT know what is the size of the monitor
        self.settings.screen_height=self.screen.get_rect().height
        pygame.display.set_caption("異星人襲来！！！")
        self.abby= Abby(self)
        self.dangan = pygame.sprite.Group()
        self.screen.fill(self.settings.bg_color)
    
    def _check_events(self):
        """react to mouse and keyboard"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                
            elif event.type == pygame.KEYUP: #when Key is released, then Boolean value will be False, Abby stop moving
                self._check_keyup_events(event)
                    
    def _check_keydown_events(self, event):
        "KEYDOWN"
        if event.key == pygame.K_RIGHT:
            """Move Abby to the right"""
            self.abby.moving_right = True #By update the Boolean value, Abby can move continuously.
        elif event.key == pygame.K_LEFT:
             """Move Abby to the left"""
             self.abby.moving_left = True #By update the Boolean value, Abby can move continuously.
        elif event.key == pygame.K_UP:
            """Move Abby to the UP"""
            self.abby.moving_up = True #By update the Boolean value, Abby can move continuously.
        elif event.key == pygame.K_DOWN:
            """Move Abby to the DOWN"""
            self.abby.moving_down = True #By update the Boolean value, Abby can move continuously.
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_dangan()
             
    def  _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.abby.moving_right = False   
        elif event.key == pygame.K_LEFT:
            self.abby.moving_left = False   
        elif event.key == pygame.K_UP:
            self.abby.moving_up = False   
        elif event.key == pygame.K_DOWN:
            self.abby.moving_down = False
    
    def _fire_dangan(self):
        """create a Dangan"""
        if len(self.dangan) < 3:
            new_dangan = Dangan(self)
            self.dangan.add(new_dangan) 
        
    def run_game(self):
        while True:
            self._check_events()   
            self.abby.update()
            self.dangan.update()
            self._update_dangan()
            self._update_screen()          
            self.clock.tick(90) #frequency of the game
            
    def _update_dangan(self):
        """Updating the position of bullets and delete the ones who are disappeared"""
        self.dangan.update()
        
        for dangan in self.dangan.copy():
            if dangan.rect.bottom <= 0:
                self.dangan.remove(dangan)
   
    def _update_screen(self):
        """Update images on the screen and switch it to the new screen"""
        self.screen.fill(self.settings.bg_color)
        for dangan in self.dangan.sprites():
            dangan.draw_bullets()      
        self.abby.blitme() 
        
        pygame.display.flip()
            
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()