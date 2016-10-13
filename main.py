#Orbic Legacy 2016 Luke Hamel & Connor Jordan
print("   __________________________________    ")
print("  /        \       \     \     /     `.  ")
print("  |        |       |     /    |    .-./             A Text Adventure   ")
print("  |   /\   |       /      \   |   |                        by   ")
print("  |   \/   |       \       \  |   I            Luke Hamel & Connor Jordan")
print("  |        |        \_     |  |    `-`\      ")
print("  \________/___/\____/_____/___\_____,i'_     ___       ____  ____    ___ ")
print("             \    ;   \     ___ /`   __  \   /    \    /     `.\   \/   /    ")
print("              |   |    |   [   \|   /  `_/  /      \  |    .-./ \      /    ") 
print("              |   |    |    `-_ |  |  ____ /    .   \ |   |      /    /  ") 
print("              |   \   /|    /`  |  | |__  |    __    \|   I     /   /     ") 
print("              |    `-` |   [___/|   ` `   |  .'  '.   \   `-`\_/   /      ")
print("              /________/_________\_____/\_|__\    /____\___________\       ")
print("   ")
def tutorial():
  response = input("Would you like to play the tutorial? ")
  if response.lower() == "yes" or response.lower() == "y":
    input("To advance past statements or events (.), simply press enter. For questions (?), type a response first.")
    input("For multiple choice questions, only type the corresponding number.")
    input("For 'yes or no' questions, type 'yes' or 'no'.")
    input("Will add more to this when there are actual game mechanics to describe.")
  elif response.lower() == "no" or response.lower() == "n": #Else if, works pretty much the same as def and if. But, you know. Else if. 
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
    if response.lower() == "yes" or response.lower() == "y":
      break
   
  global playerGender
  global playerPronoun
  global playerPosPronoun
  global playerObjectPronoun
  global playerCapitalPronoun
  
  while True:
    response = input("Is the main character male (1) or female (2)?")
    if response.lower() == "1":
      playerGender = 0
      playerPronoun = "he"
      playerPosPronoun = "his"
      playerObjectPronoun = "him"
      playerCapitalPronoun = "He"
      break
    elif response.lower() == "2":
      playerGender = 1
      playerPronoun = "she"
      playerPosPronoun = "her"
      playerObjectPronoun = "her"
      playerCapitalPronoun = "She"
      break
  global location
  location = playerName+"'s ship" #The 'location' string will be pretty important. It's also used in main(), so all location names should look decent when it says "You are currently at [location]". That's why I called it "your ship" and not just "ship".
  global planet
  planet = "domaterum"
  global streetsFirstTimeCheck
  streetsFirstTimeCheck = True
  global apartmentsFirstTimeCheck
  apartmentsFirstTimeCheck = True
  global dockFirstTimeCheck
  dockFirstTimeCheck = True
  global apartmentFirstTimeCheck
  apartmentFirstTimeCheck = True
  global streetsHoboEncounterCheck 
  streetsHoboEncounterCheck = False
  global simCenterFirstTimeCheck
  simCenterFirstTimeCheck = True
  global simCenterAttackCheck
  simCenterAttackCheck = False
    
  
      
  input(""+playerName+"'s ship exits hyperspace as a planet begins to enter "+playerPosPronoun+" view.")
  input("Through the surrounding windows, a brilliant white horizon blossoms upward.")
  input("As "+playerPosPronoun+" ship flies ever closer to the planet, "+playerPronoun+" adjusts velocity for entry.")
  input(playerCapitalPronoun+"'s been travelling "+playerPosPronoun+" whole life, but now is the time to find a place to stay.")
  input("This will be "+playerPosPronoun+" first visit to Domaterum... hopefully, "+playerPronoun+"'ll be able to settle here.")
  input("The ship lands and docks just outside of a bustling city. "+playerName+" prepares to leave, unsure of what the future may hold.")
  print()

  
  
