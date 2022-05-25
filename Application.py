from Scripts import Writer, Reader, REDReader


def main():
    print("RED Utilities\n")
    print("1) Convert to RED")
    print("2) Convert to PNG")
    print("3) Show in RED Reader")
    print("4) Convert and Show")
    choice = input(">>> ")

    if choice == "1":
        image_path = input("Image name: ")
        image_output_name = input("Output name: ")
        Writer.copy_image(image_path, image_output_name)
    elif choice == "2":
        image_path = input("Image to convert: ")
        Reader.convert(image_path)
    elif choice == "3":
        image_path = input("Image to show: ")

        REDReader.show_image(image_path)
    else:
        image_path = input("Image: ")
        Writer.copy_image(image_path, "output.red")
        REDReader.show_image("output.red")


main()
