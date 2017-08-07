import turtle
turtle.register_shape("trash.gif")
turtle.clone()
turtle.shape("trash.gif")
SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X,SIZE_Y)
x_pos=snake.pos()[0] #Get x-position with snake.pos()[0]
y_pos=snake.pos()[1]
pos_list = []
my_pos=(x_pos,y_pos)
if player1.pos() in food_pos:
        food_ind=food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])
min_x=-int(SIZE_X/3/SQUARE_SIZE)+1
max_x=int(SIZE_X/3/SQUARE_SIZE)-1
min_y=-int(SIZE_Y/3/SQUARE_SIZE)-1
max_y=int(SIZE_Y/3/SQUARE_SIZE)+1
