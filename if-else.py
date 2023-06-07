# print("Welcome to age validation")

# name = input("What's is your name? ")

# age = int(input("Enter your age"))

# if age >18:
#     print("Your age above the age range")
# else:
#     print("Your are permitted")

print("Welcome to the rollercoaster!")
height = int(input("what is your height in cm?"))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 18:
        print("please pay $7.")
    else:
        print("Please pay $12.")
else:
        print("Sorry, you have to grow taller before you can ride ")