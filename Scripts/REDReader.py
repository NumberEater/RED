import pygame
import json
import pickle
from Scripts import PlacementThreadFunctions, Logging
from threading import Thread


def lower_resolution(load, factor):
    x = 0
    y = 0
    revised_load = [[round(load[0][0] / factor), round(load[0][1] / factor)], []]
    for i in range(len(load[1])):
        try:
            revised_load[1].append(load[1][PlacementThreadFunctions.calculate_index(x, y, load[0][0])])
            if x < load[0][0] - factor:
                x += factor
            else:
                x = 0
                y += factor
        except IndexError:
            break
    return revised_load


def show_image(image_path):
    image_showing = False
    REDReader_logger = Logging.Logger(Logging.Mode.MODE_ERROR)
    with open(image_path, "rb") as f:
        load = pickle.load(f)
        load = json.loads(load)
        f.close()

    if load[0][0] > 1920 or load[0][1] > 1080:
        load = lower_resolution(load, 3)
        REDReader_logger.Info("Image is too big to display. Resolution is 1/3")
    elif load[0][0] > 1200 or load[0][1] > 900:
        load = lower_resolution(load, 2)
        REDReader_logger.Info("Image is too big to display. Resolution is 1/2")

    SCREEN_SIZE = (load[0][0], load[0][1])

    # Pygame stuff
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('RED Reader')

    # Start threads
    top_left = Thread(target=PlacementThreadFunctions.show_top_left, args=(load, screen))
    bottom_left = Thread(target=PlacementThreadFunctions.show_bottom_left, args=(load, screen))
    top_right = Thread(target=PlacementThreadFunctions.show_top_right, args=(load, screen))
    bottom_right = Thread(target=PlacementThreadFunctions.show_bottom_right, args=(load, screen))
    top_left.start()
    bottom_left.start()
    top_right.start()
    bottom_right.start()

    while True:
        if not image_showing:
            if not top_left.is_alive():
                if not bottom_left.is_alive():
                    if not top_right.is_alive():
                        if not bottom_right.is_alive():
                            pygame.display.update()
                            image_showing = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
