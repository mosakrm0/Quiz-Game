import time

Points = 0

print("Welcome To The Quiz Game !!")

time.sleep(2)



# Question 1

answer = input("What is the orange part of an egg called ? > ")

if answer.lower() == "yolk":
    print("Correct !")
    Points += 1
else:
    print("Incorrect !")

#Question 2

answer = input("What is the closest planet to the Sun ? > ")

if answer.lower() == "mercury":
    print("Correct !")
    Points += 1
else:
    print("Incorrect !")

#Question 3

answer = input("How many days are there in a year ? > ")

if answer.lower() == "365":
    print("Correct !")
    Points += 1
else:
    print("Incorrect !")


#Question 4

answer = input("In which country can you find the Eiffel Tower ? > ")

if answer.lower() == "france":
    print("Correct !")
    Points += 1
else:
    print("Incorrect !")


print("""

""")
print(f"     Game Is Over ")
print(f"    You Got {Points} Correct Answers out of 4")

