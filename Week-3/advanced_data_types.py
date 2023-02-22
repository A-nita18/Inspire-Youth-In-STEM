#Advanced data types

#Mutables vs immutable

#Mutables are data types that can change or be edited during program life cycle
#add or remove elements

#Immutable are data types that cannot be edited during program life cycle

# 1)List(mutable)

friends = ["Mark","Shem","Manu"]

# or friends = [] for empty list
#add--> append(), extend()
#remove --> pop()

students = ["Shoto","Izuku","Waswa"]
friends.extend(students)
friends.append(80)
friends.reverse()
# 2)Tuples(immutable)
#Type of list that are immutable
stationary = ("pens","ink","eraser","pencil")

#replace the whole tuple
stationaries = ("ruler","clip board","quills")

for stationary in stationaries:
    print(stationary)

numbers = (1,2,3,4,5,6,7,8,9)

# 3)Dictionaries aka dict 

#uses key and value pair
student = {"name": "Anita", "age": 18,"gender":"female","height":"is_tall"}

print(student["name"])
print(student["age"])
print(student["gender"])
print(student["height"])


 #name : "Bob" --> name(key)Bob(value)