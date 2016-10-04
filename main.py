#Orbic Legacy 2016 Luke Hamel & Connor Jordan
print("   __________________________________    ")
print("  /        \       \     \     /     `.  ")
print("  |        |       |     /    |    .-./             A Text Adventure   ")
print("  |   /\   |       /      \   |   |                        by   ")
print("  |   \/   |       \       \  |   I            Luke Hamel & Connor Jordan")
print("  |        |        \_     |  |    `-`\      ")
print("  \________/___/\____/_____/___\_____,i'_     ___       ____  ____    ___ ")
print("             \    ;   \     ___ /`   __  \   /    \    /     `.\   \/   /    ")
print("              |   |    |   [   \|   /  `_/  /      \  |    .-./  \     /    ") 
print("              |   |    |    `-_ |  |  ____ /    .   \ |   |       /   /  ") 
print("              |   \   /|    /`  |  | |__  |    __    \|   I      /   /     ") 
print("              |    `-` |   [___/|   ` `   |  .'  '.   \   `-`\_/   /      ")
print("              /________/_________\_____/\_|__\    /____\___________\       ")
print("   ")
def tutorial():
  response = input("Would you like to play the tutorial? ")
  if response.lower() == "yes":
    input("To advance past statements or events (.), simply press enter. For questions (?), type a response first.")
    input("For multiple choice questions, only type the corresponding number.")
    input("For 'yes or no' questions, type 'yes' or 'no'.")
    input("Will add more to this when there are actual game mechanics to describe.")
  elif response.lower() == "no": #Else if, works pretty much the same as def and if. But, you know. Else if. 
    print("Type 'Tutorial' at any time to view the tutorial, or 'Commands' for a command list.")
  else:
    tutorial()
tutorial() #The earlier code was just defining the tutorial, but now we're actually running it. If this were a one time thing we wouldn't bother with a function, but now the code can run any time it's called.
def initialize():
  import sys
  while True:
    global playerName
    playerName = input("What is the name of the main character? ")
    response = input("Is "+playerName+" the name you want?")
    print(response)
    if response.lower() == "yes":
      break
   
  global playerGender
  global playerPronoun
  global playerPosPronoun
  
  while True:
    response = input("Is the main character male (1) or female (2)?")
    if response.lower() == "1":
      playerGender = 0
      playerPronoun = "he"
      playerPosPronoun = "his"
      break
    elif response.lower() == "2":
      playerGender = 1
      playerPronoun = "she"
      playerPosPronoun = "her"
      break
  global location
  location = playerName+"'s ship" #The 'location' string will be pretty important. It's also used in main(), so all location names should look decent when it says "You are currently at [location]". That's why I called it "your ship" and not just "ship".
  global planet
  planet = "domaterum"
  global streetsFirstTimeCheck
  streetsFirstTimeCheck = True 
    
  
      
  input(""+playerName+"'s ship exits hyperspace as a planet begins to enter "+playerPosPronoun+" view.")
  input("Through the surrounding windows, a brilliant white horizon blossoms upward.")
  input("As "+playerPosPronoun+" ship flies ever closer to the planet, "+playerPronoun+" adjusts velocity for entry.")
  input(playerPronoun+"'s been travelling "+playerPosPronoun+" whole life, but now is the time to find a place to stay.")
  input("This will be "+playerPosPronoun+" first visit to Domaterum... hopefully, "+playerPronoun+"'ll be able to settle here.")
  input("The ship lands and docks just outside of a bustling city. "+playerName+" prepares to leave, unsure of what the future may hold.")

  
  
#Basic Functions
def core():
  if location == "[City name]'s streets" and streetsFirstTimeCheck == True:
    streetsFirstTime()
  response = input(playerName+" is currently at"+location+". What would you like to do? ")
  if response.lower() == "ship" and location == playerName+"'s ship":
    ship()
  elif response.lower() == "move to dock" and (location == playerName+"'s ship" or location == "[City name]'s streets"):
    move("docking bay 825")
  elif response.lower() == "move to ship" and location == "docking bay 825":
    move(playerName+"'s ship")
  elif response.lower() == "move to streets" and (location == "docking bay 825" or location == "the apartment lobby"):
    move("[City name]'s streets")
  elif response.lower() == "move to apartments" and (location == "[City name]'s streets" or location == playerName+"'s apartment"):
    move("the apartment lobby")
  elif response.lower() == "move to aparment" and location == "the apartment lobby":
    move(playerName+"'s apartment")
  
  elif response.lower() == "commands":
    commands()
  elif response.lower() == "use map":
    map()
  elif response.lower() == "quit":
    quit()
  else:
    core()    
