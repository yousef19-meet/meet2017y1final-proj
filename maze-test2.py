import turtle
turtle.tracer(1,0)
loading_screen=turtle.clone()

##turtle.register_shape("giphy2.gif")
##
##loading_screen.goto(0,0)
##loading_screen.shape("giphy2.gif")
##loading_screen.stamp()

turtle.shape("square")
turtle.penup()
turtle.setup(900,900)
turtle.goto(-300,300)
pos_List=[]
stamp_list=[]
turtle.speed(1)


#TOP
for i in range(7):
    turtle.stamp()
    turtle.forward(20)
    x_pos=turtle.pos()[0]
    y_pos=turtle.pos()[1]
    
    my_pos=(x_pos,y_pos)

    pos_List.append(my_pos)
    new_stamp=turtle.stamp()
    stamp_list.append(new_stamp)
    
turtle.forward(60)

for i in range(20):
    
    turtle.forward(20)
    x_pos=turtle.pos()[0]
    y_pos=turtle.pos()[1]
    
    my_pos=(x_pos,y_pos)

    pos_List.append(my_pos)
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
    x_pos_R=turtle.pos()[0]
    y_pos_R=turtle.pos()[1]
    
    my_pos_R=(x_pos,y_pos)

    pos_List_R.append(my_pos_R)
    new_stamp_R=turtle.stamp()
    stamp_list_R.append(new_stamp_R)
############
turtle.forward(60)
for i in range(5):
    turtle.stamp()
    turtle.forward(20)
    x_pos_R=turtle.pos()[0]
    y_pos_R=turtle.pos()[1]
    
    my_pos_R=(x_pos,y_pos)

    pos_List_R.append(my_pos_R)
    new_stamp_R=turtle.stamp()
    stamp_list_R.append(new_stamp_R)
#Down
stamp_list_D=[]
new_stamp_D=[]
pos_List_D=[]
turtle.right(90)
for i in range(30):
    turtle.stamp()
    turtle.forward(20)
    x_pos_D=turtle.pos()[0]
    y_pos_D=turtle.pos()[1]
    
    my_pos_D=(x_pos,y_pos)

    pos_List_D.append(my_pos_D)
    new_stamp_D=turtle.stamp()
    stamp_list_D.append(new_stamp_D)

    #Left
stamp_list_L=[]
new_stamp_L=[]
pos_List_L=[]
turtle.right(90)

for i in range(30):
    turtle.stamp()
    turtle.forward(20)
    x_pos_L=turtle.pos()[0]
    y_pos_L=turtle.pos()[1]
    
    my_pos_L=(x_pos,y_pos)

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
turtle.right(90)
for i in range(8):
    turtle.stamp()
    turtle.forward(20)
    x_pos_L=turtle.pos()[0]
    y_pos_L=turtle.pos()[1]
turtle.goto(-300,180)
turtle.right(180)
for i in range(17):
    turtle.stamp()
    turtle.forward(20)
    x_pos_L=turtle.pos()[0]
    y_pos_L=turtle.pos()[1]
turtle.right(90)
for i in range(3):
    turtle.stamp()
    turtle.forward(20)
    x_pos_L=turtle.pos()[0]
    y_pos_L=turtle.pos()[1]
turtle.left(90)
for i in range(3):
    turtle.stamp()
    turtle.forward(20)
    x_pos_L=turtle.pos()[0]
    y_pos_L=turtle.pos()[1]
turtle.left(90)
for i in range(6):
    turtle.stamp()
    turtle.forward(20)
    x_pos_L=turtle.pos()[0]
    y_pos_L=turtle.pos()[1]
turtle.left(90)
for i in range(5):
    turtle.stamp()
    turtle.forward(20)
    x_pos_L=turtle.pos()[0]
    y_pos_L=turtle.pos()[1]
turtle.right(180)
for i in range(5):
    turtle.stamp()
    turtle.forward(20)
    x_pos_L=turtle.pos()[0]
    y_pos_L=turtle.pos()[1]
turtle.right(90)
for i in range(6):
    turtle.stamp()
    turtle.forward(20)
    x_pos_L=turtle.pos()[0]
    y_pos_L=turtle.pos()[1]
turtle.left(90)
for i in range(4):
    turtle.stamp()
    turtle.forward(20)
    x_pos_L=turtle.pos()[0]
    y_pos_L=turtle.pos()[1]
