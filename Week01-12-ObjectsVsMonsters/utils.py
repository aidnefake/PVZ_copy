import pygame
import os


def load_sprite(name, scale = 1, alpha = True):
     '''
          Loads given sprite object as a pygame surface.
     '''
     path = os.path.join(os.path.dirname(__file__), 'assets', 'sprites', f'{name}.png')
     sprite = pygame.image.load(path)

     if alpha:
          sprite = sprite.convert_alpha()
     else:
          sprite = sprite.convert()
     
     if scale == 1:
          return sprite
     else:
          return pygame.transform.scale_by(sprite,scale)

def write(surface, msg, pos, font, colour, align = 'left'):
     '''
          Writes text onto a given surface with given parameters.
     '''
     text = font.render(msg, True, colour)
     text_box = text.get_rect()
     if align == 'center':
          text_box.center = pos
     elif align == 'left':
          text_box.topleft = pos
     elif align == 'midleft':
          text_box.midleft = pos
     elif align == 'midright':
          text_box.midright = pos
     elif align == 'right':
          text_box.topright = pos


     surface.blit(text, text_box)

def alpha_fill(surface, colour, alpha):
     '''
          Draws a layer with specified colour and alpha value onto a given surface.
     '''
     layer = pygame.Surface(surface.get_size())
     layer.fill(colour)
     layer.set_alpha(alpha)
     surface.blit(layer, (0,0))