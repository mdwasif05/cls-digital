print("*** AREA CALCULATOR ***")

print("""Press 1 to get the area of a square
      Press 2 to get the area of a rectangle
      Press 3 to get the area of a circle
      Press 4 to get the area of a triangle""")

choice=int(input('Enter a Number between 1 to 4: '))

if choice==1:
    side=float(input('Enter the length of one side: '))
    area=side**2
    print('The Area of a Square is ',area)

elif choice==2:
    length=float(input('Enter the length of rectangle: '))
    width=float(input('Enter the width of rectangle: '))
    area=length*width
    print('The Area of a Rectangle is ',area)

elif choice==3:
    radius=float(input('Enter the radius of cicle: '))
    area=3.14*radius**2
    print('The Area of a Circle is ',area)

elif choice==4:
    base=float(input('Enter the base of triangle: '))
    height=float(input('Enter the height of triangle: '))
    area=0.5*base*height
    print('The Area of a Triangle is ',area)

else:
    print("--------ENTER VALID INPUT---------")

