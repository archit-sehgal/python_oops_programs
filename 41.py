class rectangle:
    def __init__(self,length,width,peri,ar):
        self.length=length
        self.width=width
        self.peri=0
        self.ar=0
    def perimeter(self):
        self.peri=2*(self.length+self.width)
    def area(self):
        self.ar=(self.width*self.length)
    def display(self):
        print(f"length= {self.length}")
        print(f"width= {self.width}")
        print(f"perimter= {self.peri}")
        print(f"area= {self.ar}")
class parallelepipede(rectangle):
    def __init__(self,height):
        self.height=height
        super().__init__(5,7,0,0)
    def volume(self):
        vol=self.height*self.length*self.width
        print(f"volume= {vol}")

call=parallelepipede(10)
call.volume()
call.perimeter()
call.area()
call.display()
