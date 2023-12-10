from Triangle import Triangle
from Square import Square
class RightPyramid(Triangle, Square):
    def __init__(self, base, slant_height , height):
        self.base = base
        self.slant_height = slant_height
        super().__init__(base, height)
        super(Square,self).__init__(base,base)
    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area
