from Scripts import RGBConversions


def calculate_index(x, y, width):
    output = y * width
    output += x
    return output


def show_top_left(load, screen):
    x = 0
    y = 0
    index = calculate_index(x, y, load[0][0])
    for i in range(len(load[1])):
        if index != len(load[1]) - 1:
            index += 1
        if len(load[1][index]) == 1:
            load[1][index] = load[1][index] + load[1][index] + load[1][index] + load[1][index] + load[1][index] + \
                             load[1][index]
        try:
            screen.set_at((x, y), RGBConversions.hex_to_rgb(load[1][index]))
        except IndexError:
            print("something went wrong: IndexError")
            exit(-1)
        if x == round(load[0][0] / 2) - 1:
            x = 0
            if y == int((load[0][1] - 1) / 2):
                break
            else:
                y += 1
            index = calculate_index(x, y, load[0][0])
        else:
            x += 1


def show_top_right(load, screen):
    x = round(load[0][0] / 2)
    y = 0
    index = calculate_index(x, y, load[0][0])
    for i in range(len(load[1])):
        if index != len(load[1]):
            index += 1
        if len(load[1][index]) == 1:
            load[1][index] = load[1][index] + load[1][index] + load[1][index] + load[1][index] + load[1][index] + \
                             load[1][index]
        try:
            screen.set_at((x, y), RGBConversions.hex_to_rgb(load[1][index]))
        except IndexError:
            print("something went wrong: IndexError")
            exit(-1)
        if x == load[0][0] - 1:
            x = round(load[0][0] / 2)
            if y == int((load[0][1] - 1) / 2):
                break
            else:
                y += 1
            index = calculate_index(x, y, load[0][0])
        else:
            x += 1


def show_bottom_left(load, screen):
    x = 0
    y = round(load[0][1] / 2)
    index = load[0][0] * round(load[0][1] / 2)
    for i in range(round(len(load[1]) / 2)):
        if index < len(load[1]) - 1:
            index += 1
        else:
            break
        try:
            if len(load[1][index]) == 1:
                load[1][index] = load[1][index] + load[1][index] + load[1][index] + load[1][index] + load[1][
                    index] + \
                                 load[1][index]
        except IndexError:
            print("Index: ")
            print(index)
            print("Length: ")
            print(len(load[1]))

        screen.set_at((x, y), RGBConversions.hex_to_rgb(load[1][index]))
        if x == round(load[0][0] / 2) - 1:
            x = 0
            y += 1
            index = calculate_index(x, y, load[0][0])
        else:
            x += 1


def show_bottom_right(load, screen):
    x = round(load[0][0] / 2)
    y = round(load[0][1] / 2) - 1
    index = load[0][0] * round(load[0][1] / 2)
    for i in range(round(len(load[1]) / 2)):
        if index < len(load[1]) - 1:
            index += 1
        else:
            break
        try:
            if len(load[1][index]) == 1:
                load[1][index] = load[1][index] + load[1][index] + load[1][index] + load[1][index] + load[1][
                    index] + \
                                 load[1][index]
        except IndexError:
            print("Index: ")
            print(index)
            print("Length: ")
            print(len(load[1]))

        screen.set_at((x, y), RGBConversions.hex_to_rgb(load[1][index]))
        if x == load[0][0] - 1:
            x = round(load[0][0] / 2) - 1
            y += 1
            index = calculate_index(x, y, load[0][0])
        else:
            x += 1
