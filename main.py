from time import sleep
from random import randint
x = ""
title = ""
menu = ""
age = 0
lactose = ""
acid = ""
diabetes = ""
cholesterol = ""
celiac = ""
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
greeting = ["Hello! Your healthy snacks for today are ", "Welcome back! It's a good day for some ", "Welcome! How about some ", "Hey there! Time for a couple ", "Good to see you again! For today, you should have "]
all_settings = [["berries", "apples", "carrots", "broccoli", "fish", "brown rice", "chicken"], ["", "", "", "", "", ""], ["", ""]]
no_celiac = [[], [], []]
no_cholesterol = [[], [], []]
celiac_cholesterol = [[], [], []]
no_diabetes = [[], [], []]
diabetes_celiac = [[], [], []]
diabetes_cholesterol = [[], [], []]
def settings():
  print("\nAnswer each question with the word \"yes\" or \"no\"\n")
  sleep(2.5)
  print("Are you lactose intolerant?\n")
  lactose = input()
  print("\nDo you have acid reflux?\n")
  acid = input()
  print("\nDo you have diabetes?\n")
  diabetes = input()
  print("\nDo you have high cholesterol?\n")
  cholesterol = input()
  print("\nDo you have celiac disease?\n")
  celiac = input()
while int(age) > 122 or int(age) < 4:
  print("How old are you?\n")
  age = input()
  for i in alphabet:
    if i in age:
      print("\nThat's not a number.\n")
      break
  if int(age) > 122:
    print("\nRight, so you're the oldest person to ever exist. I find that hard to believe.\n")
  elif int(age) < 4:
    print("\nHow are you writing this, exactly?\n")
  else:
    print()
    break
  print()
print(title + "\n")
print("Type in \"start\" to begin\nType in \"settings\" to go to settings\n")
menu = input()
while not x == "this does not matter":
  if menu == "start":
    print("\nHello! Before you start, have you checked the settings menu to make sure everything is correct? Remember, after you restart the program, all data is lost!\n\n\"yes\" or \"no\"\n")
    settings_ = input()
    if settings_ == "no":
      print("\nThen go check them! It's important! Here you go!\n")
      settings()
      break
    elif settings_ == "yes":
      print("\nOK then, let's move on!\n")
      break
    else:
      print("I don't understand what that's supposed to mean.")
  elif menu == "settings":
    settings()
    break
  else:
    if not x == "wrong option":
      print("\nThat's... not an option.\n")
      x = "wrong option"
if lactose == "yes":
  if acid == "yes":
    if diabetes == "yes":
      if cholesterol == "yes":
        if celiac == "yes":
          if int(age) < 18:
            healthy_food = all_settings[0][randint(0, 6)]
          elif int(age) > 17 and int(age) < 65:
            healthy_food = all_settings[1][randint(0, )]
          elif int(age) > 64:
            healthy_food = all_settings[2][randint(0, )]
        elif celiac == "no":
          if int(age) < 18:
            healthy_food = no_celiac[0][randint(0, )]
          elif int(age) > 17 and int(age) < 65:
            healthy_food = no_celiac[1][randint(0, )]
          elif int(age) > 64:
            healthy_food = no_celiac[2][randint(0, )]
      elif cholesterol == "no":
        if celiac == "yes":
          if int(age) < 18:
            healthy_food = no_cholesterol[0][randint(0, )]
          elif int(age) > 17 and int(age) < 65:
            healthy_food = no_cholesterol[1][randint(0, )]
          elif int(age) > 64:
            healthy_food = no_cholesterol[2][randint(0, )]
        elif celiac == "no":
          if int(age) < 18:
            healthy_food = celiac_cholesterol[0][randint(0, )]
          elif int(age) > 17 and int(age) < 65:
            healthy_food = celiac_cholesterol[1][randint(0, )]
          elif int(age) > 64:
            healthy_food = celiac_cholesterol[2][randint(0, )]
    elif diabetes == "no":
      if cholesterol == "yes":
        if celiac == "yes":
          if int(age) < 18:
            healthy_food = no_diabetes[0][randint(0, )]
          elif int(age) > 17 and int(age) < 65:
            healthy_food = no_diabetes[1][randint(0, )]
          elif int(age) > 64:
            healthy_food = no_diabetes[2][randint(0, )]
        elif celiac == "no":
          if int(age) < 18:
            healthy_food = diabetes_celiac[0][randint(0, )]
          elif int(age) > 17 and int(age) < 65:
            healthy_food = diabetes_celiac[1][randint(0, )]
          elif int(age) > 64:
            healthy_food = diabetes_celiac[2][randint(0, )]
      elif cholesterol == "no":
        if celiac == "yes":
          if int(age) < 18:
            healthy_food = diabetes_cholesterol[0][randint(0, )]
          elif int(age) > 17 and int(age) < 65:
            healthy_food = diabetes_cholesterol[1][randint(0, )]
          elif int(age) > 64:
            healthy_food = diabetes_cholesterol[2][randint(0, )]
        elif celiac == "no":
          if int(age) < 18:
            healthy_food = celiac_cholesterol[0][randint(0, )]
          elif int(age) > 17 and int(age) < 65:
            healthy_food = celiac_cholesterol[1][randint(0, )]
          elif int(age) > 64:
            healthy_food = celiac_cholesterol[2][randint(0, )]