def commands():
  print("Use 'quit' to exit the game.")
  print("Use 'move to [location]' to go somewhere.")
  print("Use 'map' to find locations to move to.")
  print("When at your ship, use 'ship' to access the ship computer. Or, use it to exit the ship computer.")
  print("When using your ship computer, use 'leave' to fly to another planet.")
  print("Or use 'info' to find information.")
  core()
def ship():
  print("<<Welcome to OorbOS v3.04. Ship #3348 - The Ravager>>")
  print("   ")
  response = input("What would you like to do, "+playerName+"?")
  if response.lower() == "info":
    info()
  elif response.lower() == "leave":
    leaveShip()
  elif response.lower() == "ship":
    core()
  elif response.lower() == "info":
    info()
  else:
    ship()
    

def move(locationToMove):
  global location
  location = locationToMove
  core()

def info():
  print("Information Library:")
  print("<<< Location Info >>>")
  print("<<<  Inventory   >>>")
  print("<<< Planet Info  >>>")
  if response.lower() == "location info":
    locationInfo()
  if response.lower() == "inventory":
    inventoryInfo()
  if response.lower() == "planet info":
    planetInfo()
def map():
  print("Here are the places you can move to:")
  if location == "docking bay 825":
    print("ship")
  elif location == playerName+"'s ship" or location == "[City name]'s streets": 
    print("dock")
  elif location == "docking bay 825" or location == "the apartment lobby":
    print("streets")
  elif location == "City name]'s streets" or location == playerName+"'s apartment":
    print("apartments")
  elif location == "the apartment lobby":
    print("apartment")
  core()
    
def inventory():
  print("You currently own:")
  print("Ship manual")
  print("Map")
  input()
  core()
  
def quit():
  print("Okay.")
def info():
  response = input("Get info on what?")
  if response == "planet":
    planetInfo()
  core()
   
def planetInfo():
  print("Planet: "+planet)
  if planet == "domaterum":
    print("This planet was discovered fairly recently, and has since had a major influx of Acrylite refugees after the destruction of their planet.")
    print("[INSERT ORBIC'S STORY PLOT HERE]") 
    print("Since then, the capital of [CITY NAME] has flourished as well as other settlements. Much of the planet remains in a more natural state.")
    print("Economists predict that Domaterum will become a Class-4 planet in 30 years or less.")
  core()
  
def locationInfo():
  response = input("Get info on which location?")
  if response.lower() == "ship":
    input("This ship is a GX-1600 medium transport shuttle, designed for long distance travel.")
    input("It contains 2 separate sleeping areas with a total of 8 beds.")
    input("While not created for combat, it features 2 PLO-4 laser cannons.")
  elif response.lower() == "dock":
    input("Dock 825 of [City name] is just one of many medium-sized docks in the area.")
    input("These docks are rented ahead of time, and most citizens find them to be affordable and accessible.")
    input("The fees were originally very high, but the City had voted to lower the price in exchange for slightly higher taxes.")
  else:
    input("Location not found.")
    info()

def inventoryInfo():
  print("Haha, let's do this later")

          
#Plot events
def streetsFirstTime():
  input("As you walk into the city, you are flooded with advertisements and crowds.")
  input("This planet was established pretty recently, but even since then immense progress has been made.")
  input("You notice the variety of citizens, a mess of colors and compositions.")
  input("Everyone here walks as if they're late, and you feel somewhat out of place.")
  input("Except, in the midst of all the movement, you notice one stationary person.")
  input("A slender man, with green, scaly skin and deeply sunken cheeks, stands in front of a building.")
  
  global streetsFirstTimeCheck
  streetsFirstTimeCheck = False
  core()
  
initialize()
core()
