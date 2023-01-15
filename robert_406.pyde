size(600,600)

#поле
fill(100,200,50)
rect(0,300,600,500)
#дом
fill(150,100,0)
triangle(200,280,285,220,355,280)
fill(149)
rect(220,281,120,80)
#кирпичи
fill(100)
rect(240,340,12,6)
fill(138)
rect(270,300,12,6)
img = loadImage( "1.jpg" )
 #image (img, 0, 0)
image (img, 230, 290, width / 10, height / 10)



img2 = loadImage( "365.jpg" )
 #image (img2, 0, 0)
image (img2, 300, 300, width / 15, height / 10)
