from color_point import ColorPoint

class AdvancePoint(ColorPoint):
    #class variables
    COLORS = ["red","green","blue","yellow","black","white"]
    def __init__(self,x,y,color):
        #check the color
        if color not in self.COLORS:
            raise ValueError(f"Invalid color: need to be one of {self.COLORS}")
        self._x=x
        self._y=y
        self._color=color

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value): #this is a SETTER!!
        if value not in self.COLORS:
            raise ValueError(f"Invalid color: need to be one of {self.COLORS}")
        self._color = value

    @classmethod
    def add_color(cls,color):
        #add a new official color to list
        cls.COLORS.append(color)

    @staticmethod
    def distance_2_points(p1,p2):
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

    @staticmethod
    def from_dict(d):
        x=d["x"]
        y=d["y"]
        color=d["color"]
        return AdvancePoint(x,y,color)

point_dict = {"x":1,"y":2,"color":"red"}
p0=AdvancePoint.from_dict({"x":1,"y":2,"color":"red"})
print(p0)
p1=AdvancePoint(1,2,"red")
print(p1)
p2=AdvancePoint(3,4,"pink")
print(p2)
print(p1.x)
#call class methods via class name instead of instance name
AdvancePoint.add_color("coral")
p3 = AdvancePoint(3,4,"coral")
print(p3)
AdvancePoint.distance_2_points(p1,p3)


