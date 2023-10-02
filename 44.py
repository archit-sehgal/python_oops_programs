class circle:
    def __init__(self,a,b,r):
        self.a=a
        self.b=b
        self.r=r
    def perimeter(self):
        self.peri=2*3.14*self.r
        print(f"Perimeter of circle is:{self.peri:.2f}") 
    def area(self):
        self.ar=3.14*self.r**2
        print(f"Area of circle is: {self.ar:.2f}")
    def testBelongs(self,x,y):
        distance_squared=(x-self.a)**2+(y-self.b)**2
        if distance_squared<=self.r**2:
            return True
        else:
            return False
call=circle(0,0,5)
points=(3,4)
call.perimeter()
call.area()
print(call.testBelongs(*points))