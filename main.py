#Orbic Legacy 2016 Luke Hamel 
#Connor, if you're seeing this, put your name on that top line and delete this. I'm adding a bunch of comments so you can figure this out.
print("Welcome to Orbic Legacy.") #Here's a print statement. I believe this was Echo in batch? The format is pretty easy, just print(). Remember that, unless it's a variable, it must have "" around it also. So a variable would look like print(string), but a certain line of text would read print("text"). You can also add them, I believe that's done like print("text"+string)
def tutorial(): #Definition for a function. The : is important, and notice how everything within the function is indented. That's not just for looks, it's required.
  response = input("Do you want to play the tutorial? (Type 'Yes' or 'No') ") #input, which we'll be using a lot for a text adventure. The parentheses are a prompt, so it would look like print("Response? ") Remember to leave a space so it looks better.
  if response == "yes" or response=="Yes" or response=="YES": #I checked, and it seems like there's no better way to do this. Anyway, if statement, remember == and because response is a string, we can only check it against other strings. So we need to check it with "yes", not yes.
    print("This is a text adventure, so you'll be typing quite a lot.")
    print("Will add more to this when there are actual game mechanics to describe.")
  elif response == "no" or response=="No" or response=="NO": #Else if, works pretty much the same as def and if. But, you know. Else if. 
    print("Type 'Tutorial' at any time if you need help.")
  else:
    tutorial()
location = your ship
print("Gazing out the ship window, you see Domuterum come into view.")

def main():
  print("You are currently at "+location+".")



