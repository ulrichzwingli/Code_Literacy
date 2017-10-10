
score = 0
oddNumList=[]                      # declare an array
evenNumList=[]
firstHalfList=[]
secHalfList=[]
firstDozen=[]
secDozen=[]
thirdDozen=[]
row1=[]
row2=[]
row3=[]
black=[]
red=[]

def setBoard():
  print("in setboard")
  # score = 0
  # oddNumList=[]                      # declare an array
  # evenNumList=[]
  # firstHalfList=[]
  # secHalfList=[]
  # firstDozen=[]
  # secDozen=[]
  # thirdDozen=[]
  # row1=[]
  # row2=[]
  # row3=[]
  # black=[]
  # red=[]
  for num in range(1,36,2):          
    oddNumList.append(num)           #adding odd nums in array
  for num in range(2,36,2):
    evenNumList.append(num)          #adding even nums in array
  for num in range(1,18):          
    firstHalfList.append(num)       #adding firsthalf nums in array
  for num in range(19,36):          
    secHalfList.append(num)        #adding sechalf nums in array
  for num in range(1,36):
    if (num>=1 and num<=12):
      firstDozen.append(num)       #adding first dozen nums in array
    elif (num>=13 and num<=24):
      secDozen.append(num)          #adding second dozen nums in array
    else:
      thirdDozen.append(num)        #adding third dozen nums in array
  for num in range(1,36,3):  
    row1.append(num)                 #adding 1 st row nums in array
  for num in range(2,36,3):  
    row2.append(num)                #adding 2 nd row nums in array
  for num in range(3,36,3):  
    row3.append(num)                #adding 3 rd row nums in array
  for num in range(1,36):
    if(num>=1 and num<=10):
      if(num % 2 is 0):
        black.append(num)
      else:
        red.append(num)
    elif(num>=11 and num<=18): 
      if(num % 2 is 0):
        red.append(num)
      else:
        black.append(num)
    elif(num>=19 and num<=28):
      if(num % 2 is 0):
        black.append(num)
      else:
        red.append(num)
    else:  
      if(num % 2 is 0):
        red.append(num)
      else:
        black.append(num)
  return      
  

                   #finished adding black and red arrays

# time to roll the dice 

def printGraphic(name):
  if (name == "GameTitle"):
    print('    ___     __     __     _                      _          ______              _              ')
    print('   /   |   / /_   / /_   (_)____   ____ _ _   __( )_____   / ____/____ _ _____ (_)____   ____  ')
    print('  / /| |  / __ \ / __ \ / // __ \ / __ `/| | / /|// ___/  / /    / __ `// ___// // __ \ / __ \ ')
    print(' / ___ | / /_/ // / / // // / / // /_/ / | |/ /  (__  )  / /___ / /_/ /(__  )/ // / / // /_/ / ')
    print('/_/  |_|/_.___//_/ /_//_//_/ /_/ \__,_/  |___/  /____/   \____/ \__,_//____//_//_/ /_/ \____/  ')
    
    
                                                                                              

    
  if (name == "Rollet"):
     print('      -----------------------------------------------------------------   ')
     print('     |    |    |    |    |    |    |    |    |    |    |    |    |    |   ') 
     print('     | 3  | 6  | 9  | 12 | 15 | 18 | 21 | 24 | 27 | 30 | 33 | 36 | R1 |   ') 
     print('     |    |    |    |    |    |    |    |    |    |    |    |    |    |   ') 
     print('     |-----------------------------------------------------------------   ')
     print('     |    |    |    |    |    |    |    |    |    |    |    |    |    |   ') 
     print('     | 2  | 5  | 8  | 11 | 14 | 17 | 20 | 23 | 26 | 29 | 32 | 35 | R2 |   ')  
     print('     |    |    |    |    |    |    |    |    |    |    |    |    |    |   ') 
     print('     |-----------------------------------------------------------------   ') 
     print('     |    |    |    |    |    |    |    |    |    |    |    |    |    |   ') 
     print('     | 1  | 4  | 7  | 10 | 13 | 16 | 19 | 22 | 25 | 28 | 31 | 34 | R3 |   ') 
     print('     |    |    |    |    |    |    |    |    |    |    |    |    |    |   ') 
     print('     |-----------------------------------------------------------------   ') 
     print('     |   1 st Dozen      |  2 nd Dozen       |   3 rd Dozen      |        ')
     print('     |------------------------------------------------------------        ')
     print('     |    FH   | Even    |    Red  |  Black  |  Odd    |  LH     |        ') 
     print('      ------------------------------------------------------------        ')
     
    
    
    
    

