def shipCombat(playerX,playerY,playerD,enemyX,enemyY,enemyD): #So this is just a test, pretty hard to explain but hopefully I can get it to work. 
  rowA = ["-","-","-","-","-"]
  rowB = ["-","-","-","-","-"]
  rowC = ["-","-","-","-","-"]
  rowD = ["-","-","-","-","-"]
  rowE = ["-","-","-","-","-"]
  if playerY == 1:
    del rowA[playerX-1]
    rowA.insert(playerX-1, "*")
  if playerY == 2:
    del rowB[playerX-1]
    rowB.insert(playerX-1, "*")
  if playerY == 3:
    del rowC[playerX-1]
    rowC.insert(playerX-1, "*")
  if playerY == 4:
    del rowD[playerX-1]
    rowD.insert(playerX-1, "*")
  if playerY == 5:
    del rowE[playerX-1]
    rowE.insert(playerX-1, "*")
  print(rowA[0], rowA[1], rowA[2], rowA[3], rowA[4])
  print(rowB[0], rowB[1], rowB[2], rowB[3], rowB[4])
  print(rowC[0], rowC[1], rowC[2], rowC[3], rowC[4])
  print(rowD[0], rowD[1], rowD[2], rowD[3], rowD[4])
  print(rowE[0], rowE[1], rowE[2], rowE[3], rowE[4])
  start()
def start():
  starting = input("What X position should the ship be in? (1-5)")
  starting2 = input("What Y position should the ship be in? (1-5)")
  starting = int(starting)
  starting2 = int(starting2)
  shipCombat(starting,starting2,1,1,1,1)
start()
#harder daddy
