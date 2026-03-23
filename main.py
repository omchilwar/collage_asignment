import maths
print("Choose a shape to find area:")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

option=int(input("enter the option"))

if option==1:
    r = float(input("Enter radius of circle: "))
    area = maths.area_circle(r)
    print("Area of Circle =", area)
elif option==2:
    l=float(input("enter the length "))
    w=float(input("enter the width "))    
    output=maths.area_rectangle(l,w)
    print("area of your rectangle is",output)
elif option==3:
    l=float(input("enter the length "))
    w=float(input("enter the width "))    
    output=maths.area_triangle(l,w)
    print("area of your triangle is",output)
else:
    print("enter corect option...")    

