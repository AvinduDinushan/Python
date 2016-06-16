fruits = ['Banana','Apple','Mango','Tomato','Amberella']
vegetables = ['Pumpkin','Tomato','Carrot','Amberella']

for common in list(set(fruits).intersection(set(vegetables))):
    print common
for alle in list(set(fruits).union(set(vegetables))):
    print alle
