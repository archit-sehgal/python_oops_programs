class Geometry:
    def __init__(self):
        pass
    def distance(self,a,b):
        a1,a2=a
        b1,b2=b
        sqaured_distance=(a1-b1)**2+(a2-b2)**2
        return sqaured_distance**0.5
    def middle(self,a,b):
        a1,a2=a
        b1,b2=b
        midA=(a1+b1)/2
        midB=(a2+b2)/2
        return (midA,midB)
    def trianglePerimeter(self):
        a=int(input("Enter a side of Triangle: "))
        b=int(input("Enter base of Triangle: "))
        c=int(input("Enter c side of Traingle: "))
        perimeter=a+b+c
        return perimeter
    def triangleIsoscel(self,x,y,z):
        return x==y or y==z or z==x
        
call=Geometry()
a=(1,2)
b=(4,6)
x,y,z=(10,20,10)
print(call.triangleIsoscel(x,y,z))