#Basic Functions
def core():
  if location == "docking bay 825" and dockFirstTimeCheck == True:
    dockFirstTime()
  if location == "[City name]'s streets" and streetsFirstTimeCheck == True:
    streetsFirstTime()
  if location == "the apartment lobby" and apartmentsFirstTimeCheck == True:
    apartmentsFirstTime()
  if location == playerName+"'s apartment" and apartmentFirstTimeCheck == True:
  	apartmentFirstTime()
  if location == "[City name]'s streets" and streetsHoboEncounterCheck == True:
    streetsHoboEncounter()
  response = input(playerName+" is currently at "+location+". What would you like to do? ")
  if response.lower() == "ship" and location == playerName+"'s ship":
    ship()
  elif response.lower() == "move to dock" and (location == playerName+"'s ship" or location == "[City name]'s streets"):
    move("docking bay 825")
  elif response.lower() == "move to ship" and location == "docking bay 825":
    move(playerName+"'s ship")
  elif response.lower() == "move to streets" and (location == "docking bay 825" or location == "the apartment lobby" or location == "High Thrills Simulation Center"):
    move("[City name]'s streets")
  elif response.lower() == "move to apartments" and (location == "[City name]'s streets" or location == playerName+"'s apartment"):
    move("the apartment lobby")
  elif response.lower() == "move to apartment" and location == "the apartment lobby":
    move(playerName+"'s apartment")
  elif response.lower() == "move to simulation center" and location == "[City name]'s streets":
    move("High Thrills Simulation Center")
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
    input("Ship")
  if location == playerName+"'s ship" or location == "[City name]'s streets": 
    input("Dock")
  if location == "docking bay 825" or location == "the apartment lobby" or location == "High Thrills Simulation Center": 
    input("Streets")
  if location == "[City name]'s streets" or location == playerName+"'s apartment":
    input("Apartments")
  if location == "the apartment lobby":
    input("Apartment")
  if location == "[City name]'s streets":
    input("Simulation center")
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
  input(playerCapitalPronoun+" notices the variety of citizens, a mess of colors and compositions.")
  input("Everyone here walks as if they're late, and "+playerName+" feels somewhat out of place.")
  input("Except, in the midst of all the movement, "+playerPronoun+" notices one stationary person.")
  input("A thin man, with green, scaly skin and deeply sunken cheeks, stands in front of a building.")
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
  input("Should "+playerName+"...")
  print("(1) Politely ask to access the apartment "+playerPronoun+" rented.")
  print("(2) Demand the apartment in a somewhat menacing threat.")
  print("(3) Attempt to seduce the young woman with faked self-confidence.")
  global apartmentWomanRelation
  global apartmentsFirstTimeCheck
  while True:
    response = input("? ")
    if response.lower() == "1":
      input("The woman smiles and hands "+playerName+" the key to the apartment.")
      input("She tells "+playerObjectPronoun+" the room number, and demonstrates how the key should be scanned.")
      apartmentWomanRelation = 1
      apartmentsFirstTimeCheck = False
      break
    if response.lower() == "2":
      input("The woman glares and begrudgingly gives "+playerName+" the key to the apartment.")
      input("She tells "+playerObjectPronoun+" where to find the room number.")
      apartmentWomanRelation = -1
      apartmentsFirstTimeCheck = False
      break
    if response.lower() == "3":
      input("She looks concerned.")
      input("She gives "+playerName+" the key and quietly goes back to work.")
      apartmentWomanRelation = 0
      apartmentsFirstTimeCheck = False
      break
  
def dockFirstTime():
  input(playerName+" steps onto the docking bay and surveys the area.")
  input("The bays are stacked on top of each other, creating a huge wall with a grid of holes.")
  input(playerName+" remembers the apartment that "+playerPronoun+" rented, and decides to find it.")
  global dockFirstTimeCheck
  dockFirstTimeCheck = False
        
def apartmentFirstTime():
  input(playerName+" enters "+playerPosPronoun+" apartment.")
  input("With nothing to do, "+playerPronoun+" decides to relax a bit and watch a holoprojection.")
  while True:
    input("Should "+playerPronoun+" watch...")
    print("(1) URC Galactic News")
    print("(2) Pimp my Ship")
    print("(3) Escape from the Elation Station Part II")
    response = input("? ")
    if response == "1":
      input("'...and the President of the Galactic Allegience has recently announced his departure.'")
      input("'Let's go right to the President and see what he has to say:'")
      input("'After the incident on the asteroid of Tariss, I have to announce my resignation.'")
      input("'I trust that the citizens of our galaxy will...'")
      input(playerName+" thinks that politics today are insane.")
      break
    if response == "2":
      input("'...and this TR-046 freighter has just been pimped!'")
      input("'We decided to replace the old, flickering lights with adaptive lights directly connected to the AI.'")
      input("'And how could you haul in comfort without a pool? We installed the...'")
      input(playerName+" thinks that shows today are trash.")
      break
    if response == "3":
      input("'I... I can't run fast enough!'")
      input("'They're coming after me! What's happening to me?'")
      input("'Why am I enjoying this?'")
      input(playerName+" thinks that movies today are terrible.")
      break
  input("After a few hours of holoprojections, "+playerPronoun+" decides to explore the city a bit.")
  input("There's no simulation chamber in "+playerPosPronoun+" apartment, but there may be a simulation center in the city.")
  input(playerCapitalPronoun+" turns off the holoprojector and prepares to leave.")
  global apartmentFirstTimeCheck
  apartmentFirstTimeCheck = False
  global streetsHoboEncounterCheck
  streetsHoboEncounterCheck = True
  core()

