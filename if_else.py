# 1
# Try this.
# You'll get an error having to do with the quotation marks.
# Why do you think that is?
name = "bob"
print(name)


# 2
# Try this.
name = "bob"
if name == "joe":
    print("Your name rhymes with low.") 
else: 
    print(f"Hey {name}.") 
     

# 3
# Copy and modify the above example so that if the name is “dell”, it will print “That’s a computer brand.” 
name = "bob"
if name == "dell":
    print("That’s a computer brand.") 
else: 
    print(f"Hey {name}.") 
     

# 4
# Try this.
age = 5
if age < 21: 
    print("You can't drink alcohol in the US yet.") 
else: 
    print("You are legally allowed to drink. Drink responsibly 😊 ") 
     

# 5
# Copy and modify the above example so that the legal drinking age is 40. (Just to be funny.) 
age = 5
if age < 40: 
    print("You can't drink alcohol in the US yet.") 
else: 
    print("You are legally allowed to drink. Drink responsibly 😊 ") 
 

# 6
# Try this. Notice that it will ask for input. 
name = input("What is your name?") 
if name == "joe": 
    print("Your name rhymes with low.") 
else: 
    print(f"Hey {name}.") 

 
# 7
# Modify the above example so that if the name is “cobb”, it will say “That’s a Ft Gordon building!” 
name = input("What is your name?") 
if name == "cobb": 
    print("That’s a Ft Gordon building!") 
else: 
    print(f"Hey {name}.") 

 
# 8 
# Try this. 
age = 10 
ageNextYear = age + 1 
print(ageNextYear) 
     

# 9
# Try this. Note: you will get an error. 
age = int(input("How old are you?"))
ageNextYear = age + 1 
print(ageNextYear) 
     

# 10 
# Try this. 
age = int(input("How old are you?")) 
ageNextYear = age + 1 
print(ageNextYear) 
     
# 11
# Copy and modify the previous example to do the following: 
# - Ask the user for age 
# - Say “You will be 65 years old in 11 years", but put the correct number instead of 11. 
age = int(input("How old are you?")) 
years = 65 - age
print(f'You will be 65 years old in {years} years') 
     

# 12
# Try this. Note: you will get an error. 
age = int(input("How old are you?")) 
if age < 21 : 
    print("You can't drink alcohol in the US yet.") 
else: 
    print("You are legally allowed to drink. Drink responsibly 😊 ") 
     

# 13
# Modify the above example so it works. You’ll use the `int` function. 

 
# 14
# Copy and modify the above example so that it shows how many years remain until you can drink (but only display that if you’re under the drinking age). 
age = int(input("How old are you?")) 
if age < 21 :
    left = 21 - age
    print(f"You can drink in {left} years") 
 

# 15
# Write a program that takes a name from the user. If the name is the letter “A”, say “Your name is just the letter A? That’s kinda cool”.  Otherwise, say “Ok, your name is ___”. 
name = input("What is your name?") 
if name.upper() == "A": 
    print("Your name is just the letter A? That's kinda cool") 
else: 
    print(f"Ok, your name is {name}.") 

     

# 16
# Try this: 
birthyear = int(input('What is your birthyear? '))
if birthyear < 2000: 
    print("You were born before 2000.") 
elif birthyear == 2000: 
    print("You were born in 2000.") 
else: 
    print("You were born after 2000.") 

 
# 17
# Modify the previous example to ask the user for year of birth (using input). 

 
# 18
# Ask the user how many French fries they want. Display different responses depending on how many they request. (Examples: “That’s way too many!”, etc.) 
frenchofthefry = int(input('How many french fry you want?'))
if frenchofthefry > 20000:
    print('Too many french fry! ABORT!!! ABORT!!!')
elif frenchofthefry == 69:
    print('Nice!')
else:
    print('Not enough french fry')


# 19
# Try this. Did it print what you expected?
# x = 44
x = 5
if x < 20: 
    print("A") 
    print("B") 
print("C") 

# 20
# Modify the value of x in the previous example. Does it print what you expected? 


# 21
# Ask the user for a number.
# If the user gives a number more than 50, 
#    then ask "What is your name?"
#    and display "Hello" followed by the name.
# If the user gives any other number,
#    then ask "How did you pick that number?"
#    and regardless of what they say, display "I see."
# After all of that, say "Have a good day."
num = int(input('Gime number idot: '))
if num > 50:
    name = input('What your name? ')
    print(f'Hello {name}')
else:
    input('How did you pick that number?')
    print('I see.')
print('Have a good day.')


# 22
# Write a program that takes a number from the user. Display the number doubled. Then do a sequence of creative if statements of your choice. Some examples: if the number is greater than 30, display “that’s pretty big.” If the number is negative, display “Really? Negative? Interesting”.  
num = int(input('Gime a num: '))
if num == 69:
    print('nice')
elif num < 0:
    print('Really? Negative? Interesting')

num * 2
print(f'Your number doubled is {num}')
 
# 23
# Ask the user for the cost of a single item and the quantity purchased. Print the total cost. 
cost = float(input('What cost of item? '))
quantity = int(input('How many of it you get? '))
total = cost * quantity
print(total)

 
# 24
# Modify the previous example so that the shop gives a discount of 10% if you buy at least 20 of an item.  
# For example, if one item costs $5, and you’re buying 20, total cost would be $90. 

cost = float(input('What cost of item? '))
quantity = int(input('How many of it you get? '))
total = cost * quantity

if quantity >= 20:
    discount = total * .10
else:
    discount = 0

total -= discount
print(total)

     

# 25
# Ask the user for a number. Print the absolute value of the number without using the abs function. 
num = int(input('Enter a number: '))
if num > 0:
    print(num * 1)
else:
    print(num * -1)

# 26
# Ask the user for a temperature in Celsius, and display the temperature in Fahrenheit. 
num = int(input('Enter temp in C: '))
print(num * 1.8 + 32)

# 27
# Same as previous example, but backwards. 
num = int(input('Enter temp in F: '))
print((num - 32) * .5556)

# 28
# Combine the two previous examples: ask the user for a number and which way to convert. \
num = int(input('Enter num: '))
conv = input('Convert to F or C? ')
if conv.lower() == 'c':
    print(num * 1.8 + 32)
elif conv.lower() == 'f':
    print((num - 32) * .5556)
else:
    print('You fucked up')