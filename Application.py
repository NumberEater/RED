import Reader
import Writer
import REDReader


def main():
    print("RED file format\n")
    print("1) Convert to RED")
    print("2) Convert to PNG")
    print("3) Convert and Show")
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
        REDReader.show_image("output.red")


main()
