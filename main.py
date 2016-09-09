#Orbic Legacy 2016 Luke Hamel 
#Connor, if you're seeing this, put your name on that top line and delete this. I'm adding a bunch of comments so you can figure this out.
print("Welcome to Orbic Legacy.") #Here's a print statement. I believe this was Echo in batch? The format is pretty easy, just print(). Remember that, unless it's a variable, it must have "" around it also. So a variable would look like print(string), but a certain line of text would read print("text"). You can also add them, I believe that's done like print("text"+string)
def tutorial(): #Definition for a function. The : is important, and notice how everything within the function is indented. That's not just for looks, it's required.
  response = input("Do you want to play the tutorial? (Type 'Yes' or 'No' and press enter) ") #input, which we'll be using a lot for a text adventure. The parentheses are a prompt, so it would look like print("Response? ") Remember to leave a space so it looks better.
  if response.lower() == "yes": #string.lower() makes a string lowercase, so the statement is now case insensitive. Anyway, if statement, remember == and because response is a string, we can only check it against other strings. So we need to check it with "yes", not yes.
    print("To advance text with a full stop (.), simply press enter. For text with a question mark (?), type a response first.")
    input()
    print("Will add more to this when there are actual game mechanics to describe.")
  elif response.lower() == "no": #Else if, works pretty much the same as def and if. But, you know. Else if. 
    print("Type 'Tutorial' at any time to view the tutorial, or 'Commands' for a command list.")
  else:
    tutorial()
location = your ship
print("Gazing out the ship window, you see Domuterum come into view.")
input()
print("As you approach the planet, you adjust your ship's velocity for entry.")
input()
print("This will be your first visit to Domuterum... and hopefully, you'll be able to settle here.")
input()
print("You've been travelling your whole life, but now is the time to find a place to stay.")
input()
print("Your ship lands and docks in a bustling city. You start making preparations to leave, unsure of what the future may hold.")
input()
main()

def main():
  response = input("You are currently at "+location+". What would you like to do?")
  if response.lower() == "ship":
    ship()

def ship():
  response = input("You access the ship computer. What would you like to do?")
  if response.lower() == "information":
    information()
  elif response.lower() == "leave":
    leaveShip()
  elif response.lower() == "exit":
    main()
  else:
    ship()
