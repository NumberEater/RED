import pygame
import json
import pickle
from Scripts import RGBConversions
from threading import Thread

def calculate_index(x, y, width):
    output = y * width
    output += x
    return output

def lower_resolution(load, factor):
    x = 0
    y = 0
    revised_load = [[round(load[0][0] / factor), round(load[0][1] / factor)], []]
    for i in range(len(load[1])):
        try:
            revised_load[1].append(load[1][calculate_index(x, y, load[0][0])])
            if x < load[0][0] - factor:
                x += factor
            else:
                x = 0
                y += factor
        except:
            break
    return revised_load


def show_half_1(load, screen):
    x = 0
    y = 0
    index = 0
    for i in range(len(load[1])):
        if index != len(load[1]) - 1:
            index += 1
        if len(load[1][index]) == 1:
            load[1][index] = load[1][index] + load[1][index] + load[1][index] + load[1][index] + load[1][index] + \
            load[1][index]
        try:
            screen.set_at((x, y), RGBConversions.hex_to_rgb(load[1][index]))
        except IndexError:
            print("something went wrong: IndexError")
            exit(-1)
        if x == load[0][0] - 1:
            x = 0
            if y == int((load[0][1] - 1) / 2):
                break
            else:
                y += 1
        else:
            x += 1


def show_half_2(load, screen):
    x = 0
    y = round(load[0][1] / 2)
    index = load[0][0] * round(load[0][1] / 2)
    for i in range(round(len(load[1]) / 2)):
        if index < len(load[1]) - 2:
            index += 1
        else:
            break
        try:
            if len(load[1][index]) == 1:
                load[1][index] = load[1][index] + load[1][index] + load[1][index] + load[1][index] + load[1][index] + \
                                 load[1][index]
        except IndexError:
            print("Index: ")
            print(index)
            print("Length: ")
            print(len(load[1]))

        screen.set_at((x, y), RGBConversions.hex_to_rgb(load[1][index]))
        if x == load[0][0] - 1:
            x = 0
            y += 1
        else:
            x += 1


def show_image(image_path):

    image_showing = False
    with open(image_path, "rb") as f:
        load = pickle.load(f)
        load = json.loads(load)
        f.close()


    if load[0][0] > 1920 or load[0][1] > 1080:
        load = lower_resolution(load, 4)
        print("Image too big, lowering resolution by a factor of 4")
    elif load[0][0] > 1200 or load[0][1] > 900:
        load = lower_resolution(load, 2)
        print("Image too big, lowering resolution by a factor of 2")

    SCREEN_SIZE = WIDTH, HEIGHT = (load[0][0], load[0][1])

    # Pygame stuff
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('RED Reader')
    fps = pygame.time.Clock()
    paused = False

    t1 = Thread(target=show_half_1, args=(load, screen))
    t2 = Thread(target=show_half_2, args=(load, screen))
    t1.start()
    t2.start()

    while True:
        if image_showing is False and t1.is_alive() is False and t2.is_alive() is False:
            pygame.display.update()
            image_showing = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
