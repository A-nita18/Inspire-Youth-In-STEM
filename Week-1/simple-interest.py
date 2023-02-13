#Write a program to calculate simple interest
P = input("Enter the principle amount in kshs : ")
R = input("Enter the rate : ")
T = input("Enter the time in years : ")
simple_interest = (int(P) * int(R) * int(T))/int(100)
print("The simple interest is kshs",simple_interest)