import random

def role(dice):
    r = random.randint(1, dice)
    return r


rolagem = input()
numb = int(rolagem[6:])
rolagem = rolagem[:6]

if rolagem == "role d" or rolagem == "Role d":
    print(role(numb))


