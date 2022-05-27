from Scripts import Writer, Reader, REDReader
from tkinter import Tk
from tkinter.filedialog import askopenfilename  # Tkinter is used for the file dialogue


def main():
    print("\nRED Utilities\n")
    print("1) Convert to RED")
    print("2) Convert to PNG")
    print("3) Show in RED Reader")
    print("4) Convert and Show")
    choice = input(">>> ")
    Tk().withdraw()

    if choice == "1":
        image_path = askopenfilename()
        Writer.copy_image(image_path)
    elif choice == "2":
        image_path = askopenfilename()
        Reader.convert(image_path)
    elif choice == "3":
        image_path = askopenfilename()
        REDReader.show_image(image_path)
    else:
        image_path = input("Image: ")
        Writer.copy_image(image_path, "output.red")
        REDReader.show_image("output.red")


while True:
    main()
