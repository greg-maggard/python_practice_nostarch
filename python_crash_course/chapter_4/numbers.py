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
cubes = list([value ** 3 for value in range(1, 11)])
print(cubes)