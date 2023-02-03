import random
import os

Logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
score = 0

def ask(use):
    u1 = input("            Press 'y' if you want to draw another card:- ")
    while u1 =='':
        u1 = input("            ")
    if u1[0] == 'y':
        use.append(allot())
        return [use, True]
    else:
        return [use, False]
    
def check1(user,computer):
    if (sum(user,0) == 21):
        win(user,computer)
    
    if (sum(user)>21):
        loose(user,computer)
        
def check(user,computer):
    while sum(computer) < 17:
        computer.append(allot())
        
    if (sum(user,0) == 21):
        win(user,computer)
    
    if (sum(user)>21):
        loose(user,computer)
        
    if (sum(computer,0) == 21):
        loose(user,computer)
    
    if (sum(computer)>21):
        win(user,computer)
    
    if(sum(user) == sum(computer)):
        draw(user,computer)
    
    if(sum(user) < sum(computer)):
        loose(user,computer)
    if (sum(user)>sum(computer)):
        win(user,computer)
    return computer
    

def win(user,computer):
    print(f"            Your Cards were {user}, score => {sum(user)} and computer's were {computer} score => {sum(computer)}. ")
    print("          you have won")
    sub()
    
def draw(user,computer):
    print(f"            Your Cards were {user}, score => {sum(user)} and computer's were {computer} score => {sum(computer)}. ")
    print("          DRAW")
    sub()
    
def loose(user,computer):
    print(f"            Your Cards were {user}, score => {sum(user)} and computer's were {computer} score => {sum(computer)}. ")
    print("          you have lost to computer")
    sub()
    
    
def allot() -> int:
    """"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    ch = random.choice(cards)
    return ch
    
def main():
    """"""
    print(Logo)
    user = []
    computer = []
    # user allotment
    user.append(allot())
    user.append(allot())
    # computer allotment
    computer.append(allot())
    computer.append(allot())
    # showing user's cards
    print(f"            Your cards are {user}")
    # checking if user has won or lost
    check1(user,computer)
    # showing computer's card
    print(f"            One of computer's card is {computer[0]}")
    # asking user if he wants to choose one more or not
    while ask(user)[1]:
        check1(user,computer)
        print(f"            Your cards are {user}")
    
    check(user,computer)
    
def sub():
    init = input("          Do you want to play the the game of BlackJack??  \n          'y' or 'n' :- ")
    while init == '':
        init = input("          ")
    if init[0] == 'y':
        os.system('cls')
        main()
    else:
        print("          Thanks")
        l = input()
        l = False
        while not l:
            exit()
sub()
