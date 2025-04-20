# Today, we learn about classes and objects in Python, specifically about operator overloading. We can use + in  3 + 3  and "hello" + "world" 
# to add, but they have different roles, one is addition in integers and another is concatenation in strings.
# But in python, we can assign operator like -, > to perform different operations, thats called operator overloading.
#  In Objects, we can give an operator its own different meaning to perfrom different operation.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def __gt__(self, other):
        return self.area() > other.area()


rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 7)

if rect1 > rect2:
    print("rect1's area is bigger than rect2's area")
else:
    print("rect2's area is bigger than rect1's area")

        