from time import sleep
from random import randint
x = ""
menu = ""
age = 0
lactose = "no"
acid = "no"
diabetes = "no"
cholesterol = "no"
celiac = "no"
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
greeting = ["Hello! Your healthy snacks for today are ", "Welcome back! It's a good day for some ", "Welcome! How about some ", "Hey there! Time for a couple ", "Good to see you again! For today, you should have "]
all_settings = [["berries", "apples", "carrots", "broccoli", "fish", "brown rice", "chicken"], ["apples", "oranges", "spinach", "avocados", "turkey", "fish"], ["blueberries", "quinoa", "kale", "chicken"]]
no_celiac = [["chicken", "berries", "apples", "sweet potatoes"], ["chicken", "turkey", "raspberries", "carrots"], ["strawberries", "brown rice", "fish", "lentils"]]
no_cholesterol = [["strawberries", "blackberries", "bananas", "chicken", "potatoes"], ["peaches", "beans", "apples", "potatoes"], ["chicken", "turkey", "white rice", "lentils"]]
celiac_cholesterol = [["chicken", "berries", "oranges"], ["eggs", "dates", "beans", "turkey"], ["beans", "kale", "apples"]]
no_diabetes = [["berries", "tomatoes", "eggs", "carrots"], ["spinach", "grapes", "chicken", "turkey", "rice"], ["beans", "apples", "oranges", "corn"]]
diabetes_celiac = [["chicken", "apples", "strawberries"], ["raspberries", "oranges", "spinach"], ["quinoa", "mangos"]]
diabetes_cholesterol = [["apples", "chicken", "fish", "blueberries"], ["broccoli", "avocados"], ["apples", "blueberries"]]
celiac_cholesterol_diabetes = [["chicken", "fish", "broccoli"], ["apples", "blueberries"], ["avocados", "blueberries", "apples"]]
no_acid = [["broccoli", "oranges", "strawberries"], ["blueberries", "apples", "oranges"], ["broccoli", "avocados", "blueberries"]]
celiac_acid = [["strawberries", "broccoli"], ["apples", "chicken", "blueberries"], ["apples", "kale"]]
cholesterol_acid = [["turkey", "oranges"], ["chicken", "blueberries"], ["strawberries", "oranges"]]
celiac_cholesterol_acid = [["apples", "oranges", "avocados"], ["oranges", "strawberries"], ["kale", "fish"]]
acid_diabetes = [["apples", "broccoli", "avocados"], ["strawberries", "blueberries"], ["chicken", "apples", "kale"]]
acid_diabetes_celiac = [["chicken", "strawberries", "blueberries", "oranges"], ["fish", "kale"], ["avocados", "oranges", "kale"]]
acid_diabetes_cholesterol = [["avocados", "strawberries"], ["apples", "chicken"], ["apples", "avocados"]]
acid_diabetes_celiac_cholesterol = [["chicken", "blueberries"], ["apples", "kale", "blueberries"], ["apples", "kale"]]
no_lactose = [["strawberries", "mangos", "broccoli"], ["almond yogurts", "carrots", "blackberries"], ["bell peppers", "apples", "oranges"]]
celiac_lactose = [["grapes", "spinach", "mangos"], ["peaches", "blueberries", "apples", "oranges"], ["bananas", "lactose-free milk", "grapefruit", "grapes"]]
cholesterol_lactose = [["turkey", "avocados"], ["strawberries", "avocados"], ["apples", "turkey", "kale"]]
celiac_cholesterol_lactose = [["kale", "oranges", "avocados", "strawberries"], ["fish", "kale"], ["turkey", "avocados", "kale"]]
diabetes_lactose = [["strawberries", "turkey"], ["turkey", "fish"], ["turkey", "blueberries", "avocados"]]
diabetes_celiac_lactose = [["strawberries", "apples"], ["apples", "avocados", "turkey"], ["blueberries", "apples"]]
lactose_diabetes_cholesterol = [["kale", "fish"], ["avocados", "kale"], ["kale", "apples"]]
lactose_diabetes_celiac_cholesterol = [["strawberries", "oranges", "avocados"], ["kale", "oranges", "apples", "avocados"], ["apples", "kale"]]
lactose_acid = [["oranges", "avocados", "turkey"], ["fish", "strawberries"], ["turkey", "avocados"]]
lactose_celiac_acid = [["turkey", "oranges", "strawberries"], ["turkey", "oranges", "avocados"], ["avocados", "blueberries"]]
lactose_acid_cholesterol = [["turkey", "fish"], ["fish", "avocados"], ["apples", "kale", "avocados"]]
lactose_acid_celiac_cholesterol = [["apples", "brown rice", "broccoli"], ["oranges", "lentils"], ["bananas", "blueberries"]]
lactose_acid_diabetes = [["sweet potatoes", "oranges", "quinoa"], ["turkey", "chicken", "peaches", "apples"], ["bananas", "strawberries"]]
lactose_acid_diabetes_celiac =  [["almond milk", "raspberries", "spinach"], ["chicken", "sweet potatoes", "kale"], ["bananas", "fish", "turkey"]]
lactose_acid_diabetes_cholesterol = [["brown rice", "apples", "bananas"], ["oranges", "avocados", "chicken"], ["dates", "turkey", "bell peppers", "grapefruits"]]
nothing = [["fish", "broccoli", "apples", "bananas"], ["oranges", "chicken", "almonds", "beans", "melons"], ["beets", "mangos", "eggs"]]
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
print("Eat of the Day\n")
sleep(1.5)
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
            healthy_food = all_settings[1][randint(0, 5)]
          elif int(age) > 64:
            healthy_food = all_settings[2][randint(0, 3)]
        elif celiac == "no":
          if int(age) < 18:
            healthy_food = no_celiac[0][randint(0, 3)]
          elif int(age) > 17 and int(age) < 65:
            healthy_food = no_celiac[1][randint(0, 3)]
          elif int(age) > 64:
            healthy_food = no_celiac[2][randint(0, 3)]
      elif cholesterol == "no":
        if celiac == "yes":
          if int(age) < 18:
            healthy_food = no_cholesterol[0][randint(0, 4)]
          elif int(age) > 17 and int(age) < 65:
            healthy_food = no_cholesterol[1][randint(0, 3)]
          elif int(age) > 64:
            healthy_food = no_cholesterol[2][randint(0, 3)]
        elif celiac == "no":
          if int(age) < 18:
            healthy_food = celiac_cholesterol[0][randint(0, 2)]
          elif int(age) > 17 and int(age) < 65:
            healthy_food = celiac_cholesterol[1][randint(0, 3)]
          elif int(age) > 64:
            healthy_food = celiac_cholesterol[2][randint(0, 2)]
    elif diabetes == "no":
      if cholesterol == "yes":
        if celiac == "yes":
          if int(age) < 18:
            healthy_food = no_diabetes[0][randint(0, 3)]
          elif int(age) > 17 and int(age) < 65:
            healthy_food = no_diabetes[1][randint(0, 4)]
          elif int(age) > 64:
            healthy_food = no_diabetes[2][randint(0, 3)]
        elif celiac == "no":
          if int(age) < 18:
            healthy_food = diabetes_celiac[0][randint(0, 2)]
          elif int(age) > 17 and int(age) < 65:
            healthy_food = diabetes_celiac[1][randint(0, 2)]
          elif int(age) > 64:
            healthy_food = diabetes_celiac[2][randint(0, 1)]
      elif cholesterol == "no":
        if celiac == "yes":
          if int(age) < 18:
            healthy_food = diabetes_cholesterol[0][randint(0, 3)]
          elif int(age) > 17 and int(age) < 65:
            healthy_food = diabetes_cholesterol[1][randint(0, 1)]
          elif int(age) > 64:
            healthy_food = diabetes_cholesterol[2][randint(0, 1)]
        elif celiac == "no":
          if int(age) < 18:
            healthy_food = celiac_cholesterol_diabetes[0][randint(0, 2)]
          elif int(age) > 17 and int(age) < 65:
            healthy_food = celiac_cholesterol_diabetes[1][randint(0, 1)]
          elif int(age) > 64:
            healthy_food = celiac_cholesterol_diabetes[2][randint(0, 2)]
  elif acid == "no":
    if diabetes == "yes":
      if cholesterol == "yes":
        if celiac == "yes":
          if int(age) < 18:
            healthy_food = no_acid[0][randint(0, 2)]
          elif int(age) > 17 and int(age) < 65:
            healthy_food = no_acid[1][randint(0, 2)]
          elif int(age) > 64:
            healthy_food = no_acid[2][randint(0, 2)]
        elif celiac == "no":
          if int(age) < 18:
            healthy_food = celiac_acid[0][randint(0, 1)]
          elif int(age) > 17 and int(age) < 65:
            healthy_food = celiac_acid[1][randint(0, 2)]
          elif int(age) > 64:
            healthy_food = celiac_acid[2][randint(0, 1)]
      elif cholesterol == "no":
        if celiac == "yes":
          if int(age) < 18:
            healthy_food = cholesterol_acid[0][randint(0, 1)]
          elif int(age) > 17 and int(age) < 65:
            healthy_food = cholesterol_acid[1][randint(0, 1)]
          elif int(age) > 64:
            healthy_food = cholesterol_acid[2][randint(0, 1)]
        elif celiac == "no":
          if int(age) < 18:
            healthy_food = celiac_cholesterol_acid[0][randint(0, 2)]
          elif int(age) > 17 and int(age) < 65:
            healthy_food = celiac_cholesterol_acid[1][randint(0, 1)]
          elif int(age) > 64:
            healthy_food = celiac_cholesterol_acid[2][randint(0, 1)]
    elif diabetes == "no":
      if cholesterol == "yes":
        if celiac == "yes":
          if int(age) < 18:
            healthy_food = acid_diabetes[0][randint(0, 2)]
          elif int(age) > 17 and int(age) < 65:
            healthy_food = acid_diabetes[1][randint(0, 1)]
          elif int(age) > 64:
            healthy_food = acid_diabetes[2][randint(0, 2)]
        elif celiac == "no":
          if int(age) < 18:
            healthy_food = acid_diabetes_celiac[0][randint(0, 3)]
          elif int(age) > 17 and int(age) < 65:
            healthy_food = acid_diabetes_celiac[1][randint(0, 1)]
          elif int(age) > 64:
            healthy_food = acid_diabetes_celiac[2][randint(0, 2)]
      elif cholesterol == "no":
        if celiac == "yes":
          if int(age) < 18:
            healthy_food = acid_diabetes_cholesterol[0][randint(0, 1)]
          elif int(age) > 17 and int(age) < 65:
            healthy_food = acid_diabetes_cholesterol[1][randint(0, 1)]
          elif int(age) > 64:
            healthy_food = acid_diabetes_cholesterol[2][randint(0, 1)]
        elif celiac == "no":
          if int(age) < 18:
            healthy_food = acid_diabetes_celiac_cholesterol[0][randint(0, 1)]
          elif int(age) > 17 and int(age) < 65:
            healthy_food = acid_diabetes_celiac_cholesterol[1][randint(0, 2)]
          elif int(age) > 64:
            healthy_food = acid_diabetes_celiac_cholesterol[2][randint(0, 1)]
