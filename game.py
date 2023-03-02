import random
def gamewin(ai,you):
    if ai==you:
        return None
    elif ai=='r':
        if you=='p':
            return False
        elif you=='s':
            return False
    elif ai=='p':
        if you=='r':
            return True
        elif you=='s':
            return True
    elif ai=='s':
        if you=='p':
            return False
        elif you=='r':
            return True
        
print("AI's turn: Rock 'r', Paper 'p' or Scissor 's': ")
rand=random.randint(1,3)
if rand==1:
    ai='r'
elif rand==2:
    ai='p'
elif rand==3:
    ai='s'

you=input("Your turn: Rock 'r', Paper 'p' or Scissor 's': ")
a=gamewin(ai,you)
print(f"AI choose {ai}")
print(f"You choose {you}")

if(a==None):
    print("Tie")
elif a:
    print("You Win")
else:
    print("You lose")


