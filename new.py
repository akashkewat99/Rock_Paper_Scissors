def ask():
   while (True):
    x=input("Do you wanna play more? ").lower()
    if x in ["yes","no","exit"]:
        if x=="no" or x=="exit":
            return True
        return False
    else:
       print("Please check your typo")
      
def statement_bot(c):
    if c=="paper": print(" | Papers covers Rock")
    elif c=="scissor": print(" | Scissor cut paper")
    else: print(" | Rock break scissor")

def statement_user(p):
    if p=="paper": print("    | Papers covers Rock")
    elif p=="scissor": print("    | Scissor cut paper")
    else: print("    | Rock break scissor")

def emoji(c):
  d={
    "rock":"🪨",
    "paper":"📰",
    "scissor":"✂️"}
  if c in d:
    return d[c]

def check(p):
    if p in ["rock", "paper", "scissor"]:
      return True
    return False

def bot_input():
  # import random
  # mylist = ["rock", "paper", "scissor"]
  # print(random.choice(mylist))
  from random import randint
  t = ["rock", "paper", "scissor"]
  botL = t[randint(0,2)]
  return botL

##################################################################################################################

def playing():
    draw=0
    game_count=0
    user_won=0
    bot_won=0
    i="yes"
    p=input("Rock, Paper, Scissor? ").lower()
    while (i=="yes") and (p != "exit"):
       c=bot_input()
       if check(p):
          game_count+=1
          if c==p:
             print("   🎌 Draw 🎌   ")
             print("You both chose: ",emoji(c))
             draw+=1
             if ask():
                return draw,game_count,user_won,bot_won
             else:
                p=input("Rock, Paper, Scissor? ").lower()
          elif (c=="rock" and p=="paper") or (c=="paper" and p=="scissor") or (c=="scissor" and p=="rock"):
            print("    | You chose:",(emoji(p)*3), " |" " Bot chose:", emoji(c),)
            print("    | Woohoo!!! You won,",name,"🥳")
            user_won+=1
            statement_user(p)
            if ask():
               return draw,game_count,user_won,bot_won
            else:
               p=input("Rock, Paper, Scissor? ").lower()            
            
          elif (c=="rock" and p=="scissor") or (c=="paper" and p=="rock") or (c=="scissor" and p=="paper"):
            bot_won+=1
            print(" | Bot Choose:",emoji(c)*3, " |" " You chose:",emoji(p))
            print(" | You lose!","😜")
            statement_bot(c)
            if ask():
               return draw,game_count,user_won,bot_won
            else:
               p=input("Rock, Paper, Scissor? ").lower()
            
       else:
          print("✋ Please check typoo!!")
          p=input("Rock, Paper, Scissor? ").lower()
    return draw,game_count,user_won,bot_won

##################################################################################################################
#START
name=input("Your Good Name👻 ")
print("👋 Hello "+name+ ", Finger Crossed🤞")
draw,game_count,user_won,bot_won=playing()

print("🤘You won {} games and {} tie(s), ouf of {}. [🤖: {}]".format(user_won,draw,game_count,bot_won))
if bot_won>user_won: print("🤖 Bot is winner")
elif game_count==0: print("Not played, come soon👋")
elif bot_won==user_won: print("🎌DRAW... Come Soon.. .")
else: print("You are Rocking🤘")