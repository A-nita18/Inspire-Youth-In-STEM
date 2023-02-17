#Assignment 10 : Get the average of numbers in a list by first entering them as input
numbers = []

n = int(input("Enter the number of elements: "))
for i in range(0,n):
    element = int(input("Enter the elements: "))
    numbers.append(element)

avg_num = sum(numbers)/n
print("The created list: ",numbers)
print("The average is: ",avg_num)