import turtle
import random
turtle.register_shape('trump.gif')
turtle.shape('trump.gif')
turtle.resizemode("user")
turtle.shapesize(-5,-5,0)
turtle.tracer(1,0) 
SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y)
turtle.penup()
SQUARE_SIZE=20
START_LENGTH=1

pos_list=[]

for i in range(START_LENGTH):
    x_pos=turtle.pos()[0]
    y_pos=turtle.pos()[1]
    x_pos+=SQUARE_SIZE
    my_pos=(x_pos,y_pos)
    turtle.goto(x_pos,y_pos)
    pos_list.append(my_pos)
    


UP_ARROW='Up'
LEFT_ARROW='Left'
DOWN_ARROW='Down'
RIGHT_ARROW='Right'
TIME_STEP=100
SPACEBAR='space'
UP=0
LEFT=1
DOWN=2
RIGHT=3

direction=UP
UP_EDGE=SIZE_Y/2
DOWN_EDGE=SIZE_Y/-2
RIGHT_EDGE=SIZE_X/2
LEFT_EDGE=SIZE_X/-2

def up():
    global direction
    direction=UP
    print('you pressed the up key!')

def left():
    global direction
    direction=LEFT
    print('you pressed the left key!')

def down():
    global direction
    direction=DOWN
    print('you pressed the down key!')

def right():
    global direction
    direction=RIGHT
    print('you pressed the right key!')
    

turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.listen()

def move_turtle():
    global direction 
    my_pos=turtle.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]
    
    if direction==RIGHT:
        turtle.goto(x_pos+SQUARE_SIZE,y_pos)
        print('you moved right!')
    elif direction==LEFT:
        turtle.goto(x_pos-SQUARE_SIZE,y_pos)
        print('you moved left!')
    elif direction==UP:
        turtle.goto(x_pos,y_pos+SQUARE_SIZE)
        print('you moved up!')
    elif direction==DOWN:
       turtle.goto(x_pos,y_pos-SQUARE_SIZE)
       print('you moved down!')
    turtle.ontimer(move_turtle,100)

move_turtle()
       

	


