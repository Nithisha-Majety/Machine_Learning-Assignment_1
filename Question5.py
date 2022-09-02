import math
r=30
#area of circle for default radius value 30
_area_of_circle_=math.pi*r*r
print("{:.2f}".format(_area_of_circle_))
#circumference of circle for default radius value 30
_circum_of_circle_=2*math.pi*r
print("{:.2f}".format(_circum_of_circle_))
#user radius input 
rad=int(input("Enter radius of circle"))
#area of circle of user input radius
Area_circle=math.pi*rad*rad
print("{:.2f}".format(Area_circle))
