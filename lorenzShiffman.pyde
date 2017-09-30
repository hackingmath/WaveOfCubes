'''Shiffman's Lorenz Attractor'''

x, y, z = 0.01,0,0

a = 10
b = 28
c = 8/3.0

points = []

def setup():
    size(800,800,P3D)
    colorMode(HSB)
    
def draw():
    global a,x,y,z
    background(0)
    dt = 0.01
    dx = (a * (y - x)) * dt
    dy = (x * (b - z) - y) * dt
    dz = (x * y - c * z) * dt
    x += dx
    y += dy
    z += dz
    points.append(PVector(x,y,z))
    #println(str(x)+str(y)+str(z))
    translate(width/2,height/2)
    rotateY(mouseX/20.0)
    rotateX(mouseY/20.0)
    #translate(0,0,-80)
    scale(5)
    #stroke(255)
    noFill()
    hu = 0
    beginShape()
    for pt in points:
        stroke(hu,255,255)
        vertex(pt.x,pt.y,pt.z)
        hu += 0.1
        if hu > 255:
            hu = 0
    endShape()