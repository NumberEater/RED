from PIL import Image
import json
from Scripts import RGBConversions, Logging
import pickle


def copy_image(image_path):
    writer_logger = Logging.Logger(Logging.Mode.MODE_ERROR)
    image = Image.open(image_path, "r")
    values = list(image.getdata())

    values = [image.size, values]

    for i in range(len(values[1])):
        hex_value = RGBConversions.rgb_to_hex(values[1][i])
        values[1][i] = hex_value

    with open("output.red", "wb") as f:
        json_string = json.dumps(values)
        pickle.dump(json_string, f)
        writer_logger.Info("Saved as output.red")
        f.close()
