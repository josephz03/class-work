a = 0
b = 0
c = 0
d = 0
u = 0
v = 0
w = 0
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
    triangle(450, height-330, 0, height-80, 1200, height-80)
    
    
    #cloud
    global u, v, w, x
    if u >= 1040:
        u = -480
    u += 5
    if v >= 890:
        v = -240
    v += 3
    if w >= 720:
        w = -100
    w += 2
    if x >= 540:
        x = -600
    x += 7
    y = height/6
    if a >= -40:
        fill(237)
        ellipse(u-400, y+10, 90, 50)
        ellipse(u-370, y+10, 90, 50)
        ellipse(u-340, y+10, 90, 50)
        ellipse(u-310, y+10, 90, 50)
        ellipse(u-370, y-20, 90, 50)
        ellipse(u-340, y-20, 90, 50)
        fill(214)
        ellipse(v-250, y-15, 100, 50)
        ellipse(v-220, y-15, 100, 50)
        ellipse(v-190, y-15, 100, 50)
        ellipse(v-160, y-15, 100, 50)
        ellipse(v-220, y-45, 100, 50)
        ellipse(v-190, y-45, 100, 50)
        fill(200)
        ellipse(w, y, 80, 50)
        ellipse(w+30, y, 80, 50)
        ellipse(w+60, y, 80, 50)
        ellipse(w+90, y, 80, 50)
        ellipse(w+30, y-30, 80, 50)
        ellipse(w+60, y-30, 80, 50)
        fill(188)
        ellipse(x+200, y-10, 120, 50)
        ellipse(x+230, y-10, 120, 50)
        ellipse(x+260, y-10, 120, 50)
        ellipse(x+290, y-10, 120, 50)
        ellipse(x+230, y-40, 120, 50)
        ellipse(x+260, y-40, 120, 50)
    if a >= 640:
        fill(190, 190, 214)
        ellipse(u-400, y+10, 90, 50)
        ellipse(u-370, y+10, 90, 50)
        ellipse(u-340, y+10, 90, 50)
        ellipse(u-310, y+10, 90, 50)
        ellipse(u-370, y-20, 90, 50)
        ellipse(u-340, y-20, 90, 50)
        fill(175, 175, 205)
        ellipse(v-250, y-15, 100, 50)
        ellipse(v-220, y-15, 100, 50)
        ellipse(v-190, y-15, 100, 50)
        ellipse(v-160, y-15, 100, 50)
        ellipse(v-220, y-45, 100, 50)
        ellipse(v-190, y-45, 100, 50)
        fill(150, 150, 188)
        ellipse(w, y, 80, 50)
        ellipse(w+30, y, 80, 50)
        ellipse(w+60, y, 80, 50)
        ellipse(w+90, y, 80, 50)
        ellipse(w+30, y-30, 80, 50)
        ellipse(w+60, y-30, 80, 50)
        fill(128, 128, 174)
        ellipse(x+200, y-10, 120, 50)
        ellipse(x+230, y-10, 120, 50)
        ellipse(x+260, y-10, 120, 50)
        ellipse(x+290, y-10, 120, 50)
        ellipse(x+230, y-40, 120, 50)
        ellipse(x+260, y-40, 120, 50)
    
    
    #ground
    if a >= -40:
        fill("#559900")
        rect(0, height-80, width, 80)
    if a >= 640:
        fill("608038")
        rect(0, height-80, width, 80)
    
    
    #house+frame
    fill(223, 194, 179)
    rect(width-180, height-120, 159, 100)
    triangle(460, height-120, 619, height-120, 539, height-190)
    quad(460, height-120, 460, height-20, 420, height-60, 420, height-160)
    fill(241, 78, 97)
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
    #front
    line(460, height-30, 420, height-70)
    line(460, height-40, 420, height-80)
    line(460, height-50, 420, height-90)
    line(460, height-60, 420, height-100)
    line(460, height-70, 420, height-110)
    line(460, height-80, 420, height-120)
    line(460, height-90, 420, height-130)
    line(460, height-100, 420, height-140)
    line(460, height-110, 420, height-150)
    #side
    line(460, height-30, 619, height-30)
    line(460, height-40, 619, height-40)
    line(460, height-50, 619, height-50)
    line(460, height-60, 619, height-60)
    line(460, height-70, 619, height-70)
    line(460, height-80, 619, height-80)
    line(460, height-90, 619, height-90)
    line(460, height-100, 619, height-100)
    line(460, height-110, 619, height-110)
    line(460, height-120, 619, height-120)
    line(472, height-130, 606, height-130)
    line(482, height-140, 595, height-140)
    line(493, height-150, 585, height-150)
    line(505, height-160, 573, height-160)
    line(516, height-170, 561, height-170)
    line(527, height-180, 550, height-180)
    #window+door
    if a >= -40:
        fill(200)
        rect(513, height-106, 53, 53)
        quad(442, height-74, 442, height-122,  423, height-142, 423, height-94)
    if a >= 630:
        fill(247, 177, 34)
        rect(513, height-106, 53, 53)
        quad(442, height-74, 442, height-122,  423, height-142, 423, height-94)
    if a >= 850:
        fill(150)
        rect(513, height-106, 53, 53)
        quad(442, height-74, 442, height-122,  423, height-142, 423, height-94)
    stroke(222)
    line(514, height-65, 565, height-65)
    line(514, height-93, 565, height-93)
    line(526, height-54, 526, height-105)
    line(552, height-54, 552, height-105)
    line(428, height-90, 428, height-134)
    line(438, height-80, 438, height-124)
    line(441, height-108, 424, height-128)
    line(441, height-86, 424, height-106)
    stroke(255)
    line(514, height-79, 565, height-79)
    line(514, height-78, 565, height-78)
    line(514, height-77, 565, height-77)
    line(540, height-54, 540, height-105)
    line(539, height-54, 539, height-105)
    line(538, height-54, 538, height-105)
    line(441, height-98, 424, height-118)
    line(441, height-97, 424, height-117)
    line(441, height-96, 424, height-116)
    line(434, height-84, 434, height-128)
    line(433, height-85, 433, height-129)
    line(432, height-86, 432, height-130)
    stroke(0)
    fill(149, 132, 96)
    quad(455, height-25, 455, height-82,  445, height-92, 445, height-35)
    fill(0)
    ellipse(453, height-53, 1, 1)
    
    
    #path
    noStroke()
    fill(139,69,19)
    triangle(455, height-24, 445, height-34, -400, height+40)
    
    
    #tree
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
