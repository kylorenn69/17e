## 1 
## Try this.
print("Here we go!")

## 3
## Try this.
firstn = "Bob"
lastn = "Smith"
print(firstn)
print(lastn)


## 4
## Try this.
firstn = "Bob"
lastn = "Smith"
print(f"My name is {firstn} {lastn}")


## 5
## Try this.
firstn = input("What is your first name?")
lastn = input("What is your last name?")
print(f"Your name is {firstn} {lastn}.")


## 7
## Ask the user for a color, and then say
## "___ is a pretty color."
## (Fill in the blank with the actual color.)
color = input("Give me a color: ")
print(f"{color} is a pretty color.")


## 8
## Ask the user for the name of an animal and a plant.
## Then display "The ___ eats ___ every day",
## but fill in the blanks with the animal and the plant.
animal = input("What is your favorite animal? ")
plant = input("What plant does this eat? ")
print(f"The {animal} eats {plant} every day")

## 9
## Try this.
a = "Hello"
b = "Goodbye"
c = a + b
print(c)


## 10
## Try this.
a = input("First word? ")
b = input("Second word? ")
c = a + b
print(c)


## 11
## Try this.
a = 5
b = 3
c = a + b
print(c)


## 12
## Try this.
a = "5"
b = "3"
c = a + b
print(c)


## 13 
## Try this.
a = int("5")
b = int("3")
c = a + b
print(c)


## 14
## Try this.
a = input("Type an integer.")
b = input("Type another integer.")
c = a + b
print(c)


## 15
## Try this.
a = int(input("Type an integer."))
b = int(input("Type another integer."))
c = a + b
print(c)


## 16
## Try this. You will get an error. How do you fix it?
a = int(input("Type an integer."))
b = int(input("Type another integer."))
c = a + b
print(c)

## 17
## Try this. You will get an error. How do you fix it?
favnum = int(input("What is your favorite number?"))
onemore = favnum + 1
print(f"One more would be {onemore}.")


## 18
## Ask the user for two integers.
## Display "The sum of your two numbers is ___".
a = int(input("Type an integer."))
b = int(input("Type another integer."))
c = a + b
print(f"One more would be {c}.")


## 19
## Ask the user for two integers.
## Display "The first number minus the second number is ___".
a = int(input("Type an integer."))
b = int(input("Type another integer."))
c = a - b
print(f"One more would be {c}.")

## 20
## Ask the user for an integer.
## Display "That number plus 2 is ___".
a = int(input("Type an integer."))
c = a + 2
print(f"One more would be {c}.")


## 21
## Ask the user for a number.
## Display "Half of that number is ___".
a = int(input("Type an integer."))
c = a / 2
print(f"One more would be {c}.")


## 22
## Ask the user for the number of questions on a test,
## and ask "how many did you get right?"
## Then, display "You got ___% right". (You'll need to calculate the percent.)

a = int(input("what is the number of questions on your test? "))
b = int(input("how many did you get right?" ))
c = b/a * 100
print(f"You got {c}% right.")