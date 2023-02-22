#Draw a diamond with a for loop
h = eval(input("Enter the diamond's height: "))
for x in range(h):
    print(" " * (h-x), "*" * (2*x + 1))
for x in range(h-2, -1, -1):
    print(" " * (h-x), "*" * (2*x + 1))

#Draw a triangle using a for loop
h = eval(input("Enter the triangle's height: "))
for x in range(h):
    print(" " * (h-x), "x" * (2*x + 1))

#Draw pascal's triangle using for loop


#Write a program that solves quadratic equation 

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

d = (b**2) - (4*a*c)
y = (-(b) * ((d)** 0.5)) / (2 * a)
print(y)

#using a for loop draw pascals triangle
rows = int(input("Enter the number of rows: "))
k = 1
for i in range(1,rows+1):
	for a in range(1,(rows-i)+1):
		print(" ",end="")
	for j in range(0,i):
		if j==0 or i==0:
			k=1
		else:
			k=k*(i-j)//j
		print(k,end=" ")
	print()