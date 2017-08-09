import turtle
import random

turtle.register_shape("clinton2.gif")

turtle.shape("clinton2.gif")
turtle.resizemode("user")
turtle.turtlesize(0.5, 0.5, 0.5)




turtle.tracer(1,0) 
SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) 


turtle.penup()
SQUARE_SIZE = 20
START_LENGTH =1
clinton=turtle.clone()
turtle.hideturtle()

pos_list=[]



for i in range(START_LENGTH):
    x_pos=clinton.pos()[0]
    y_pos=clinton.pos()[1]
    x_pos+=SQUARE_SIZE
    my_pos=(x_pos,y_pos)
    clinton.goto(x_pos,y_pos)
    pos_list.append(my_pos)
    
    
W_KEY='w'
A_KEY='a'
S_KEY='s'
D_KEY='d'
TIME_STEP=100
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
    if direction !=DOWN:
        global direction
        direction=UP
        print('you pressed the up key!')

def left():
    if direction !=RIGHT:
        global direction
        direction=LEFT
        print('you pressed the left key!')

def down():
    if direction !=UP:
        global direction
        direction=DOWN
        print('you pressed the down key!')

def right():
    if direction !=LEFT:
        global direction
        direction=RIGHT
        print('you pressed the right key!')
    

turtle.onkeypress(up,W_KEY)
turtle.onkeypress(left,A_KEY)
turtle.onkeypress(down,S_KEY)
turtle.onkeypress(right,D_KEY)
turtle.listen()





def move_clinton():
    global direction 
    my_pos=clinton.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]
    
    if direction==RIGHT:
        clinton.goto(x_pos+SQUARE_SIZE,y_pos)
        print('you moved right!')
    elif direction==LEFT:
        clinton.goto(x_pos-SQUARE_SIZE,y_pos)
        print('you moved left!')
    elif direction==UP:
        clinton.goto(x_pos,y_pos+SQUARE_SIZE)
        print('you moved up!')
    elif direction==DOWN:
        clinton.goto(x_pos,y_pos-SQUARE_SIZE)
        print('you moved down!')
    turtle.ontimer(move_clinton,100)

    
move_clinton()

food_pos=[(100,100)]


turtle.penup()
stamp_list=[]
food_pos=[]
food_list=[]
turtle.setup(SIZE_X,SIZE_Y)
x_pos=snake.pos()[0] #Get x-position with snake.pos()[0]
y_pos=snake.pos()[1]
pos_list = []
if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos())
        food.clear_stamp(food_stamps[food_ind])
min_x=-int(SIZE_X/3/SQUARE_SIZE)+1
max_x=int(SIZE_X/3/SQUARE_SIZE)-1
min_y=-int(SIZE_Y/3/SQUARE_SIZE)-1
max_y=int(SIZE_Y/3/SQUARE_SIZE)+1

def make_food():
    turtle.register_shape('hamburger.gif')
    food=turtle.clone()
    food.shape('hamburger.gif')
    food.goto(-100,100)
   
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
make_food()   
turtle.mainloop()




    
    


    
    






    