def rollDice(playerBet, denomination):
  import random
  dice = random.randint(1,36)
  if(playerBet=="21"):    # secretly fixed 21 as the winning number to see the graphic during demo
    print(' WOAH !!!  You just won a jackpot of 36 times your money !!!')
    print('                                                            ')
    print('                                                            ')
    print('                                                            ')
    print('                              oooo$$$$$$$$$$$$oooo                          ')
    print('                      oo$$$$$$$$$$$$$$$$$$$$$$$$o                            ')
    print('                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$      ')
    print('   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$     ')
    print('oo $ $ "$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$       ')
    print('"$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$        ')
    print('  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$        ')
    print('  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  """$$$          ')
    print('   "$$$""""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$         ')
    print('    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$o       ')
    print('   o$$"   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o      ')
    print('   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" "$$$$$$ooooo$$$$o    ')
    print('  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$   ')
    print('  $$$$$$$$"$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$""""""""         ')
    print(' """"       $$$$    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$"      o$$$                  ')
    print('            "$$$o     """$$$$$$$$$$$$$$$$$$"$$"         $$$                  ')
    print('              $$$o          "$$""$$$$$$""""           o$$$                   ')
    print('               $$$$o                                o$$$"                    ')
    print('                "$$$$o      o$$$$$$o"$$$$o        o$$$$                       ')
    print('                  "$$$$$oo     ""$$$$o$$$$$o   o$$$$""                        ')
    print('                     ""$$$$$oooo  "$$$o$$$$$$$$$"""                          ')
    print('                        ""$$$$$$$oo $$$$$$$$$$                                ')
    print('                                """"$$$$$$$$$$$                               ')
    print('                                    $$$$$$$$$$$$                             ')
    print('                                     $$$$$$$$$$"                             ')
    print('                                      "$$$""""                               ')
    print('                                                            ')
    print('                                                            ')
    print('                                                            ')
    win = int(denomination) * 36
    score += win
    print(' Your prize money is' + score)
    gameNarration()
  elif (playerBet is "ODD"):
    if(dice in oddNumList):
      win = int(denomination) * 2
      score += win
      print(' Your prize money is' + score)
      gameNarration()
      
    
  elif (playerBet is "EVEN"):
    if(dice in evenNumList):
      win = int(denomination) * 2
      score += win
      print(' Your prize money is' + score)
      gameNarration()
      
    
  elif (playerBet is "FH"):
    if(dice in firstHalfList):
      win = int(denomination) * 2
      score += win
      print(' Your prize money is' + score)
      gameNarration()
      
     
  elif (playerBet is "SH"):
    if(dice in secHalfList):
      win = int(denomination) * 2
      score += win
      print(' Your prize money is' + score)
      gameNarration()
      
  elif (playerBet is "RED"):
    if(dice in red):
      win = int(denomination) * 2
      score += win
      print(' Your prize money is' + score)
      gameNarration()
      
    
  elif (playerBet is "BLACK"):
    if(dice in black):
      win = int(denomination) * 2
      score += win
      print(' Your prize money is' + score)
      gameNarration()
      
    
  elif (playerBet is "DOZEN1"):
    if(dice in firstDozen):
      win = int(denomination) * 3
      score += win
      print(' Your prize money is' + score)
      gameNarration()
      
    
  elif (playerBet is "DOZEN2"):
    if(dice in secDozen):
      win = int(denomination) * 3
      score += win
      print(' Your prize money is' + score)
      gameNarration()
      
    
  elif (playerBet is "DOZEN3"):
    if(dice in thirdDozen):
      win = int(denomination) * 3
      score += win
      print(' Your prize money is' + score)
      gameNarration()
      
    
  elif (playerBet is "ROW1"):
    if(dice in row1):
      win = int(denomination) * 3
      score += win
      print(' Your prize money is' + score)
      gameNarration()
      
  elif (playerBet is "ROW2"):
    if(dice in row2):
      win = int(denomination) * 3
      score += win
      print(' Your prize money is' + score)
      gameNarration()
      
  elif (playerBet is "ROW3"):
    if(dice in row3):
      win = int(denomination) * 3
      score += win
      print(' Your prize money is' + score)
      gameNarration()      
      
  else:
    print('The value on the dice is : '+ dice )
    print(' I am sorry !!! You lost your bet !!!')
    gameNarration()
    
    

    
def gameNarration():
  print(' Do you want to continue playing?')
  playerChoice = input("Input Yes/No")
  if (playerChoice=="Yes"):
    denomination = input("Enter How much money you want to bet in numbers between 1-100")
    print(' Enter amongst the following bet choices :')
    print(' Option 1 : Any Number between 1 to 36 for a chance to win 36 times your money')
    print(' Option 2 : For betting on Odd numbers and 2 times the money, input: ODD ')
    print(' Option 3 : For betting on Even numbers and 2 times the money, input: EVEN ')
    print(' Option 4 : For betting on First Half numbers and 2 times the money, input: FH ')
    print(' Option 5 : For betting on Seconf Half numbers and 2 times the money, input: SH ')
    print(' Option 6 : For betting on Red Numbers and 2 times the money, input: RED ')
    print(' Option 7 : For betting on Black Numbers and 2 times the money, input: BLACK ')
    print(' Option 8 : For betting on 1 st Dozen and 3 times the money, input: DOZEN1 ')
    print(' Option 9 : For betting on 2 nd Dozen and 3 times the money, input: DOZEN2')
    print(' Option 10 : For betting on 3 rd Dozen and 3 times the money, input: DOZEN3 ')
    print(' Option 11 : For betting on 1 st Row and 3 times the money, input: ROW1 ')
    print(' Option 12 : For betting on 2 nd Row and 3 times the money, input: ROW2 ')
    print(' Option 13 : For betting on 3 rd Row and 3 times the money, input: ROW3 ')
    playerBet = input(">")
    rollDice(playerBet, denomination)
  else:
    print(' :(   :(   :(   I wish you had played a bit more with us ! Anyways , Good bye')
    print(' Your winning amount is ' + score)
    return
  

  
  

     
                                                                                         
def main():
  print("in main")
  import random
  import sys
  setBoard()
  printGraphic("GameTitle")
  P1name = input("Please Enter Your name :")
  print(' Lets play the game of Roullet')
  gameNarration()
  setBoard()
  
main()                                                                                                                                        
 
    
  
         