turtle.left(90)
for i in range(5):
    turtle.stamp()
    turtle.forward(20)
    x_pos_L=turtle.pos()[0]
    y_pos_L=turtle.pos()[1]
turtle.right(90)
for i in range(2):
    turtle.stamp()
    turtle.forward(20)
    x_pos_L=turtle.pos()[0]
    y_pos_L=turtle.pos()[1]
turtle.right(180)
for i in range(2):
    turtle.stamp()
    turtle.forward(20)
    x_pos_L=turtle.pos()[0]
    y_pos_L=turtle.pos()[1]
turtle.left(90)
for i in range(6):
    turtle.stamp()
    turtle.forward(20)
    x_pos_L=turtle.pos()[0]

    y_pos_L=turtle.pos()[1]
turtle.left(90)
for i in range(3):
    turtle.stamp()
    turtle.forward(20)
    x_pos_L=turtle.pos()[0]
    y_pos_L=turtle.pos()[1]
turtle.left(90)
for i in range(3):
    turtle.stamp()
    turtle.forward(20)
    x_pos_L=turtle.pos()[0]
    y_pos_L=turtle.pos()[1]
turtle.goto(145,300)
turtle.right(180)
for i in range(2):
    turtle.stamp()
    turtle.forward(20)
    x_pos_L=turtle.pos()[0]
    y_pos_L=turtle.pos()[1]
turtle.goto(300,180)
turtle.right(90)
for i in range(2):
    turtle.stamp()
    turtle.forward(20)
    x_pos_L=turtle.pos()[0]
    y_pos_L=turtle.pos()[1]
turtle.goto(300,-160)
for i in range(3):
    turtle.stamp()
    turtle.forward(20)
    x_pos_L=turtle.pos()[0]
    y_pos_L=turtle.pos()[1]
turtle.right(90)
for i in range(7):
    turtle.stamp()
    turtle.forward(20)
    x_pos_L=turtle.pos()[0]
    y_pos_L=turtle.pos()[1]
turtle.left(90)
for i in range(6):
    turtle.stamp()
    turtle.forward(20)
    x_pos_L=turtle.pos()[0]
    y_pos_L=turtle.pos()[1]
turtle.right(90)
for i in range(4):
    turtle.stamp()
    turtle.forward(20)
    x_pos_L=turtle.pos()[0]
    y_pos_L=turtle.pos()[1]
turtle.right(180)
for i in range(4):
    turtle.stamp()
    turtle.forward(20)
    x_pos_L=turtle.pos()[0]
    y_pos_L=turtle.pos()[1]
turtle.left(90)
for i in range(3):
    turtle.stamp()
    turtle.forward(20)
    x_pos_L=turtle.pos()[0]
    y_pos_L=turtle.pos()[1]
turtle.right(90)
for i in range(7):
    turtle.stamp()
    turtle.forward(20)
    x_pos_L=turtle.pos()[0]
    y_pos_L=turtle.pos()[1]
turtle.right(180)
for i in range(7):
    turtle.stamp()
    turtle.forward(20)
    x_pos_L=turtle.pos()[0]
    y_pos_L=turtle.pos()[1]
turtle.left(90)
for i in range(11):
    turtle.stamp()
    turtle.forward(20)
    x_pos_L=turtle.pos()[0]
    y_pos_L=turtle.pos()[1]
turtle.right(90)
for i in range(3):
    turtle.stamp()
    turtle.forward(20)
    x_pos_L=turtle.pos()[0]
    y_pos_L=turtle.pos()[1]
turtle.right(90)
for i in range(3):
    turtle.stamp()
    turtle.forward(20)
    x_pos_L=turtle.pos()[0]
    y_pos_L=turtle.pos()[1]
turtle.right(180)
for i in range(3):
    turtle.stamp()
    turtle.forward(20)
    x_pos_L=turtle.pos()[0]
    y_pos_L=turtle.pos()[1]
turtle.right(90)
for i in range(3):
    turtle.stamp()
    turtle.forward(20)
    x_pos_L=turtle.pos()[0]
    y_pos_L=turtle.pos()[1]
turtle.left(90)
for i in range(6):
    turtle.stamp()
    turtle.forward(20)
    x_pos_L=turtle.pos()[0]
    y_pos_L=turtle.pos()[1]
turtle.goto(-300,40)
turtle.right(180)
for i in range(7):
    turtle.stamp()
    turtle.forward(20)
    x_pos_L=turtle.pos()[0]
    y_pos_L=turtle.pos()[1]
