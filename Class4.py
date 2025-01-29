import math
class point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def show(self):
        print(self.x,self.y)
    def move(self,x,y):
        self.x=x
        self.y=y
    def dist(self,other_point):
        return math.sqrt((self.x - other_point.x)**2+(self.y - other_point.y)**2)
x1=float(input())
y1=float(input())
p1=point(x1,y1)
x2=float(input())
y2=float(input())
p2=point(x2,y2)
p1.show()
p2.show()
distance=p1.dist(p2)
new_x=float(input())
new_y=float(input())
p1.move(new_x,new_y)
p1.show()