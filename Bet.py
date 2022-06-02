import time
import random

def roll():
    return (random.randint(1,6))

def display(x):
    if x == 1: return "CHERRY"
    if x == 2: return "BANANA"
    if x == 3: return "LEMON"
    if x == 4: return "BELL"
    if x == 5: return "PLUM"
    if x == 6: return "BAR"
    
    
totalOfBets = 0
totalOfWinnings = 0
money = 100
file = open("BetWin.txt","w")

while money>0:
    print()
    bet = int(input("Enter Bet: "))
    if bet>money:
        bet = money
    print("You bet", bet, "coins...Rolling!!")          
    money -=bet
    totalOfBets += bet
    x = roll()
    y = roll()
    z = roll()          
    print(display(x), end = "  ")
    time.sleep(1)
    print(display(y), end = "  ")
    time.sleep(1)          
    print(display(z))
    time.sleep(1)          
    print()
    if (x == y and y == z):
              print("**** JACKPOT ****")
              win = bet*10
              money += win
              totalOfWinnings += win
              file.write("Total Of Bets:"+str(totalOfBets)+"-Total Of Winnings:"+str(totalOfWinnings))
              print("You win" , win, "coins!!")
    elif (x == y and z == 6):
              print("****YOU WİN! ****")
              win = bet*5
              money += win
              totalOfWinnings += win
              file.write("Total Of Bets:",totalOfBets,"-Total Of Winnings:",totalOfWinnings)
              print("You win" , win, "coins!!")
    elif (x == 1):
              print("****CHERRY!!****")
              win = bet*2
              money += win
              totalOfWinnings += win
              file.write("Total Of Bets:",totalOfBets,"-Total Of Winnings:",totalOfWinnings)
              print("You win" , win, "coins!!")
    else:
        file.write("Total Of Bets:",totalOfBets,"-Total Of Winnings:",totalOfWinnings)
        print("Sorry you lose...")

print("You leave the casino with", money, "coins...")        
              
