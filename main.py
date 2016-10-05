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
  global apartmentsFirstTimeCheck
  apartmentsFirstTimeCheck = True
    
  
      
  input(""+playerName+"'s ship exits hyperspace as a planet begins to enter "+playerPosPronoun+" view.")
  input("Through the surrounding windows, a brilliant white horizon blossoms upward.")
  input("As "+playerPosPronoun+" ship flies ever closer to the planet, "+playerPronoun+" adjusts velocity for entry.")
  input(playerPronoun+"'s been travelling "+playerPosPronoun+" whole life, but now is the time to find a place to stay.")
  input("This will be "+playerPosPronoun+" first visit to Domaterum... hopefully, "+playerPronoun+"'ll be able to settle here.")
  input("The ship lands and docks just outside of a bustling city. "+playerName+" prepares to leave, unsure of what the future may hold.")
  print()

  
  
#Basic Functions
def core():
  if location == "[City name]'s streets" and streetsFirstTimeCheck == True:
    streetsFirstTime()
  if location == "the apartment lobby" and apartmentsFirstTimeCheck == True:
    apartmentsFirstTime()
  response = input(playerName+" is currently at "+location+". What would you like to do? ")
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
  elif response.lower() == "move to apartment" and location == "the apartment lobby":
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
  print()
  print("Submit 'quit' to exit the game.")
  print("Submit 'move to [location]' to go somewhere.")
  print("Submit 'use map' to find locations to move to.")
  print("When at your ship, submit 'ship' to access the ship computer. Or, submit it to exit the ship computer.")
  print("When using your ship computer, submit 'leave' to fly to another planet.")
  print("Or submit 'info' to find information.")
  print()
  core()
def ship():
  print()
  print("<<Welcome to OorbOS v3.04. Ship #3348 - The Ravager>>")
  print("   ")
  response = input("What would you like to do, "+playerName+"?")
  if response.lower() == "info":
    info()
  elif response.lower() == "leave":
    leaveShip()
  elif response.lower() == "ship":
    core()
  else:
    ship()
    

def move(locationToMove):
  global location
  location = locationToMove
  core()

def info():
  print()
  print("Information Library:")
  print("<<< Locations >>>")
  print("<<< Inventory >>>")
  print("<<<  Planets  >>>")
  response = input("What should I get info on?")
  if response.lower() == "locations":
    locationInfo()
  if response.lower() == "inventory":
    inventoryInfo()
  if response.lower() == "planets":
    planetInfo()
  print()
  core()
  
def map():
  input("Here are the places you can move to:")
  if location == "docking bay 825":
    input("ship")
  if location == playerName+"'s ship" or location == "[City name]'s streets": 
    input("dock")
  if location == "docking bay 825" or location == "the apartment lobby":
    input("streets")
  if location == "[City name]'s streets" or location == playerName+"'s apartment":
    input("apartments")
  if location == "the apartment lobby":
    input("apartment")
  print()
  core()
    
def inventory():
  print()
  input("You currently own:")
  input("Map")
  print()
  core()
  
def quit():
  print("Okay.")
   
def planetInfo():
  print()
  print("Planet: "+planet)
  if planet == "domaterum":
    print("This planet was discovered fairly recently, and has since had a major influx of Acrylite refugees after the destruction of their planet.")
    print("[INSERT ORBIC'S STORY PLOT HERE]") 
    print("Since then, the capital of [CITY NAME] has flourished as well as other settlements. Much of the planet remains in a more natural state.")
    print("Economists predict that Domaterum will become a Class-4 planet in 30 years or less.")
  print()
  core()
  
def locationInfo():
  print()
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
  print()

def inventoryInfo():
  print("Haha, let's do this later")

          
#Plot events
def streetsFirstTime():
  print()
  input("As "+playerName+" walks into the city, "+playerPronoun+" is flooded with advertisements and crowds.")
  input("This planet was established pretty recently, but even since then immense progress has been made.")
  input(playerPronoun+" notices the variety of citizens, a mess of colors and compositions.")
  input("Everyone here walks as if they're late, and "+playerName+" feels somewhat out of place.")
  input("Except, in the midst of all the movement, "+playerPronoun+" notices one stationary person.")
  input("A slender man, with green, scaly skin and deeply sunken cheeks, stands in front of a building.")
  input("The man notices "+playerName+" and walks away, but not before initiating a call on his communicator.")
  input(playerName+" remembers that "+playerPronoun+" needs to rent an apartment and continues.") 
  print()
  global streetsFirstTimeCheck
  streetsFirstTimeCheck = False
  core()
  
def apartmentsFirstTime():
  print()
  input(playerName+" enters the apartment building "+playerPronoun+" had previously read about.")
  input("Behind the counter sits a friendly-looking, vaguely humanoid young woman.")
  input("Should "+playerName+"..."
  print("Politely ask to access the apartment "+playerPronoun+" rented. (1)")
  print("Demand the apartment in a vaguely menacing threat. (2)")
  print("Attempt to seduce the young woman with faked self-confidence. (3)")
  response = input("? ")
  if response.lower() == "1":
    input("The woman smiles and 
        
  
initialize()
core()
