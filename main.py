def Bio():
  name = input("What is your whole name?")
  res = input("Where do you live?")
  age = input("What is your age?")
  bio = "{} is {} years old and lives in {}.".format(name,age,res)
  return bio

age = -1
if age > 30:
  print("You're over 30!")
else:
  print("You're NOT over 30.")

pizza = input("Do you like pizza?Y/N....")
if pizza == "Y" or pizza == "Yes":
  print("I like pizza too.")
else:
  print("What do you like then?")

food = input("What kind of food do you like?....")
lunch = input("Is it after 12pm? Y/N....")
hungry = input("Are you hungry right now?Y/N.....")

if lunch == "Y" and hungry == "Y":
  print("Let's go find some {} to eat.".format(food))

elif lunch == "Y" and hungry == "N":
  print("OK, let's eat later then.")

else:
  print("We have to wait until 12pm.")




  

