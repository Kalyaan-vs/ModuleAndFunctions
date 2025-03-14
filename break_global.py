# import better_code
from better_code import area_of_square
#
# area = better_code.area_of_square(30)
area = area_of_square(50)
print(f"The new area of the square is {area}")

print(f"Global namespace")
namespace = globals().copy()
for name, obj in namespace.items():
    print(name, obj)
print("*" * 80)
# print(dir())
print(globals())

