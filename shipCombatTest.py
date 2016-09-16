def shipCombat(playerX,playerY,playerD,enemyX,enemyY,enemyD): #So this is just a test, pretty hard to explain but hopefully I can get it to work. 
  rowA = [0,0,0,0,0]
  rowB = [0,0,0,0,0]
  rowC = [0,0,0,0,0]
  rowD = [0,0,0,0,0]
  rowE = [0,0,0,0,0]
  if playerY == 3:
    rowA.remove(playerY-1)
    rowA.insert(playerY-1, >)
  print(rowA)
  print(rowB)
  print(rowC)
  print(rowD)
  print(rowE)
def start()
  starting = input("What position should the ship be in?")
  starting = int(starting)
  shipCombat(3,starting,1,1,1,1)
start()
