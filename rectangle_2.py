from rectangle import Rectangle, Square, Circle

rec_1 = Rectangle(5, 10)
rec_2 = Rectangle(3, 4)

print(f'{rec_1.get_area()}\n'
      f'{rec_2.get_area()}\n')

square_1 = Square(4)
square_2 = Square(5)

print(f'{square_1.get_area_square()}\n'
      f'{square_2.get_area_square()}\n')

circle_1 = Circle(5)
circle_2 = Circle(7)

print(f'{round(circle_1.get_area_circle(), 2)}\n'
      f'{round(circle_2.get_area_circle(), 2)}\n')
