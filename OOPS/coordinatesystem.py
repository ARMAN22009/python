class Point():

    def __init__(self,x,y):
        self.x_cor=x
        self.y_cor=y

    def __str__(self):
        return "<{},{}>".format(self.x_cor,self.y_cor)
    
    def distance_from_origin(self):
        p=((self.x_cor-0)**2  +  (self.y_cor-0)**2)**(.5)
        return p
    
    def distance_from_other(self,other):
        p=((self.x_cor-other.x_cor)**2  +  (self.y_cor-other.y_cor)**2)**(.5)
        return p
    
p1=Point(3,4)
p2=Point(-3,-4)
p3=Point(0,0)

print(p1.distance_from_origin())
print(p1.distance_from_other(p2))               #one object is specified as p1 so only one needed
print(p1.distance_from_other(p1))  


class Line:

    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def __str__(self):
        return "{}x + {}y + {} = 0".format(self.a,self.b,self.c)
    
    def point_on_line(Line,Point):
      
        if (Point.x_cor*Line.a+Point.y_cor*Line.b+Line.c==0):
            print("points ",Point.x_cor,"&",Point.y_cor," are on line.")
        else:
            print("doesn't lies on line.")


    def shortest_dis_point_line(Line,Point):
        v=abs(Point.x_cor*Line.a+Point.y_cor*Line.b+Line.c)         #absolute valve for abs
        u=((Line.a)**2 + (Line.b)**2)**(.5)
        return v/u
    
    def intersection(Line):
        
l1=Line(3,4,-11)
print(l1)
print(l1.point_on_line(p1))
print(l1.shortest_dis_point_line(p3))
