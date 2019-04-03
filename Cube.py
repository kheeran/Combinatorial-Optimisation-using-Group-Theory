import numpy as np


main_array = np.zeros((8,8,8,8,8,8,8,3,3,3,3,3,3,3))

print (main_array)

def record (main_array, config):
    if main_array[config] == True:
        return
    else


def move_up ((a,b,c,d,e,f,g,x1,x2,x3,x4,x5,x6,x7)):
    (a,b,c,d,e,f,g,x1,x2,x3,x4,x5,x6,x7) = (a,b,c,d,e,f,g,x1,x2,x3,x4,x5,x6,x7)

#
# class Cubicle:
#     def __init__(self, position, orientation):
#         self.position = position
#         self.orientation = orientation
#
#     def Up(cubicle):
#         if (0 <= cubicle.position <= 3):
#             cubicle.position += 1 % 4
#
#     def Down(cubicle):
#         if (4 <= cubicle.position <= 7):
#             cubicle.position = (cubicle.position + 1) % 4 + 4
#
#     def Right(cubicle):
#         # TO DO
#
#     def Left(cubicle):
#         # TO DO
#
#     def Front(cubicle):
#         #TO DO
#
#     def Back(cubicle):
#         #To DO
