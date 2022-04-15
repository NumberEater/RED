import Reader
import Writer


def main():
    print("RED file format\n")
    print("1) Convert image")
    print("2) Read image")
    choice = input(">>> ")

    if choice == "1":
        image_path = input("Image name: ")
        image_output_name = input("Output name: ")
        Writer.copy_image(image_path, image_output_name)
    else:
        image_path = input("Image to read: ")
        Reader.read(image_path)


main()
