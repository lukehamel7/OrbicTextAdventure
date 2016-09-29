try: 
  print("Test: Accented character ǹ")
except: 
  print("Accented character does not work")
try: 
  print("Test: Uncommon character 🞑")
except:
  print("Uncommon character does not work")
try: 
  print("Test: Uncommon character using code \u0394")
except:
  print("Well that didn't work.")
