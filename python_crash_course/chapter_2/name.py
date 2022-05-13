name = "ada lovelace"
print(name.title())

print(name.upper())

name = "aDa LoVeLaCe"
print(name.lower())

#Using format strings:
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = (f"Hello, {full_name.title()}!")
print(message)

#Adding whitespace to strings with tabs or newlines:
print("Python")
##The below will add a tab before the output:
print("\tPython")

#Adding newlines:
print("Languages:\nPython\nC\nJavaScript")

#Adding newlined *AND* tabs:
print("Languages:\n\tPython\n\tC\n\tJavaScript")

#Stripping Whitespace:
favorite_language = " Python "
favorite_language
favorite_language.rstrip()
favorite_language.lstrip()
favorite_language.strip()
favorite_language = favorite_language.strip()
favorite_language

#Try it yourself:
#2-3. Personal Message
name = "Greg"
print(f"Hello, {name}! Would you like to learn some Python today?")
#2-4. Name Cases
name = "gReG mAgGaRd"
print(name.lower())
print(name.upper())
print(name.title())
#2-5. Famous Quote
print('One of my favorite lines from Shakespeare is "We are such stuff as dreams are made on."')
#2-6. Famous Quote 2:
famous_person = "William Shakespeare"
print(f'{famous_person} once said in a play, "We are such stuff as dreams are made on."')
#2-7. Stripping Names:
whitespace_name = '\tGreg Maggard\n'
print(whitespace_name)
print(whitespace_name.lstrip())
print(whitespace_name.rstrip())
print(whitespace_name.strip())

#Practice with numbers
#Try it Yourself
#2-8. The Number 8:
print(3+5)
print(14-6)
print(2*4)
print(32/4)

#2-9. Favorite Number:
favorite_number = 7
print(f'My favorite number is {favorite_number}!')

#2-10: This task is to add comments, but I have already been doing that, so we'll consider it done. 

#2-11. Zen of Python:
import this