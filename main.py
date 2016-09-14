#Orbic Legacy 2016 Luke Hamel 
#Connor, if you're seeing this, put your name on that top line and delete this. I'm adding a bunch of comments so you can figure this out.
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
location = "your ship" #The 'location' string will be pretty important. It's also used in main(), so all location names should look decent when it says "You are currently at [location]". That's why I called it "your ship" and not just "ship".
print("Gazing out the ship window, you see Domuterum come into view.") #We can change this name if we want to. It has latin roots with the word for "home" (domum) and the word for "past" (praeteritum).I figured a bit of foreshadowing was good.
input() 
print("As you approach the planet, you adjust your ship's velocity for entry.")
input()
print("This will be your first visit to Domuterum... and hopefully, you'll be able to settle here.")
input()
print("You've been travelling your whole life, but now is the time to find a place to stay.")
input()
print("Your ship lands and docks in a bustling city. You start making preparations to leave, unsure of what the future may hold.")
input()


def main():
    response = input("You are currently at "+location+". What would you like to do? ")
    if response.lower() == "move to ship":
        ship()
    elif response.lower() == "move to city":
        move("city")
    elif response.lower() == "commands":
        commands()
    else
        main()    
def commands():
  print("I hope I remember to do this later")
def ship():
  response = input("You access the ship computer. What would you like to do? ")
  if response.lower() == "information":
    information()
  elif response.lower() == "leave":
    leaveShip()
  elif response.lower() == "move":
    main()
  else:
    ship()
    
def move(locationToMove):
  location = locationToMove
  main()
main()
