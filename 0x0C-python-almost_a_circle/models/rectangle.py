#!/usr/bin/python3
"""Module showing properties of rectangle"""

from models.Base import Base


class Rectangle(Base):
    """A rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes attributes of the class reactangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        #getter functions
        @property
        def width(self):
            """gets value for width"""
            return self.__width

        @property
        def height(self):
            """get value fo height"""
            return self.__height

        @property
        def x(self):
            """get value for x"""
            return self.__x

        @property
        def y(self):
            """gets value for y"""
            return self.__y

        #setter functions
        @width.setter
        def width(self, value):
            """sets value for width"""
            if not isinstance(value, int):
                raise TypeError("width must be an integer")

            if value <= 0:
                raise ValueError("width must be > 0")

            self.__width = value

        @height.setter
        def height(self, value):
            """sets value for height"""
            if not isinstance(value, int):
                raise TypeError("height must be an integer")

            if value <= 0:
                raise ValueError("height must be > 0")

            self.__height = value

        @x.setter
        def x(self, value):
            """sets value for x"""
            if not isinstance(value, int):
                raise TypeError("x must be an integer")

            if value <= 0:
                raise ValueError("x must be > 0")

            self.__x = value

        @y.setter
        def y(self, value):
            """sets value for y"""
            if not isinstance(value, int):
                raise TypeError("y must be an integer")

            if value <= 0:
                raise ValueError("y must be > 0")

            self.__y = value

        def area(self):
            """returns area of a reactangle"""
            return (self.__width * self.__height)

        def display(self):
            """displays rectangle with #"""
            for y in range(self.y):
                print("")
            for row in range(self.__height):
                for x in range(self.x):
                    print(" ", end="")
                for column in range(self.__width):
                    print("#", end="")
                print()

        def __str__(self):
            """string representation of the class"""
            return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
                    {self.__width}/{self.__height}"

        def update(self, *args, **kwargs):
            """assign arguments to the attribute"""

            if args and len(args) != 0:
                a = 0
                for arg in args:
                    if a == 0:
                        if arg is None:
                            self.__init__(self.width, self.height, self.x, self.y)
                        else:
                            self.id = arg
                    elif a == 1:
                        self.width = arg
                    elif a == 2:
                        self.height = arg
                    elif a == 3:
                        self.x = arg
                    elif a == 4:
                        self.y = arg
                    a += 1

            elif kwargs and len(kwargs) != 0:
                for k, v in kwargs.items():
                    if k == "id":
                        if v is None:
                            self.__init__(self.width, self.height, self.x, self.y)
                        else:
                            self.id = v
                    elif k == "width":
                        self.width = v
                    elif k == "height":
                        self.height = v
                    elif k == "x":
                        self.x = v
                    elif k == "y":
                        self.y = v

        def to_dictionary(self):
            """returns the dictionary representation of a Rectangle"""

            rec_dictionary = {'id': self.id, 'width': self.__width,
                    'height': self.__height, 'x': self.__x,
                    'y': self.__y}

            return rec_dictionary
