from csv import reader
from os import walk
from settings import TILESIZE
import pygame

def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter=',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map


def import_folder(path):
    surface_list = []
    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

        return surface_list


def import_cut_graphic(path):
    surface = pygame.image.load(path).convert_alpha()
    tile_num_x = surface.get_size()[0] // TILESIZE
    tile_num_y = surface.get_size()[1] // TILESIZE
    cut_tiles = []
    for row in range(tile_num_y):
        for column in range(tile_num_x):
            x = column * TILESIZE
            y = row * TILESIZE
            new_surface = pygame.Surface((int(TILESIZE), int(TILESIZE)))
            new_surface.blit(surface, (0, 0), pygame.Rect(x, y, TILESIZE, TILESIZE))
            cut_tiles.append(new_surface.convert_alpha())

    return cut_tiles
