import time
import turtle
secondes=60
turtle.right(90)
turtle.ontimer(
while secondes >0:
    turtle.forward(20)
    time.sleep(1)
    
    turtle.write(str(secondes)+"secondes left")
    secondes -=1
    
