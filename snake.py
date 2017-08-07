import turtle
import random

turtle.tracer(1,0) #This helps the turtle move more smoothly
SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window
#size.
turtle.penup()
SQUARE_SIZE = 20
START_LENGTH = 1
#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []
#Set up positions (x,y) of boxes that make up the snake
turtle.register_shape("clinton.gif")
snake = turtle.clone()
snake.shape("clinton.gif")

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()




for i in range(START_LENGTH):
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]
    x_pos+=SQUARE_SIZE
    my_pos=(x_pos,y_pos)
    snake.goto(x_pos,y_pos)
    pos_list.append(my_pos)
    new_stamp=snake.stamp()
    stamp_list.append(new_stamp)
    

W_KEY='Up'
A_KEY='Left'
S_KEY='Down'
D_KEY='Right'
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
    

turtle.onkeypress(up,W_KEY)
turtle.onkeypress(left,A_KEY)
turtle.onkeypress(down,S_KEY)
turtle.onkeypress(right,D_KEY)
turtle.listen()

score=turtle.clone()
score.penup()
score.goto(300,250)
score1=0
def write (score1):
    score.clear()
    score.write(str(score1),font=("ARIAL",20,"normal"))



def make_food():
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)-1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)+1
    food_x=random.randint(min_x,max_x)*SQUARE_SIZE
    food_y=random.randint(min_y,max_y)*SQUARE_SIZE
    food.goto(food_x,food_y)
    new_food=(food_x,food_y)
    food_pos.append(new_food)
    new_stamp=food.stamp()
    food_stamps.append(new_stamp)


def move_snake():
    global direction , score1
    my_pos=snake.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]
    
    if direction==RIGHT:
        snake.goto(x_pos+SQUARE_SIZE,y_pos)
        print('you moved right!')
    elif direction==LEFT:
        snake.goto(x_pos-SQUARE_SIZE,y_pos)
        print('you moved left!')
    elif direction==UP:
        snake.goto(x_pos,y_pos+SQUARE_SIZE)
        print('you moved up!')
    elif direction==DOWN:
        snake.goto(x_pos,y_pos-SQUARE_SIZE)
        print('you moved down!')

    new_pos=snake.pos()
    new_x_pos=new_pos[0]
    new_y_pos=new_pos[1]
    pos_list.append(my_pos)
    new_stamp=snake.stamp()
    stamp_list.append(new_stamp)
    

    
    
    
    if new_x_pos>=RIGHT_EDGE:
        print('you hit the right edge!Game over!')
        quit()
    elif new_x_pos<=LEFT_EDGE:
        print('you hit the left edge!Game over!')
        quit()
    elif new_y_pos>=UP_EDGE:
        print('you hit the up edge!Game over!')
        quit()
    elif new_y_pos<=DOWN_EDGE:
        print('you hit the down edge!Game over!')
        quit()
    

   # my_pos=snake.pos()
    #new_stamp=snake.stamp()
    #stamp_list.append(new_stamp)
    global food_stamps, food_pos
    if snake.pos() in food_pos:
        print(food_stamps)
        food_ind=food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print('you have eaten the food!')
        score1=score1+1
        write(score1)
        make_food()
    
        

    if snake.pos() in pos_list[0:-1]:
        print('Game over!')
        quit()
        
    else:
        old_stamp=stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)
    turtle.ontimer(move_snake,TIME_STEP)

move_snake()

food_pos=[(100,100)]


for this_food_pos in food_pos:
    food.goto(this_food_pos)
    stamp_id=food.stamp()
    food_stamps.append(stamp_id)


    
    


    
    






    



