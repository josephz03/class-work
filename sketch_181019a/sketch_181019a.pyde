# while loop to change values
# convert to draw
# move ellipse
# reset ball
# Make clouds move
a = 0
b = 0
c = 0
d = 0
x = 0


def setup():
    size(640, 480)


def draw():
  ###  #background
    background(225)
    noStroke()
    global a, b, c, d
    
    
    if a >= 240:
        fill("#87CEEB")
        rect(0, 0, width, height)

    
    #sun
    if a >= 1360:
        a = -40
    a += 1
    if a >= 280:
        b += 0
        if a >= 320:
            b += 0.3
            if a > 660:
                b = 0
    else:
        b += -0.3
    fill(253, 184, 19)
    ellipse(0+a, 200+b, 100, 100)
    
    
  ###  #moon
    if c >= 2000:
        c = -40
    c += 1
    if c >= 560:
        d += 0
        if c >= 640:
            d += 0.3
            if c <= 640:
                d = 0
                if c >= 1280:
                    d = 0
    else:
        d += -0.3
    fill("#F0C420")
    ellipse(-640+c, 200+d, 100, 100)
    
    #cloud
    global x
    if x >= 640:
        x = 0
    x += 3
    fill(237)
    y = height/6
    ellipse(x, y, 50, 50)
    ellipse(x+30, y, 50, 50)
    ellipse(x+60, y, 50, 50)
    ellipse(x+90, y, 50, 50)
    ellipse(x+30, y-30, 50, 50)
    ellipse(x+60, y-30, 50, 50)
    
    # ground
    fill(0, 128, 0)
    rect(0, height-50, width, 50)

        
    # tree
    fill("#603E11")
    rect(width/2, height-180, 20, 130)
    fill(0, 128, 0)
    ellipse(width/2-20, height-200, 50, 50)
    ellipse(width/2, height-180, 50, 50)
    ellipse(width/2, height-220, 50, 50)
    ellipse(width/2+20, height-180, 50, 50)
    ellipse(width/2+40, height-200, 50, 50)
    ellipse(width/2+20, height-220, 50, 50)
