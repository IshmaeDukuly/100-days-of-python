
import random

names_string = input("Give me Everybody's names, sperated by a comma. ")

names = names_string.split(", ")

num_item = len(names)
random_choice = random.randint(0, num_item-1)

person_who_will_pay = names[random.choice]
print(person_who_will_pay + "is going to buy the meal today")