import turtle
display = turtle.Screen()
display.screensize(1920, 1080)
def UI_underline(length):
    print('Length =', length)
    t = turtle.Pen()
    t.pensize(2)
    t.speed(1)
    for line in range(length):
        t.forward(100)
        t.penup()
        t.forward(20)
        t.pendown()

def UI_hanged_man(chances_left):
    print('chance(s) left:', chances_left)

def UI_exit_button(end):
    if end is True:
        print("Are you sure to leave the game?")
        print('The button is flashing.')
        print('Ending in a second.')

def UI_menu_table():
    print('\t  <------>\n \t\tMENU\n To "Play" type p.\n To "Configure" '
          'type c.\t\n For "Admin" type a.\n'
          ' To "Exit" type e.\n\t  <------>')  # Introduction menu