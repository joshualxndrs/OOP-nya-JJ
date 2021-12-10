from circleclass import *

def main():
    circle_1 = silinder(4,"Blue", 7)
    print(f"Radius of this circle/cylinder {circle_1.getradius()}")
    print(f"Height of this circle/cylinder {circle_1.getheight()}")
    print(f"Color of this circle/cylinder {circle_1.getcolor()}")
    print(f"Area of this circle/cylinder {'{:.2f}'.format(circle_1.getArea())}")
    print(f"Volume of this circle/cylinder {'{:.2f}'.format(circle_1.getvolume())}")

    change_radius = float(input("Set new radius (in numbers): "))
    change_height = float(input("Set new height (in numbers): "))
    change_color = str(input("Set new color: "))

    circle_1.setradius(change_radius)
    circle_1.setheight(change_height)
    circle_1.setcolor(change_color)

    print(f"Updated circle radius is {circle_1.getradius()}, height is {circle_1.getheight()} , color is {circle_1.getcolor()} color")

main()