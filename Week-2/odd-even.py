#write a program to list all:

number = 10
if number % 2 == 0:
    print("even number") 
else:
    print("odd number")

#even numbers
for i in range(0,101,2):
    print(i)
     
#odd numbers
for x in range(1,101,2):
    print(x)

#prime numbers

for i in range(2,101): 
    for j in range(2,101):
        if i%j == 0:
            break
    if i == j:
        print(i,end=",")

#write a program to do arithmetic progression of numbers from 1 -100
number = 0
for i in range(0,101):
    ap = number + i
print(ap)