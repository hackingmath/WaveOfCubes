'''Cloning Saskia Freeke again:
https://twitter.com/sasj_nl/status/913848084416876544
Sept. 29, 2017'''

class Ball:
    def __init__(self,x,y,z,sz,offset,off):
        self.x = x
        self.y = y
        self.z = z
        self.sz = sz
        self.offset = offset
        self.off = off #snake offset
        
    def oscillate(self,t): #off is offset
        self.x = 150*sin(t-self.offset/20.0-self.off)
        self.z = 150*cos(0.5*t-self.offset/20.0-self.off)
        #self.y = 50*sin(t/10.0-self.offset)
        self.sz = 25+25*sin(t/2.0-self.offset/20.0)#-self.off)
        
    def update(self,t):
        self.oscillate(t)
        pushMatrix()#save this location
        translate(self.x,self.y,self.z)
        fill(255,0,0)
        stroke(0,0,255)
        sphereDetail(12)
        sphere(self.sz)
        popMatrix()
        
class Snake: #a string of 6 Balls
    def __init__(self,x,y,z,offset):
        self.offset = offset
        self.x = x - self.offset
        self.y = y# - self.offset
        self.z = z - self.offset
        self.ballList = []
        for i in range(6):
            self.ballList.append(Ball(self.x,
                                           self.y,
                                           self.z,50,
                                           10*i,
                                           self.offset))
    
    def update(self,t):
        for ball in self.ballList:
            ball.update(t)
        
def setup():
    global snakeList,t,dt
    snakeList = []
    size(600,600,P3D)
    t = 0.0 #time
    dt = 0.05 #change in time
    for j in range(4):
        snakeList.append(Snake(100,100+j*100,100,j))
    
def draw():
    background(255)
    global snakeList,t,dt
    translate(width/2.0,height/8.0,0)
    for s in snakeList:
        s.update(t)
    t += dt