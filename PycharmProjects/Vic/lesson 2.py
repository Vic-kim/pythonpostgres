# tuple
points = (23,34,34,54,56.7,67,78,34,22,90)
print("I GOT ", points[0]) # prints 1st item
print("We GOT", points[2:]) # print from position 2 and above
print("WE have ", points[2:6])
print("Points are ", points*2)
# tuple are static (immutable)

print("-----LIST-----")
# lists use square brackets
age = [12,34,23,55,67,88,99,78,89,67]

print("AGE IS ", age[3])
print("AGE IS ", age[3:])
age.append(100)

print(age)
age.append(56)
print(age)

age.remove(23)
print(age)

age.remove(age[4])
print(age)

# tuple are immutable lists are commutable

# dictionary
print("----Dictionary----")
car = {'Reg': 'KCF445Z',
       'Color' : 'Red',
       'Year':2009,
       'Make': 'Toyota',
       'Cost':600000,
       'Tel':734787878,
       'Location':'MSA'}
# Dictionary uses key and value approach
print(car['Cost'])
print(car['Year'])
print(car['Make'])
print(car['Tel'])
print(car['Color'])
print(car['Location'])
print(car['Reg'])

#Updating items
car['Tel'] = 5656565
#Adding items
car['Model'] = 'Wish'
print(car)
# del an item, clear the dictionary, to delete the dictionary
del car['Location']
print(car)

car.clear()
print(car)
# delete dictionary
del car
print(car)

# Operators
# Comparison Operators

a = 67
a == 8