def streetsHoboEncounter():
  input("As "+playerName+" walks through the streets, "+playerPronoun+" sees a homeless man in an alley.")
  input("He screams at "+playerName+" and tries to talk to them.")
  input("'Don't trust [Company name]! They're brainwashing people! I'm not crazy, I swear!'")
  while True:
    input("Should "+playerName+"...")
    print("(1) Talk to the man")
    print("(2) Continue walking at the same pace")
    print("(3) Walk away quickly")
    response = input("? ")
    if response == "1":
      input(playerName+" approaches the man and he continues talking.")
      input("'Yeah, they're taking people from the streets and brainwashing them! Or doing something to them...")
      input("'I've seen it myself! If I were you, I would leave this planet.'")
      input(playerName+" considers the man's words, but can't afford to leave the planet.")
      input(playerCapitalPronoun+" continues on "+playerPosPronoun+" way.")
      break
    if response == "2":
      input(playerName+" keeps walking, trying to ignore the man.")
      input("'Hey! Don't ignore me! Listen or you'll regret it!")
      input(playerCapitalPronoun+" continues on "+playerPosPronoun+" way.")
      break
    if response == "3":
      input(playerName+" walks faster, and hears the man yelling.")
      input(playerCapitalPronoun+" doesn't hear what the man is saying, and doesn't want to engage.")
      input(playerCapitalPronoun+" decides to continue to the simulation center.")
      break
  global streetsHoboEncounterCheck
  streetsHoboEncounterCheck = False
  global simCenterAttackCheck
  simCenterAttackCheck = True
  global simCenterFirstTimeCheck
  simCenterFirstTimeCheck = False
  core()
  
def simCenterFirstTime:
  input(playerName+" enters a Simulation Center.")
  input("There's not many people here, but these usually get popular at night.")
  input("Right now "+playerPronoun+" wants to find "+playerPosPronoun+" apartment, but "+playerPronoun+" might come back later.")
  global simCenterFirstTime
  simCenterFirstTime = False
  core()

def simCenterAttack:
  input(playerName+" enters the simulation center, ready to experience whatever it has to offer.")
  input(playerPronoun+" approaches a simulation chamber, pays for it, and stumbles inside.")
  input("A friendly voice booms in from all sides:")
  input("'Welcome to High Thrills Simulation Center!'")
  input("'We have a number of high quality simulations here, and we hope you enjoy your stay.")
  input("'After 1 hour, the simulation will end and you should exit the chamber or pay for another round.'")
  input("'Please approach the monitor and select your preferred experience.'")
  input("Should "+playerName+" choose...")
  print("(1) Action-adventure simulation")
  print("(2) Historical simulation")
  print("(3) Happy fun time simulation")
  input("? ")
  input("While "+playerName+" struggles to decide, time seems to halt.")
  input("As if from nowhere, the ground trembles and part of the wall collapses as a blinding red light appears.")
  input("Millions of objects flicker in front of "+playerName+" as the projectors are destroyed.")
  input(playerPronoun+" falls to the ground and tries to take cover from the falling rubble.")
  input("Looking up, "+playerPronoun" notices bright lights and the unmistakable whine of a ship flying overhead.")
  While True:
    input("Should "+playerName+"...")
    print("(1) Continue to hide in the Sim Center")
    print("(2) Run to "+playerPosPronoun+" ship and pursue the attackers")
    print("(3) Flee to "+playerPosPronoun+" apartment")
    response = input("? ")
    if response == "1":
      input(playerName+" stays on the ground, waiting.")
      input("After what feels like hours, "+playerPronoun+" decides that it must be safe.")
      input(playerPronoun+" gets up and looks around. Most of the building was destroyed by what must have been laser fire.")
      input(playerName+" is not injured, and wants to help.")
      input(playerPronoun+" decide to investigate the area.")
      break
    if response == "2":
      input(playerName+" rushes out of the building and into their docking bay.")
      input("The Ravager clicks to life, and "+playerPronoun+" circles around to above the Sim Center.")
      input("Thick smoke billows from the Center, but the ship that attacked is nowhere in sight".)
      input("With disappointment, "+playerName+" lands and ponders what to do next.")
      input(playerPronoun+" decides to investigate the Center.")
      global location
      location == playerName+"'s ship"
      break
    if response == "3":
      input(playerName+" escapes to the building and runs through the streets.")
      input(playerPronoun+" hides for a few hours, watching the proceedings from a distance.")
      input("Eventually, "+playerPronoun+" resolves to investigate the area.")
      global location
      location == playerName+"'s apartment"
      break
  core()
    
  
initialize()
core()
