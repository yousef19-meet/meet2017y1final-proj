import turtle
import random
import time
def maze_maker():
    #TOP
    for i in range(7):
        turtle.stamp()
        turtle.forward(20)
        x_pos=turtle.pos()[0]
        y_pos=turtle.pos()[1]
        
        my_pos=(round(x_pos),round(y_pos))

        pos_List_L.append(my_pos)
        new_stamp=turtle.stamp()
        stamp_list.append(new_stamp)
        
    turtle.forward(60)

    for i in range(20):
        
        turtle.forward(20)
        x_pos=turtle.pos()[0]
        y_pos=turtle.pos()[1]
        
        my_pos=(round(x_pos),round(y_pos))

        pos_List_L.append(my_pos)
        new_stamp=turtle.stamp()
        stamp_list.append(new_stamp)
        
        #Right
    stamp_list_R=[]
    new_stamp_R=[]
    pos_List_R=[]
    turtle.right(90)
    ############
    for i in range(23):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        
        my_pos_R=(round(x_pos_L),round(y_pos_L))

        pos_List_L.append(my_pos_R)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_R)
    ############
    turtle.forward(60)
    for i in range(5):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        
        my_pos_R=(round(x_pos_L),round(y_pos_L))

        pos_List_L.append(my_pos_R)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_R)
    #Down
    stamp_list_D=[]
    new_stamp_D=[]
    pos_List_D=[]
    turtle.right(90)
    for i in range(30):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        
        my_pos_D=(round(x_pos_L),round(y_pos_L))

        pos_List_L.append(my_pos_D)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_D)

        #Left
    #stamp_list_L=[]
    new_stamp_L=[]
    #pos_List_L=[]
    turtle.right(90)

    for i in range(30):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        
        my_pos_L=(round(x_pos_L),round(y_pos_L))

        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
    turtle.goto(-80,300)
    turtle.right(180)
    #####################################
    for i in range(3):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
        
    turtle.right(90)
    for i in range(8):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
        
    turtle.goto(-300,180)
    turtle.right(180)
    for i in range(17):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
        
    turtle.right(90)
    for i in range(3):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
        
    turtle.left(90)
    for i in range(3):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
        
    turtle.left(90)
    for i in range(6):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
        
    turtle.left(90)
    for i in range(5):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
        
    turtle.right(180)
    for i in range(5):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
        
    turtle.right(90)
    for i in range(6):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
        
    turtle.left(90)
    for i in range(4):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
        
    turtle.left(90)
    for i in range(5):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
        
    turtle.right(90)
    for i in range(2):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
        
    turtle.right(180)
    for i in range(2):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
    turtle.left(90)
    for i in range(6):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
        
    turtle.left(90)
    for i in range(3):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
        
    turtle.left(90)
    for i in range(3):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)

        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
        
    turtle.goto(145,300)
    turtle.right(180)
    for i in range(1):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
        
    turtle.goto(300,180)
    turtle.right(90)
    for i in range(1):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
        
    turtle.goto(300,-160)
    for i in range(3):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
        
    turtle.right(90)
    for i in range(7):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
        
    turtle.left(90)
    for i in range(6):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
        
    turtle.right(90)
    for i in range(4):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
        
    turtle.right(180)
    for i in range(4):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
        
    turtle.left(90)
    for i in range(3):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
        
    turtle.right(90)
    for i in range(9):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
        
    turtle.right(180)
    for i in range(9):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
        
    turtle.left(90)
    for i in range(11):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
        
    turtle.right(90)
    for i in range(3):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
    turtle.right(90)
    for i in range(3):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
        
    turtle.right(180)
    for i in range(3):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
        
    turtle.right(90)
    for i in range(3):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
        
    turtle.left(90)
    for i in range(6):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
        
    turtle.goto(-300,40)
    turtle.right(180)
    for i in range(7):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
        
    turtle.goto(300,-220)
    turtle.right(180)
    for i in range(3):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
    turtle.left(90)
    for i in range(2):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
    turtle.right(90)
    for i in range(7):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
    turtle.right(90)
    for i in range(8):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
    turtle.left(90)
    for i in range(8):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
    turtle.left(90)
    for i in range(6):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
    turtle.goto(-40,-20)
    turtle.right(90)
    for i in range(5):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
    turtle.goto(-300,-80)
    turtle.right(180)
    for i in range(6):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)
    turtle.goto(-120,-20)
    turtle.right(90)


    for i in range(8):
        turtle.stamp()
        turtle.forward(20)
        x_pos_L=turtle.pos()[0]
        y_pos_L=turtle.pos()[1]
        my_pos_L=(round(x_pos_L),round(y_pos_L))
        pos_List_L.append(my_pos_L)
        new_stamp_L=turtle.stamp()
        stamp_list_L.append(new_stamp_L)

def make_food():
    min_x=-int(SIZE_X/3/SQUARE_SIZE)+1
    max_x=int(SIZE_X/3/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/3/SQUARE_SIZE)-1
    max_y=int(SIZE_Y/3/SQUARE_SIZE)+1
    
    food_x=random.randint(min_x,max_x)*SQUARE_SIZE
    food_y=random.randint(min_y,max_y)*SQUARE_SIZE
    while (food_x, food_y) in pos_List_L:
        food_x=random.randint(min_x,max_x)*SQUARE_SIZE
        food_y=random.randint(min_y,max_y)*SQUARE_SIZE
    food.goto(food_x,food_y)
    food_pos.append((food_x, food_y))
    foodID=food.stamp()
    food_stamps.append(foodID)

