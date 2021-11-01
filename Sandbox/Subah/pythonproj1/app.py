"""

# String operations
first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder.'
msg = f'{first} [{last}] is a coder.'
print(message)
print(msg)

course = 'python for beginners'
print(len(course))
print(course.upper())
print(course.find('o'))
print(course.replace('p', 'J'))
print('python' in course)

# Arithmetic operations
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)
x = 10
x = x + 3
print(x)
x += 3  # Augmented Assignment operator
print(x)

Order of operations:
parenthesis
Exponentiation
Multiplication or division
Addition or Subtraction

y = 10 + 3 * 2 ** 2
print(y)
z = -2.8
print(round(z))
print(abs(z))

# If statements
is_hot = False
is_cold = False

if is_hot:
    print("It is a hot day")
    print("Drink plenty if water")
elif is_cold:
    print("Its a cold day")
    print("Wear warm cloths")
else:
    print("Its a lovely day")
print("Enjoy your day")

House_Price = 1000000
credit_good = True
if credit_good:
    down_payment = House_Price * 0.1
else:
    down_payment = House_Price * 0.2
print(f"Down payment: ${down_payment}")

has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan")

has_high_income = True
has_good_credit = False

if has_high_income or has_good_credit:
    print("Eligible for loan")

temperature = 35

if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

name = "Subah"
if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters")
else:
    print("Name looks good!")


weight = int(input("Weight: "))
unit = input("(L)bs or (K)gs: ")

if unit.upper() == 'L':
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} lbs")

# While Loop
i = 1
while i <= 5:
    print(i)
    i = i + 1
print("Done")

i = 1
while i <= 5:
    print("*" * i)
    i = i + 1
print("Done")


secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count <= guess_limit :
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
    print("Sorry, you failed")


command = ""
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that")
        
"""



