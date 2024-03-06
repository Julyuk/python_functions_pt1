import math

def __rectangle_area(width, height):
    return round(width * height, 2)

def __circle_area(radius):
    return round(math.pi * radius**2, 2)

def __triangle_area(side, height):
    return round(side * height / 2, 2)

def __init_menu():
    menu = ("Enter 1 if you want to calculate the area of a rectangle\n" +
            "Enter 2 if you want to calculate the area of a circle\n" +
            "Enter 3 if you want to calculate the area of a triangle\n" +
            "Enter 0 if you want to quit")
    print(menu)
    return int(input("Enter a number: "))

def check_number_is_positive(num):
    return (type(num) == int or type(num) == float) and num > 0

def __get_console_input(name):
    num = float(input(f"Enter a {name}: "))
    if check_number_is_positive(num):
        return num
    return __get_console_input(name)

def area_calculator():
    input_number = __init_menu()
    while input_number != 0:
        if input_number == 1:
            width = __get_console_input("width of a rectangle")
            height = __get_console_input("height of a rectangle")
            print("The area of a rectangle is "+str(__rectangle_area(width, height)))

        elif input_number == 2:
            radius = __get_console_input("radius of a circle")
            print("The area of a circle is "+str(__circle_area(radius)))

        elif input_number == 3:
            side = __get_console_input("side of a triangle")
            height = __get_console_input("height of a triangle, falling to the side you have just entered")
            print("The area of a triangle is "+str(__triangle_area(side, height)))

        else:
            print("Invalid input")

        input_number = __init_menu()

area_calculator()
