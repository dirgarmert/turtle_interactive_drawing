import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("Light Blue")
drawing_board.title("Drawing")

drawing_example = turtle.Turtle()
def turtle_forward():
    drawing_example.forward(100)
def rotate_angle_right():
    drawing_example.setheading(drawing_example.heading()+100)
def rotate_Angle_left():
    drawing_example.setheading(drawing_example.heading()-100)
def clear_screen():
    drawing_example.clear()
def turtle_homecoming():
    drawing_example.home()
def pen_up():
    drawing_example.penup()
def pen_down():
    drawing_example.pendown()

drawing_board.listen()
drawing_board.onkey(key="space",fun=turtle_forward)
drawing_board.onkey(key="Up",fun=rotate_Angle_left)
drawing_board.onkey(fun=rotate_angle_right,key="Down")
drawing_board.onkey(fun=clear_screen,key="c")
drawing_board.onkey(fun=turtle_homecoming,key="h")
drawing_board.onkey(fun=pen_up,key="w")
drawing_board.onkey(fun=pen_down,key="s")
turtle.mainloop()
