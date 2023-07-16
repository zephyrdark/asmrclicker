# values to initialise the game
import math
import pygame
screen_width = 900
screen_height = 600
tile_width = 100
screen_size = [screen_width, screen_height]
gameTitle = "Lousy paint"
white = [255, 255, 255]
black = [0, 0, 0]
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 192, 203]
deeppink = [255, 20, 147]
yellow = [255, 255, 0]
cyan = [0, 255, 255]
purple = [255, 0, 255]
colours = [white, black, red, green, blue, pink, deeppink, yellow, cyan, purple]
screen = pygame.display.set_mode(screen_size)
tile = pygame.Rect(0, 0, tile_width, tile_width)
tile_array = []
tile_arraystate = []
tile_arraycolour = []
tile_array_index = []
palette_array = int(len(colours)) - int(len(colours))
palette_state = 0
mouse_move_pos = (0, 0)


# function that returns unused value for toggling palette - toggle feature not coded haha
def set_palette():
    global palette_state
    if palette_state == 0:
        for c in range(len(colours)):
            pygame.draw.rect(screen, black, pygame.Rect(0, (c*30), 32, 32))
            pygame.draw.rect(screen, colours[c], pygame.Rect(1, (c*30)+1, 30, 30))
        return 0


# function to setup array list & array-state list
def start_set_array():
    global tile_array_index
    column_quantity = screen_width / tile_width
    row_quantity = screen_height / tile_width
    c_range = range(int(column_quantity))
    r_range = range(int(row_quantity))
    for r in r_range:
        for c in c_range:
            tile_array.append((c, r))
    for a in tile_array:
        tile_arraystate.append(0)
        tile_arraycolour.append(0)
        tile_array_index = tile_array.index(a)


# function to determine which tile the mouse clicked
def click():
    mousePos = pygame.mouse.get_pos()
    tx = mousePos[0]
    ty = mousePos[1]
    ax = math.floor(tx/tile_width)
    ay = math.floor(ty/tile_width)
    return [ax, ay]


# function to draw tiles based on mouse position i
def tile_draw(i, c):
    pygame.draw.rect(screen, colours[c-1], pygame.Rect(i[0]*tile_width, i[1]*tile_width, tile_width, tile_width))
    return c


# main loop
def main():
    global palette_state
    global palette_array
    global tile_arraycolour
    global tile_array_index
    start_set_array()
    pygame.display.init()
    pygame.display.set_caption(gameTitle)
    screen.fill(white)
    palette_state = set_palette()
    while True:
        for tile_colour_index, tile_colour in enumerate(tile_arraycolour):
            tile_pos = tile_array[tile_colour_index]
            pygame.draw.rect(screen, colours[tile_colour],pygame.Rect(tile_pos[0] * tile_width, tile_pos[1] * tile_width, tile_width, tile_width))
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                break
            if event.key == pygame.K_SPACE:
                continue
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click_array = click()
                for i in tile_array:
                    if i[0] == click_array[0]:
                        if i[1] == click_array[1]:
                            tile_array_index = tile_array.index(i)
                            tile_arraycolour[tile_array_index] = tile_draw(i, palette_array)
            if event.button == 4:
                if palette_array == 0:
                    palette_array = int(len(colours))
                elif palette_array == int(len(colours)):
                    palette_array = 9
                else:
                    palette_array = palette_array - 1
            if event.button == 5:
                if palette_array == int(len(colours)):
                    palette_array = 0
                elif palette_array == int(len(colours))-1:
                    palette_array = 0
                else:
                    palette_array = palette_array + 1

        elif event.type == pygame.MOUSEMOTION:
            mouse_move_pos = list(pygame.mouse.get_pos())
            x = mouse_move_pos[0]
            y = mouse_move_pos[1]
            pygame.draw.rect(screen, colours[palette_array], pygame.Rect(x, y, 10, 10))
        palette_state = set_palette()
        pygame.display.flip()


main()
exit()
