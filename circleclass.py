class lingkaran:
    def __init__(self, radius = 1.0, color = "Red"):
        self.__radius = radius
        self.__color = color
    def getradius(self):
        return self.__radius
    def getcolor(self):
        return self.__color
    def getArea(self):
        return((3.14)*(self.getradius()**2))
    def setcolor(self, new_color):
        self.__color = new_color
    def setradius(self, new_radius):
        self.__radius = new_radius
    def tostring(self):
        return f"radius: {self.getradius()}" + "\n" + f"Color: {self.getcolor()}"


class silinder(lingkaran):
    def __init__(self, radius=1, color="Red", height = 1.0):
        super().__init__(radius=radius, color=color)
        self.__height = height
    def getheight(self):
        return float(self.__height)
    def setheight (self, height: float):
        self.__height = height
    def tostring (self):
        return f"height: {self.getheight()}"
    def getvolume(self):
        return (3.14)*((self.getradius())**2) * self.getheight()