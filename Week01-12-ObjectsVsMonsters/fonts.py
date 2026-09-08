import pygame.font as font
import os.path as path

font.init()


FONT_PATH = path.join(path.dirname(__file__),'assets','fonts','pixel.ttf')

FONTS   = {'normal': font.Font(FONT_PATH, 36),
           'large':  font.Font(FONT_PATH, 72), 
           'small':  font.Font(FONT_PATH, 24), 
           'tiny':   font.Font(FONT_PATH, 10), 
           'title':  font.Font(FONT_PATH, 96)}

COLOURS = {'white':        (255, 255, 255),
           'black':        (0,     0,   0),
           'red':          (177,   7,   7),
           'white_purple': (239, 190, 255),
           'grey_purple':  (163, 120, 177),
           'purple':       (125,   0, 125),
           'magenta':      (230,   0, 220),
           'green':        ( 78, 172,   0),
           'grey':         ( 54,   54, 49),
           }
