import Reader
import Writer
from PIL import Image


def main():
    print("RED file format\n")
    print("1) Convert image")
    print("2) Read image")
    print("3) Convert and Read")
    choice = input(">>> ")

    if choice == "1":
        image_path = input("Image name: ")
        image_output_name = input("Output name: ")
        Writer.copy_image(image_path, image_output_name)
    elif choice == "2":
        image_path = input("Image to read: ")
        Reader.read(image_path)
    else:
        image_path = input("Image: ")
        Writer.copy_image(image_path, "output.red")
        Reader.read("output.red")
        Image.open("output.red.png").show()


main()
