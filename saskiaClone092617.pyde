'''Cloning another Saskia sketch:
https://twitter.com/sasj_nl/status/912777216865513473
Sept 26, 2017 Peter Farrell'''

class Cube:
    def __init__(self,a,b,c,sz,offset):
        self.x = a
        self.y = b
        self.z = c
        self.col = color(255-5*offset,
                         255,
                         255)
        self.sz = sz
        self.offset = offset

    def update(self):
       pushMatrix() #saves the location
       translate(self.x,self.y,self.z)
       self.x = 300 + 150*sin((t-self.offset)/2.0)
       self.z = -300 + 150*cos((t-self.offset)/2.0)
       self.y = 300 + 150*sin((t-self.offset/2.0)/5.0)
       #rotateX(mouseY/20.0)
       #rotateY(mouseX/20.0)
       fill(self.col)
       box(self.sz)
       
       popMatrix() #reset location

cubeList = []
for i in range(20):
    cubeList.append(Cube(0,0,0,50,i))
t = 0 #time
dt = 0.1 #change in time
             
def setup(): #done once
    size(600,600,P3D) #600x600 screen
    background(255) #white
    
def draw(): #infinite loop
    global cubeList,t,dt
    background(255) #white
    for cube in cubeList:
        cube.update()
    t += dt