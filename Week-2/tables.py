# import module
import tabulate
 
# assign data
mydata = [
    ["Zen", "Clarines"],
    ["Twilight", "Westania"],
    ["Yona", "Bangladesh"],
    ["Dokja", "Seoul"]
]
 
# create header
head = ["Name", "City"]
 
# display table
print(tabulate(mydata, headers=head, tablefmt="grid"))