#Print factorials of a number using functions,for loops

def factorial(n):
    for i in range(0,n):
        fact_n = n * (n-i)
        return fact_n

print(factorial(3))
print(factorial(6))

#Write a program to calc simple interest
#SI = P*R*T / 100

def simple_interest(principle,rate,time):
    simp = (principle * rate * time)/100
    print(simp)

simple_interest(24000,10,2)

def linear_Equation(m,x,c):
    y = (m * x) *c
    return y