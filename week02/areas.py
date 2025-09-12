#square
#ask for the information
side = float(input("what is the length of one side of the square?"))

#calculate the value
square_area = side * side

#display the value
print(f"the area of the square is: {square_area:.4f}")

#rectangle
length = float(input("what is the length of the rectangle?"))
width = float(input("what is the width of the rectangle?"))
rectangle_area = length * width
print(f"the area of the rectangle is: {rectangle_area}")

#circle
radius = float(input("what is the radius of the circle?"))
circle_area = 3.14 * radius ** 2
print(f"the area of the circle is: {circle_area}")