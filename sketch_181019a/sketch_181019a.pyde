a = 0
b = 0
c = 0
d = 0
x = 0


def setup():
    size(640, 480)


def draw():
  ###  #background
    global a, b, c, d
    background(255, 204, 170)
    noStroke()
    #day
    if a >= 100:
        fill(255, 188, 106)
        rect(0, 0, width, height)
    if a >= 140:
        fill(255, 239, 181)
        rect(0, 0, width, height)
    if a >= 160:
        fill(203, 238, 244)
        rect(0, 0, width, height)
    if a >= 180:
        fill(135, 206, 235)
        rect(0, 0, width, height)
    if a >= 320:
        fill(84, 184, 226)
        rect(0, 0, width, height)
    if a >= 400:
        fill(203, 238, 244)
        rect(0, 0, width, height)
    if a >= 420:
        fill(255, 239, 181)
        rect(0, 0, width, height)
    if a >= 440:
        fill(255, 188, 106)
        rect(0, 0, width, height)
    if a >= 500:
        fill(255, 159, 43)
        rect(0, 0, width, height)
    if a >= 620:
        fill(213, 117, 0)
        rect(0, 0, width, height)
    #night
    if a >= 640:
        fill(0, 51, 106)
        rect(0, 0, width, height)
    if a >= 660:
        fill(0, 40, 85)
        rect(0, 0, width, height)
    if a >= 680:
        fill(0, 28, 58)
        rect(0, 0, width, height)
    if a >= 720:
        fill(0, 19, 40)
        rect(0, 0, width, height)
    if a >= 1200:
        fill(55, 116, 140)
        rect(0, 0, width, height)
    if a >= 1350:
        fill(141, 178, 181)
        rect(0, 0, width, height)
    
    
    #sun
    if a >= 1360:
        a = -40
    a += 1
    if a >= 280:
        b += 0
        if a >= 320:
            b += 0.3
            if a >= 720:
                b = 0
    else:
        b += -0.3
        
    if a >= -40:
         fill(254, 255, 189)
         ellipse(0+a, 200+b, 100, 100)
    if a >= 420:
        fill(254, 207, 99)
        ellipse(0+a, 200+b, 100, 100)
    if a >= 440:
        fill(253, 184, 19)
        ellipse(0+a, 200+b, 100, 100)
    
    
  #moon
    if c >= 640:
        c = -760
    c += 1
    if c >= -440:
        d += 0
        if c >= -400:
            d += 0.3
            if c >= 0:
                d = 0
    else:
       d += - 0.3
    fill(240, 253, 255)
    ellipse(720+c, 200+d, 100, 100)
    fill(0, 51, 106)
    ellipse(735+c, 190+d, 96, 96)
    if a >= 660:
        fill(0, 40, 85)
        ellipse(735+c, 190+d, 96, 96)
    if a >= 680:
        fill(0, 28, 58)
        ellipse(735+c, 190+d, 98, 98)
    if a >= 720:
        fill(0, 19, 40)
        ellipse(735+c, 190+d, 100, 100)
    if a >= 1200:
        fill(55, 116, 140)
        ellipse(735+c, 190+d, 102, 102)
    if a >= 1350:
        fill(141, 178, 181)
        ellipse(735+c, 190+d, 102, 102)
        
        
    #mountian
    fill("#867e70")
    triangle(500, height-300, 50, height-80, 1000, height-80)
    
    
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
    
    
    #ground
    fill(0, 128, 0)
    rect(0, height-80, width, 80)

    
    #house
    fill(223, 194, 179)
    rect(width-180, height-120, 159, 100)
    triangle(460, height-120, 619, height-120, 539, height-190)
    quad(460, height-120, 460, height-20, 420, height-60, 420, height-160)
    quad(420, height-160, 460, height-120, 540, height-190, 500, height-230)
    stroke(0)
    line(460, height-120, 460, height-20)
    line(619, height-120, 619, height-20)
    line(460, height-20, 619, height-20)
    line(460, height-120, 539, height-190)
    line(619, height-120, 539, height-190)
    line(460, height-20, 420, height-60)
    line(420, height-60, 420, height-160)
    line(420, height-160, 460, height-120)
    line(499, height-230, 420, height-160)
    line(539, height-190, 499, height-230)
    
    #tree
    noStroke()
    fill("#603E11")
    rect(width/2, height-110, 15, 80)
    fill(0, 128, 0)
    ellipse(width/2-20, height-130, 40, 40)
    ellipse(width/2, height-110, 40, 40)
    ellipse(width/2, height-150, 40, 40)
    ellipse(width/2+20, height-110, 40, 40)
    ellipse(width/2+40, height-130, 40, 40)
    ellipse(width/2+20, height-150, 40, 40)
    ellipse(width/2+20, height-130, 40, 40)