def eat_food():
    global score1
    if trump.pos() in food_pos:
        print(food_stamps)
        food_ind=food_pos.index(trump.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print('you have eaten the food!')
        score1=score1+1
        score.clear()
        score.write(score1)
        
        #write(score1) 

now = time.time()
def move_trump():
    global direction ,timer
    my_pos=trump.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]
    
    if direction==RIGHT:
        maybe_pos = (x_pos+SQUARE_SIZE,y_pos)
        if not maybe_pos in pos_List_L:            
            trump.goto(x_pos+SQUARE_SIZE,y_pos)
        print('you moved right!')
    elif direction==LEFT:
        maybe_pos=(x_pos-SQUARE_SIZE,y_pos)
        if not maybe_pos in pos_List_L:
            trump.goto(x_pos-SQUARE_SIZE,y_pos)
        print('you moved left!')
    elif direction==UP:
        maybe_pos=(x_pos,y_pos+SQUARE_SIZE)
        if not maybe_pos in pos_List_L:
            trump.goto(x_pos,y_pos+SQUARE_SIZE)
        print('you moved up!')
    elif direction==DOWN:
        maybe_pos=(x_pos,y_pos-SQUARE_SIZE)
        if not maybe_pos in pos_List_L:
            trump.goto(x_pos,y_pos-SQUARE_SIZE)
        print('you moved down!')

    
    
    turtle_timer.clear()
    time_left = time_limit-(int(time.time() - now))
    turtle_timer.write(str(time_left)+" secondes left")
    if time_left<=0:
        quit()
##    while time_left > 0:        
##        turtle_timer.clear()
##        timer = timer-int(time.time())
##        turtle_timer.write(str(timer)+" secondes left")
        
    if trump.pos()==(300,-180) or trump.pos()==(300,-200):
        you_won.stamp()
        move_trump.end()
    turtle.ontimer(move_trump,100)

    eat_food()


######################################################

turtle.tracer(1,0) 
SIZE_X=900
SIZE_Y=900
turtle.setup(SIZE_X, SIZE_Y)
turtle.shape("square")
turtle.penup()
turtle.goto(-300,300)
pos_List_L=[]
stamp_list_L=[]
stamp_list=[]
#<<<<<<< HEAD
turtle.speed(1)
=======
#turtle.speed(1)

#>>>>>>> 5923b4331c1fe9f0db5f2721a012c52c79533412
turtle.register_shape('trump_head.gif')

turtle.resizemode("user")
turtle.penup()
SQUARE_SIZE=20
START_LENGTH=1
trump=turtle.clone()
trump.shape('trump_head.gif')
trump.shapesize(0.05,0.05,0)

turtle.ht()
start_position= (-120,300)
trump.goto(start_position)
pos_list=[]
score1 = 0
time_limit=45

food_stamps=[]

turtle.penup()
food_pos=[]
food_list=[]
turtle.register_shape('hamburger.gif')
food=turtle.clone()
food.shape('hamburger.gif')
food.goto(-100,100)
turtle_timer=turtle.clone()
turtle_timer.ht()
#turtle_timer.penup()
turtle_timer.goto(320,320)

############################
score=turtle.clone()
score.penup()
score.ht()
score.goto(-300,320)
############################
turtle.register_shape('homless.gif')
homless=turtle.clone()
homless.shape('homless.gif')
homless.penup()

homless.goto(300,-185)
homless.stamp()
############################
you_won=turtle.clone()
turtle.register_shape("you_won.gif")
you_won.shape("you_won.gif")
you_won.penup()
you_won.goto(0,0)
############################
   
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

direction=DOWN
UP_EDGE=SIZE_Y/2
DOWN_EDGE=SIZE_Y/-2
RIGHT_EDGE=SIZE_X/2
LEFT_EDGE=SIZE_X/-2

def up():
    global direction
    x_pos=trump.pos()[0]
    y_pos=trump.pos()[1]
    new_pos=(x_pos,y_pos+SQUARE_SIZE)
    if not new_pos in pos_List_L:
        direction=UP
        print('you pressed the up key!')

def left():
    global direction
    x_pos=trump.pos()[0]
    y_pos=trump.pos()[1]
    new_pos=(x_pos-SQUARE_SIZE,y_pos)
    if not new_pos in pos_List_L:
        direction=LEFT
        print('you pressed the left key!')
 

def down():
    global direction
    x_pos=trump.pos()[0]
    y_pos=trump.pos()[1]
    new_pos=(x_pos,y_pos-SQUARE_SIZE)
    if not new_pos in pos_List_L:
        direction=DOWN
        print('you pressed the down key!')

def right():
    global direction
    x_pos=trump.pos()[0]
    y_pos=trump.pos()[1]
    new_pos=(x_pos+SQUARE_SIZE,y_pos)
    if not new_pos in pos_List_L:
        direction=RIGHT
        print('you pressed the right key!')
      

turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.listen()

maze_maker()

for i in range (10):
    make_food()   
     
move_trump()
homless.stamp()       
