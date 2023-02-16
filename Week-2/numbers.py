numbers = []

sum_num = 0
numbers.append(input("Enter the first ten numbers: "))
for number in numbers:
    sum_num = sum_num + int(number)

avg_num = sum_num / 10
print(avg_num)