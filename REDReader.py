import pygame
import json
import pickle
import RGBConversions


def show_image(image_path):
    with open(image_path, "rb") as f:
        load = pickle.load(f)
        load = json.loads(load)
        f.close()

    SCREEN_SIZE = WIDTH, HEIGHT = (load[0][0], load[0][1])

    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('RED Reader')
    fps = pygame.time.Clock()
    paused = False

    x = 0
    y = 0

    screen.fill((175, 175, 175))

    for i in range(len(load[1])):
        if len(load[1][i]) == 1:
            load[1][i] = load[1][i] + load[1][i] + load[1][i] + load[1][i] + load[1][i] + load[1][i]
        try:
            screen.set_at((x, y), RGBConversions.hex_to_rgb(load[1][i]))
        except IndexError:
            print("something went wrong IndexError")
            exit(-1)
        if x == load[0][0] - 1:
            x = 0
            y += 1
        else:
            x += 1

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
