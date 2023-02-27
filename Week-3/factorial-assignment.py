#Print factorials of a number using functions,for loops

def factorial(n):
    factorial = 1
    for i in range(n):
        factorial *= 1 + i
    return factorial

print(factorial(3))
print(factorial(6))

#Write a program to calc simple interest
#SI = P*R*T / 100

def simple_interest(principle,rate,time):
    simp = (principle * rate * time)/100
    print(simp)

simple_interest(24000,10,2)

def linear_equation(m,x,c):
    y = (m * x) *c
    print(y)

linear_equation(4,6,8)