import json
from PIL import Image
import RGBConversions
import pickle


def read(image_path):
    with open(image_path, "rb") as f:
        load = pickle.load(f)
        load = json.loads(load)
        f.close()
    img = Image.new('RGB', (load[0][0], load[0][1]))
    x = 0
    y = 0
    for i in range(len(load[1])):
        if len(load[1][i]) == 1:
            load[1][i] = load[1][i] + load[1][i] + load[1][i] + load[1][i] + load[1][i] + load[1][i]
        try:
            img.putpixel((x, y), RGBConversions.hex_to_rgb(load[1][i]))
        except IndexError:
            print("something went wrong IndexError")
            exit(-1)
        if x == load[0][0] - 1:
            x = 0
            y += 1
        else:
            x += 1
    img.save("{0}.png".format(image_path))
