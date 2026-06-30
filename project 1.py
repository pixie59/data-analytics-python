import random
def game(user,computer):
    if user==computer:
        return None
    if user=="s" and computer=="w":
        return True
    elif user=="w" and computer=="s":
        return False
    if user=="w" and computer=="g":
        return True
    elif user=="g" and computer=="w":
        return False
    if user=="g" and computer=="s":
        return True
    elif user=="s" and computer=="g":
        return False
a=random.randint(1,3)
if a==1:
    computer="s"
elif a==2:
    computer="w"
else:
    computer="g"
print ("Computer's turn: Snake(s), Water(w), Gun(g)")
user=input("User's turn: Snake(s), Water(w), Gun(g):").lower()
won=game(user,computer)
print("you chose",user)
print("Computer chose",computer)
if won is None:
    print("Its a tie")
elif won is True:
    print("User won")
else:
    print("Computer won")