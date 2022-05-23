from PIL import Image
import json
import RGBConversions
import pickle

# If you want to questionably round the image, set this to True
ROUND_VALUES = False
# If you want to questionably compress the image, set this to True
COMPRESS_VALUES = False


def RGBRound(x, base=40):
    return base * round(x / base)


def copy_image(image_path, name):
    image = Image.open(image_path, "r")
    values = list(image.getdata())

    values = [image.size, values]

    # Convert RGB to hex
    for i in range(len(values[1])):
        if ROUND_VALUES:
            if values[1][i][0] > 200:
                if values[1][i][1] > 200:
                    if values[1][i][2] > 200:
                        values[1][i] = (255, 255, 255)
            elif values[1][i][0] < 55:
                if values[1][i][1] < 55:
                    if values[1][i][2] < 55:
                        values[1][i] = (0, 0, 0)
        elif COMPRESS_VALUES:
            values[1][i] = (RGBRound(values[1][i][0]), RGBRound(values[1][i][1]), RGBRound(values[1][i][2]))
        hex_value = RGBConversions.rgb_to_hex(values[1][i])
        split_hex_value = hex_value[0].split()

        values[1][i] = hex_value

    with open(name, "wb") as f:
        json_string = json.dumps(values)
        pickle.dump(json_string, f)
        f.close()
