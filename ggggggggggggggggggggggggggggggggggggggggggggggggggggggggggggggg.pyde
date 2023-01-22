angle = 0
def setup():
    size(600,600)
    
def draw():
    background(100)
    global angle
    translate(300,300)
    rotate(radians(angle))
    
    fill(255)
    rect(0,0,70,30)
    rect(0,0,70,10)
    angle += 100
   
    
    rect(300,300,30,50)
