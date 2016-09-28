#Orbic Legacy 2016 Luke Hamel & Connor Jordan
print("Welcome to Orbic Legacy.") #Here's a print statement. I believe this was Echo in batch? The format is pretty easy, just print(). Remember that, unless it's a variable, it must have "" around it also. So a variable would look like print(string), but a certain line of text would read print("text"). You can also add them, I believe that's done like print("text"+string)
def tutorial(): #Definition for a function. The : is important, and notice how everything within the function is indented. That's not just for looks, it's required.
  response = input("Do you want to play the tutorial? ") #input, which we'll be using a lot for a text adventure. The parentheses are a prompt, so it would look like print("Response? ") Remember to leave a space so it looks better.
  if response.lower() == "yes": #string.lower() makes a string lowercase, so the statement is now case insensitive. Anyway, if statement, remember == and because response is a string, we can only check it against other strings. So we need to check it with "yes", not yes.
    print("To advance text with a full stop (.), simply press enter. For text with a question mark (?), type a response first.")
    input() #This doesn't actually save to anything, it's just to force the player to press enter. Otherwise all the text would display at once.
    print("Will add more to this when there are actual game mechanics to describe.")
  elif response.lower() == "no": #Else if, works pretty much the same as def and if. But, you know. Else if. 
    print("Type 'Tutorial' at any time to view the tutorial, or 'Commands' for a command list.")
  else:
    tutorial()
tutorial() #The earlier code was just defining the tutorial, but now we're actually running it. If this were a one time thing we wouldn't bother with a function, but now the code can run any time it's called.
def initialize():
    import sys
    global location
    location = "your ship" #The 'location' string will be pretty important. It's also used in main(), so all location names should look decent when it says "You are currently at [location]". That's why I called it "your ship" and not just "ship".
    global planet
    planet = "domaterum"
    global cityFirstTimeCheck
    cityFirstTimeCheck = True 
    input("Gazing out the ship window, you see Domaterum come into view.") #We can change this name if we want to. It has latin roots with the word for "home" (domum) and the word for "past" (praeteritum).I figured a bit of foreshadowing was good.
    input("As you approach the planet, you adjust your ship's velocity for entry.")
    input("This will be your first visit to Domaterum... and hopefully, you'll be able to settle here.")
    input("You've been travelling your whole life, but now is the time to find a place to stay.")
    input("Your ship lands and docks just outside of a bustling city. You start making preparations to leave, unsure of what the future may hold.")

#Basic Functions
def core():
    if location == "the city" and cityFirstTimeCheck == True:
      cityFirstTime()
    response = input("You are currently at "+location+". What would you like to do? ")
    if response.lower() == "ship":
        ship()
    elif response.lower() == "move to city" and location == "your ship":
        move("the city")
    elif response.lower() == "move to ship" and location == "the city":
        move("your ship")
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
  print("Or use 'info' to find information")
  core()
def ship():
  response = input("You access the ship computer. What would you like to do? ")
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
    print (locationToMove)
    print (location)
    core()
    
def map():
    print("Here are the places you can move to:")
    if location == "your ship": 
        print("city")
    if location == "the city":
        print("ship")
    core()
    
def inventory():
  print("You currently own:")
  print("Ship manual")
  print("Map") 
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
    
#Plot events
def cityFirstTime():
  input("As you walk into the city, you are flooded with advertisements and crowds.")
  input("This planet was established pretty recently, but since then immense progress has been made.")
  input("You notice the various different citizens, a mess of colors and body compositions.")
  input("Everyone here walks as if they're late, and you feel somewhat out of place.")
  input("Except, in the midst of all the movement, you notice one stationary person.")
  input("A slender man, with green, scaly skin and deeply sunken cheeks, stands in front of a building.")
  
  global cityFirstTimeCheck
  cityFirstTimeCheck = False
  core()
  
initialize()
core()
