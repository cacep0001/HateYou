import random

print('HateYou 1.0.0')
print("For show command list, enter 'help'.")

worda = ["nope", "nuh uh",  "There is no real commands, don't try.", "No, don't try even.", "Do you really want to know?", "Go away", "Are you so interested?", "ACCESS DENIED. PLEASE TRY AGAIN."]

def rando():
    hate = random.choice(worda)
    print(hate)

while(True):
    c = input(">>> ")
    
    if c == "help":
        print("===COMMANDA===")
        print("math — Mathematics?")
        print("whatdoido — idk what to put here")
        print("joke — Generates a joke")
        print("random — Generates random number")
        print("tip — Generates you a tip.")
        
    elif c == "math":
        rando()
        
    elif c == "whatdoido":
        rando()
        
    elif c == "joke":
        rando()
        
    elif c == "random":
        rando()
        
    elif c == "tip":
        rando()
        
    else:
        print("Here is no command '" + c + "'.")