elif lactose == "no":
  if acid == "yes":
    if diabetes == "yes":
      if cholesterol == "yes":
        if celiac == "yes":
          if int(age) < 18:
            healthy_food = no_lactose[0][randint(0, 2)]
          elif int(age) > 17 and int(age) < 65:
            healthy_food = no_lactose[1][randint(0, 2)]
          elif int(age) > 64:
            healthy_food = no_lactose[2][randint(0, 2)]
        elif celiac == "no":
          if int(age) < 18:
            healthy_food = celiac_lactose[0][randint(0, 2)]
          elif int(age) > 17 and int(age) < 65:
            healthy_food = celiac_lactose[1][randint(0, 3)]
          elif int(age) > 64:
            healthy_food = celiac_lactose[2][randint(0, 3)]
      elif cholesterol == "no":
        if celiac == "yes":
          if int(age) < 18:
            healthy_food = cholesterol_lactose[0][randint(0, 1)]
          elif int(age) > 17 and int(age) < 65:
            healthy_food = cholesterol_lactose[1][randint(0, 1)]
          elif int(age) > 64:
            healthy_food = cholesterol_lactose[2][randint(0, 2)]
        elif celiac == "no":
          if int(age) < 18:
            healthy_food = celiac_cholesterol_lactose[0][randint(0, 3)]
          elif int(age) > 17 and int(age) < 65:
            healthy_food = celiac_cholesterol_lactose[1][randint(0, 1)]
          elif int(age) > 64:
            healthy_food = celiac_cholesterol_lactose[2][randint(0, 2)]
    elif diabetes == "no":
      if cholesterol == "yes":
        if celiac == "yes":
          if int(age) < 18:
            healthy_food = diabetes_lactose[0][randint(0, 1)]
          elif int(age) > 17 and int(age) < 65:
            healthy_food = diabetes_lactose[1][randint(0, 1)]
          elif int(age) > 64:
            healthy_food = diabetes_lactose[2][randint(0, 2)]
        elif celiac == "no":
          if int(age) < 18:
            healthy_food = diabetes_celiac_lactose[0][randint(0, 1)]
          elif int(age) > 17 and int(age) < 65:
            healthy_food = diabetes_celiac_lactose[1][randint(0, 1)]
          elif int(age) > 64:
            healthy_food = diabetes_celiac_lactose[2][randint(0, 1)]
      elif cholesterol == "no":
        if celiac == "yes":
          if int(age) < 18:
            healthy_food = lactose_diabetes_cholesterol[0][randint(0, 1)]
          elif int(age) > 17 and int(age) < 65:
            healthy_food = lactose_diabetes_cholesterol[1][randint(0, 2)]
          elif int(age) > 64:
            healthy_food = lactose_diabetes_cholesterol[2][randint(0, 1)]
        elif celiac == "no":
          if int(age) < 18:
            healthy_food = lactose_diabetes_celiac_cholesterol[0][randint(0, 2)]
          elif int(age) > 17 and int(age) < 65:
            healthy_food = lactose_diabetes_celiac_cholesterol[1][randint(0, 3)]
          elif int(age) > 64:
            healthy_food = lactose_diabetes_celiac_cholesterol[2][randint(0, 1)]
  elif acid == "no":
    if diabetes == "yes":
      if cholesterol == "yes":
        if celiac == "yes":
          if int(age) < 18:
            healthy_food = lactose_acid[0][randint(0, 2)]
          elif int(age) > 17 and int(age) < 65:
            healthy_food = lactose_acid[1][randint(0, 1)]
          elif int(age) > 64:
            healthy_food = lactose_acid[2][randint(0, 1)]
        elif celiac == "no":
          if int(age) < 18:
            healthy_food = lactose_celiac_acid[0][randint(0, 1)]
          elif int(age) > 17 and int(age) < 65:
            healthy_food = lactose_celiac_acid[1][randint(0, 1)]
          elif int(age) > 64:
            healthy_food = lactose_celiac_acid[2][randint(0, 2)]
      elif cholesterol == "no":
        if celiac == "yes":
          if int(age) < 18:
            healthy_food = lactose_acid_cholesterol[0][randint(0, 2)]
          elif int(age) > 17 and int(age) < 65:
            healthy_food = lactose_acid_cholesterol[1][randint(0, 2)]
          elif int(age) > 64:
            healthy_food = lactose_acid_cholesterol[2][randint(0, 1)]
        elif celiac == "no":
          if int(age) < 18:
            healthy_food = lactose_acid_celiac_cholesterol[0][randint(0, 2)]
          elif int(age) > 17 and int(age) < 65:
            healthy_food = lactose_acid_celiac_cholesterol[1][randint(0, 1)]
          elif int(age) > 64:
            healthy_food = lactose_acid_celiac_cholesterol[2][randint(0, 1)]
    elif diabetes == "no":
      if cholesterol == "yes":
        if celiac == "yes":
          if int(age) < 18:
            healthy_food = lactose_acid_diabetes[0][randint(0, 2)]
          elif int(age) > 17 and int(age) < 65:
            healthy_food = lactose_acid_diabetes[1][randint(0, 3)]
          elif int(age) > 64:
            healthy_food = lactose_acid_diabetes[2][randint(0, 1)]
        elif celiac == "no":
          if int(age) < 18:
            healthy_food = lactose_acid_diabetes_celiac[0][randint(0, 2)]
          elif int(age) > 17 and int(age) < 65:
            healthy_food = lactose_acid_diabetes_celiac[1][randint(0, 2)]
          elif int(age) > 64:
            healthy_food = lactose_acid_diabetes_celiac[2][randint(0, 2)]
      elif cholesterol == "no":
        if celiac == "yes":
          if int(age) < 18:
            healthy_food = lactose_acid_diabetes_cholesterol[0][randint(0, 2)]
          elif int(age) > 17 and int(age) < 65:
            healthy_food = lactose_acid_diabetes_cholesterol[1][randint(0, 2)]
          elif int(age) > 64:
            healthy_food = lactose_acid_diabetes_cholesterol[2][randint(0, 3)]
        elif celiac == "no":
          if int(age) < 18:
            healthy_food = nothing[0][randint(0, 3)]
          elif int(age) > 17 and int(age) < 65:
            healthy_food = nothing[1][randint(0, 4)]
          elif int(age) > 64:
            healthy_food = nothing[2][randint(0, 2)]
print("\n" + greeting[randint(0, 4)] + healthy_food + ".")