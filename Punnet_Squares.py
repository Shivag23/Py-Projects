
def monohybrid(a1, a2):
  allele1 = a1.split()
  allele2 = a2.split()
  possible_genotypes = []
  for i in range(0, 2):
    for j in range(0,2):
      possible_genotypes.append(allele1[0][i] + allele2[0][j])
  
  return possible_genotypes

def drawBoard(board):
  print("        " + board[0] + "    " + board[1] + "      " + board[2] + "    " + board[3])
  print("     ----------------------------")
  print("     |      |      |      |      |")
  print("  " +board[4] + " | " + board[8]  + " | " + board[12]  + " | " + board[16]  + " | " + board[20]  + " |")
  print("     |      |      |      |      |")
  print("     ----------------------------")
  print("     |      |      |      |      |")
  print("  " +board[5] + " | " + board[9]  + " | " + board[13]  + " | " + board[17]  + " | " + board[21]  + " |")
  print("     |      |      |      |      |")
  print("     ----------------------------")
  print("     |      |      |      |      |")
  print("  " +board[6] + " | " + board[10]  + " | " + board[14]  + " | " + board[18]  + " | " + board[22]  + " |")
  print("     |      |      |      |      |")
  print("     ----------------------------")
  print("     |      |      |      |      |")
  print("  " +board[7] + " | " + board[11]  + " | " + board[15]  + " | " + board[19]  + " | " + board[23]  + " |")
  print("     |      |      |      |      |")
  print("     ----------------------------")
  
og1 = input("First Allele> ").split()
allele1 = (og1[0][0:2])
allele2 = (og1[0][2:4])

og2 = input("Second Allele> ").split()
allele3 = og2[0][0:2]
allele4 = og2[0][2:4]
possible_genotypes = []
set1 = monohybrid(allele1, allele2)
set2 = monohybrid(allele3, allele4)

items = []

for i in range(0, 4):
  for j in range(0,4):
    items.append(set1[i] + set2[j])

theBoard = []
for i in set1:
  theBoard.append(i)
for i in set2:
  theBoard.append(i)
for i in items:
  theBoard.append(i)
drawBoard(theBoard)
