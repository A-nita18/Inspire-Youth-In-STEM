names = ["Anita", "Dokja", "Yona", "Sokka", "Laura"]
#Accessing items in a list

print(names)
print(names[0])
print(names[-1])
print(names[2])
print(names[0:3])

fruits = ["apples","avocado","pineapple","cherry","kiwi","passion"]
print(fruits[0:-1])
print(fruits[3])
print("My favourite fruit is ",fruits[-2])
print("My favourite fruit is ",fruits[-2].upper())

#adding two lists
vegetables = ["broccoli","celery","kales","carrot","spinach","pumpkin","cassava"]
stationary = ["pens","paper","scissors","ruler","eraser","cellotape"]
shopping = vegetables + stationary
print(shopping)
print(shopping[5])

for vegetable in vegetables:
    print(vegetable)

for shopping in shopping:
    print(shopping)

print("My name is " + names[3] +" and my favourite fruit is " + fruits[3])
