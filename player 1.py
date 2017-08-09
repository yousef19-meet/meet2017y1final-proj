import turtle
import random
turtle.register_shape('trump_small.gif')
turtle.shape('trump_small.gif')
turtle.resizemode("user")
turtle.shapesize(-5,-5,0)
turtle.tracer(1,0) 
SIZE_X=800
SIZE_Y=500

turtle.setup(SIZE_X, SIZE_Y)
turtle.penup()
SQUARE_SIZE=20
START_LENGTH=1
trump=turtle.clone()
turtle.ht()

pos_list=[]

for i in range(START_LENGTH):
    x_pos=trump.pos()[0]
    y_pos=trump.pos()[1]
    x_pos+=SQUARE_SIZE
    my_pos=(x_pos,y_pos)
    trump.goto(x_pos,y_pos)
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
    if direction!=DOWN:
        global direction
        direction=UP
        print('you pressed the up key!')

def left():
    if direction!=RIGHT:
        global direction
        direction=LEFT
        print('you pressed the left key!')

def down():
    if direction!=UP:
        global direction
        direction=DOWN
        print('you pressed the down key!')

def right():
    if direction!=LEFT:
        global direction
        direction=RIGHT
        print('you pressed the right key!')
    

turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.listen()

def move_trump():
    global direction 
    my_pos=trump.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]
    
    if direction==RIGHT:
        trump.goto(x_pos+SQUARE_SIZE,y_pos)
        print('you moved right!')
    elif direction==LEFT:
        trump.goto(x_pos-SQUARE_SIZE,y_pos)
        print('you moved left!')
    elif direction==UP:
        trump.goto(x_pos,y_pos+SQUARE_SIZE)
        print('you moved up!')
    elif direction==DOWN:
       trump.goto(x_pos,y_pos-SQUARE_SIZE)
       print('you moved down!')
<<<<<<< HEAD
    turtle.ontimer(move_trump,100)
    
     
move_trump()
       
=======
    turtle.ontimer(move_turtle,100)

move_turtle()

stamp_list=[]
food_pos=[]
food_list=[]
turtle.setup(SIZE_X,SIZE_Y)
x_pos=player1.pos()[0] #Get x-position with snake.pos()[0]
y_pos=player1.pos()[1]
pos_list = []
if player1.pos() in food_pos:
        food_ind=food_pos.index(player1.pos())
        food.clear_stamp(food_stamps[food_ind])
min_x=-int(SIZE_X/3/SQUARE_SIZE)+1
max_x=int(SIZE_X/3/SQUARE_SIZE)-1
min_y=-int(SIZE_Y/3/SQUARE_SIZE)-1
max_y=int(SIZE_Y/3/SQUARE_SIZE)+1

def make_food():
    turtle.register_shape('hamburger.gif')
    food=turtle.clone()
    food.shape('hamburger.gif')
   
    min_x=-int(SIZE_X/3/SQUARE_SIZE)+1
    max_x=int(SIZE_X/3/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/3/SQUARE_SIZE)-1
    max_y=int(SIZE_Y/3/SQUARE_SIZE)+1
    
    food_x=random.randint(min_x,max_x)*SQUARE_SIZE
    food_y=random.randint(min_y,max_y)*SQUARE_SIZE
    while food_pos in pos_list:
        food_x=random.randint(min_x,max_x)*SQUARE_SIZE
        food_y=random.randint(min_y,max_y)*SQUARE_SIZE
    food.goto(food_x,food_y)
    food_pos.append((food_x, food_y))
    foodID=food.stamp()
    food_stamps.append(foodID)   
>>>>>>> d46845059ca3cb85738f021415ce9275a32b8627

	


