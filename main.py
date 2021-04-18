import math
import pygame
screen_width = 300
screen_height = 300
tile_width = 150
screen_size = [screen_width, screen_height]
gameTitle = "ASMR Clicker"
white = [255, 255, 255]
pink = [255, 192, 203]
deeppink = [255, 20, 147]
screen = pygame.display.set_mode(screen_size)
tile = pygame.Rect(0, 0, tile_width, tile_width)
tile_array = []
tile_arraystate = []


def start_set_array():
    column_quantity = screen_width / tile_width
    row_quantity = screen_height / tile_width
    c_range = range(int(column_quantity))
    r_range = range(int(row_quantity))
    for c in c_range:
        for r in r_range:
            tile_array.append((c, r))
    print("tile_array:", tile_array)
    for a in tile_array:
        tile_arraystate.append(0)
    print("tile_arraystate:", tile_arraystate)


def click():
    mousePos = pygame.mouse.get_pos()
    tx = mousePos[0]
    ty = mousePos[1]
    ax = math.floor(tx/tile_width)
    ay = math.floor(ty/tile_width)
    print("mousePos", mousePos)
    print("ax, ay:", [ax, ay])
    return [ax, ay]


def tile_draw(i):
    if tile_arraystate[tile_array.index(i)] == 0:
        pygame.draw.rect(screen, deeppink, pygame.Rect(i[0]*tile_width, i[1]*tile_width, tile_width, tile_width))
        print("Drawing tile at", i[0]*tile_width, "&", i[1]*tile_width)
        tile_arraystate[tile_array.index(i)] = 1
        print("tile_arraystate after 58", tile_arraystate)
    else:
        pygame.draw.rect(screen, pink, pygame.Rect(i[0]*tile_width, i[1]*tile_width, tile_width, tile_width))
        print("Drawing tile at", i[0]*tile_width, "&", i[1]*tile_width)
        tile_arraystate[tile_array.index(i)] = 0
        print("tile_arraystate after 63", tile_arraystate)


def main():
    start_set_array()
    pygame.display.init()
    pygame.display.set_caption(gameTitle)
    screen.fill(pink)
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_array = click()
            for i in tile_array:
                if i[0] == click_array[0]:
                    if i[1] == click_array[1]:
                        tile_draw(i)
        pygame.display.flip()


main()
exit()