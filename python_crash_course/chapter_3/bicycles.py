bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])

#Using format strings to create outputs based on list values:
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

#Try it Yourself:
#3-1. Names:
names = ['Stephen', 'Jen', 'Ryan', 'Abby']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[-1])

#3-2. Greetings:
message = f"Good morning, {names[0]}!"
print(message)
message = f"Good morning, {names[1]}!"
print(message)
message = f"Good morning, {names[2]}!"
print(message)
message = f"Good mornign, {names[3]}!"
print(message)

#3-3. Your Own List:
cars = ['Stinger', 'Mustang', 'Prius', 'Optima']
message = f"I would like to own a {cars[0]}."
print(message)
message = f"I would like to own a {cars[1]}."
print(message)
message = f"I would like to own a {cars[2]}."
print(message)
message = f"I would like to own an {cars[3]}."
print(message)