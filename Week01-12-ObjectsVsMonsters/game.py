import pygame
import random

from models import *
from utils import *
from fonts import FONTS, COLOURS
from audio import SFX


class Game:
    def __init__(self):

        # pygame setup:
        pygame.init()
        # 16:9 aspect ratio
        self.width  = 16 * 50 # 800
        self.height =  9 * 50 # 450
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Objects Vs Monsters')

        self.clock = pygame.time.Clock()
        
        # loading assets:
        self.background = load_sprite('bg2', alpha = False)
        self.hud = {'energy_back' :load_sprite('hud_energy_back'),
                    'energy_front':load_sprite('hud_energy_front'),
                    'energy_bar'  :load_sprite('energy_bar'),
                   }   

        self.state = 'game'

    def main_loop(self):

        while True:
            self._process_input()
            self._process_game_logic()
            self._draw()
            self.clock.tick(60)

    def _process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

    def _process_game_logic(self):
        pass

    def _draw(self):
        self.screen.blit(self.background,(0,0))

        pygame.display.update()