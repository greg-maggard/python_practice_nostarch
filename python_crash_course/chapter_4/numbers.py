#first_numbers:
for value in range (1, 5):
    print(value)
## Note that 5 is not included

## To include:
for value in range(1, 6):
    print(value)

##Creating a list of numbers from range():
numbers = list(range(1, 6))
print(numbers)

##using third argument in range() to skip by n amount:
even_numbers = list(range(2, 11, 2))
print(even_numbers)

## Using this method to create a list of squares:
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

# You can also do some very basic functions on lists of numbers:
print(min(squares))
print(max(squares))
print(sum(squares))

# List Comprehensions:
## These are simpler than writing out 'for' loops
##Basically syntactically structured to say "do x for y in z"
squares = [value ** 2 for value in range(1, 11)]
print(squares)

#Try It Yourself:

#4-3 Counting to Twenty:
for i in range(1, 21):
    print(i)

#4-4 One Million:
million = list(range(1,1000001))
for i in million:
    print(i)

#4-5 Summing a Million:
million = list(range(1, 1000001))
print(max(million))
print(min(million))
print(sum(million))

#4-6 Odd Numbers:
for i in range(1, 21, 2):
    print(i)

#4-7 Threes:
threes = list(range(3, 31, 3))
print(threes)

#4-8 Cubes:
cubes = []
for i in range(1, 11):
    cubes.append(i ** 3)
for i in cubes:
    print(i)

#4-9 Cubes Comprehension (similar to the above, but in comprehension form):
cubes_list = list([value ** 3 for value in range(1, 11)])
print(cubes_list)

# Working with a Part of a List:
players = ['charles', 'martina', 'michael', 'florence', 'eli']

## Slicing a list:
print(players[0:3])
print(players[1:4])
### Omitting the first index in the slice will start it at the beginning:
print(players[:4])
### Omitting the second index in the slice will select through the end of the list:
print(players[2:])
### Using a negative index will cause the slicing to start at the end of the list (backward from the first item at index 0):
print(players[-3:])
### You can also include a third argument in the slicing brackets which, like the 'range' function, will tell Python how many steps to skip in counting up:
print(players[0::2])
#### It is further worth noting that leaving the second slice space empty worked fine, causing the slice to run through the end of the list. 

## Looping Through a Slice:
print('Here are the firs tthree players on my team:')
for player in players[0:3]:
    print(player.title())

## Copying a List:
my_foods = ['pizza', 'falafel', 'carrot cake']

### A list can be copied by omitting the indices in the slice:
friend_foods = [my_foods[:]]

print('My favorite foods are:')
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

### To demonstrate that we actually have a copy, we can add different foods to each list:
my_foods.append("cannoli")
friend_foods.append("ice cream")

print('My favorite foods are:')
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

### It's important to note that if we had just set friend_foods equal to my_foods, we would not have created a separate copy.
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print('My favorite foods are:')
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
#### This shows that even if the lists are considered 'separate' early on, they are both modified when they refer to the same thing:

# Try it Yourself:
## 4-10:
my_foods = ['pizza', 'falafel', 'carrot cake', 'apple sauce', 'blueberry muffins', 'steak', 'tamales']
### a. 
print('The first three items in the list are:')
print(my_foods[0:3])
### b. 
print('The middle three items are:')
print(my_foods[2:5])
### c. 
print('The last three items are:')
print(my_foods[-3:])

## 4-11: Making a copy of the pizza toppings from 4-1 to start.
toppings = ['sausage', 'cheese', 'pineapple']
friend_pizza = toppings[:]

### a. Adding a new topping to the original list:
toppings.append('pepperoni')

### b. Adding a new topping to the friend_pizza list:
friend_pizza.append('onions')

### c. Proving that the two are separate by printing thnm out in separate statements:
print("My favorite pizzas are:")
for topping in toppings:
    print(topping)

print("My friend's favorite pizzas are:")
for pizza in friend_pizza:
    print(pizza)

#Tuples (will pick up here later, page 59):