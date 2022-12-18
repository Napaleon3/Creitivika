x = 0
x1 = 0
x2 = 0
x3 = 0
x4 = 0
x5 = 0
def setup():
  size(600,600)
def draw(): 
  global x , x1 , x2, x3, x4 , x5
  background(100)
  #красный
  fill(x,0,0)
  ellipse(200,300,40,40)
  #синий
  fill(0,x1,0)
  ellipse(400,300,40,40)
  #зеленый
  fill(0,0,x2)
  ellipse(300,300,40,40)
  #желтый
  fill(x3,x3,0)
  ellipse(200,150,40,40)
  #голубой
  fill(0,x4,x4)
  ellipse(300,150,40,40)
  #феолтовый
  fill(x5,0,x5)
  ellipse(400,150,40,40)
  x = x + 1
  x1 = x1 + 3
  x2 = x2 + 2 
  x3 = x3 + 6
  x4 = x4 + 5
  x5 = x5 + 4
  if x > 255*60:
    noLoop()
colorMode
  
