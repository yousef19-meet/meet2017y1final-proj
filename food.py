import turtle
turtle.register_shape("trash.gif")
trash=turtle.clone()
trash.shape("trash.gif")
SIZE_X=800
SIZE_Y=500
turtle.penup()
SQUARE_SIZE = 20
stamp_list=[]
food_pos=[]
food_list=[]
turtle.setup(SIZE_X,SIZE_Y)
x_pos=player1.pos()[0] #Get x-position with snake.pos()[0]
y_pos=player1.pos()[1]
pos_list = []
my_pos=(x_pos,y_pos)
if player1.pos() in food_pos:
        food_ind=food_pos.index(snake.pos())
        food.clear stamp(food_stamps[food_ind])
min_x=-int(SIZE_X/3/SQUARE_SIZE)+1
max_x=int(SIZE_X/3/SQUARE_SIZE)-1
min_y=-int(SIZE_Y/3/SQUARE_SIZE)-1
max_y=int(SIZE_Y/3/SQUARE_SIZE)+1

def make_food():
    turtle.register_shape('food.gif')
    turtle.shape('food.gif')
   
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
    
