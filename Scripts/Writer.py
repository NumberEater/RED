from PIL import Image
import json
from Scripts import RGBConversions, Logging
import pickle


def copy_image(image_path):
    image = Image.open(image_path, "r")
    values1 = list(image.getdata())

    values1 = [image.size, values1]

    for i in range(len(values1[1])):
        hex_value = RGBConversions.rgb_to_hex(values1[1][i])
        values1[1][i] = hex_value

    with open("output.red", "wb") as f:
        json_string = json.dumps(values1)
        pickle.dump(json_string, f)
        f.close()
