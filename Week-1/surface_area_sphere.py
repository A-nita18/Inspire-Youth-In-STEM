#sphere
pi = 3.142
r = input("Enter the radius of the sphere : ")

surface_area_sphere = 4 * pi * int(r)**2
print("The surface area is ",surface_area_sphere)

volume_sphere = 4/3 * pi * int(r)**3
print("The volume is ",volume_sphere)

#cylinder
r = input("Enter radius of cylinder : ")
h = input("Enter height of cylinder : ")

surface_area_cylinder = (2 * pi * int(r)**2 ) + (2 * pi * int(r) * int(h))
print("The surface area is ",surface_area_cylinder)

volume_cylinder = pi * int(r)**2 * int(h)
print("The volume is ",volume_cylinder)
