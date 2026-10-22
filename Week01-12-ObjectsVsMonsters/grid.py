'''
Keep this code for future use:

# Coordinates for unit placement
self.TILE_COORDS = [[(118 + 70*i,105) for i in range(num_cols)],
                    [(102 + 74*i,160) for i in range(num_cols)],
                    [(86  + 78*i,220) for i in range(num_cols)],
                    [(68  + 83*i,285) for i in range(num_cols)],
                    [(52  + 87*i,355) for i in range(num_cols)]
                    ]
'''

from models import *
from pygame.math import Vector2

TILE_RADIUS = 25

class Grid:
    def __init__(self, rows, cols, summon_x):
        self.tiles = [[None for _ in range(cols)] for _ in range(rows)]

        self.TILE_COORDS = [[(118 + 70 * i, 105) for i in range(cols)],
                            [(102 + 74 * i, 160) for i in range(cols)],
                            [(86 + 78 * i, 220) for i in range(cols)],
                            [(68 + 83 * i, 285) for i in range(cols)],
                            [(52 + 87 * i, 355) for i in range(cols)]
                            ]
        self.monsters = [set() for _ in range(rows)]
        self.projectiles = set()

        self.rows = rows
        self.cols = cols

        self.summon_x = summon_x

    def update(self):
        energy_mods = 0
        dead_monsters = set()
        dead_projectiles = set()

        for row in range(self.rows):
            #update units
            for col in range(self.cols):
                if not self._is_empty(row,col):
                    #energy mod for energy producing units
                    energy_mod = self.tiles[row][col].update(self.monsters[row])

                    if energy_mod:
                        energy_mods +=energy_mod

                    if self.tiles[row][col].health<=0:
                        self.tiles[row][col] = None

            #monster update
            for monster in self.monsters[row]:
                monster.update(self.tiles[row], self.TILE_COORDS[row])
                if monster.health <= 0:
                    dead_monsters.add(monster)

        for projectile in self.projectiles:
            projectile.update()
            if projectile.elapsed >= projectile.lifespan:
                dead_projectiles.add(projectile)

        for row in self.monsters:
            row-=dead_monsters

        self.projectiles -= dead_projectiles

        return energy_mods

    def _is_empty(self, row, col):
        return self.tiles[row][col] is None

    def draw(self, surface):
        for row in self.tiles:
            for tile in row:
                if tile:
                    tile.draw(surface)

        for row in self.monsters:
            for monster in row:
                monster.draw(surface)

        for projectile in self.projectiles:
            projectile.draw(surface)

    def _in_tile(self, pos, row, col):
        scale = 1 + 0.1 * row

        return Vector2(pos).distance_to(self.TILE_COORDS[row][col]) < TILE_RADIUS*scale

    def _deploy_unit(self, row, col, unit_type:str):
        scale = 1 + 0.1 * row

        match unit_type:
            case "microwave":
                self.tiles[row][col] = Microwave(self.TILE_COORDS[row][col], self.projectiles.update, scale)
            case "blender":
                self.tiles[row][col] = Blender(self.TILE_COORDS[row][col], self.projectiles.update, scale)
            case "toaster":
                self.tiles[row][col] = Toaster(self.TILE_COORDS[row][col], self.projectiles.update, scale)

        SFX["deploy"].play()

    def deploy_monster(self, row, monster_type:str):
        scale = 1 + 0.1 * row

        match monster_type:
            case "fortified":
                self.monsters[row].add(Monster((self.summon_x, self.TILE_COORDS[row][0][1]),
                                               scale = scale,
                                               sprites=("fortified_monster_a",
                                                        "fortified_monster_b",
                                                        "fortified_monster_eat")))
            case "normal":
                self.monsters[row].add(Monster((self.summon_x, self.TILE_COORDS[row][0][1]), scale = scale))

    def on_click(self, mouse_pos):
        for row in self.tiles:
            for unit in row:
                if unit and unit.clicked(mouse_pos):
                    return unit.on_clicked()