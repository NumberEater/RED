from PIL import Image
import json
import RGBConversions
import pickle


def copy_image(image_path, name):
    image = Image.open(image_path, "r")
    values = list(image.getdata())

    values = [image.size, values]

    # Convert RGB to hex
    for i in range(len(values[1])):
        if values[1][i][0] > 200:
            if values[1][i][1] > 200:
                if values [1][i][2] > 200:
                    values[1][i] = (255, 255, 255)
        elif values[1][i][0] < 55:
            if values[1][i][1] < 55:
                if values [1][i][2] < 55:
                    values[1][i] = (0, 0, 0)
        hex_value = RGBConversions.rgb_to_hex(values[1][i])
        split_hex_value = hex_value[0].split()
        if split_hex_value.count(split_hex_value[0]) == len(hex_value):
            print(split_hex_value)
            hex_value = split_hex_value[0]
        values[1][i] = hex_value

    with open(f"{name}.red", "wb") as f:
        json_string = json.dumps(values)
        pickle.dump(json_string, f)
        f.close()
