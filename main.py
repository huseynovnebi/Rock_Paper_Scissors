import random

results = {
    "rock" : {
        "paper" : False,
        "scr" : True 
    },
    "paper" : {
        "rock" : True,
        "scr" : False 
    },
    "scr" : {
        "rock" : False,
        "paper" : True 
    }
}



while True:
    arr = ["rock","paper","scr"]
    user = input("Select rock-paper-scr(scissors) :")
    arr.remove(user)
    computer = random.choice(arr)
    status = results[user][computer]
    print(computer)

    if status:
        print("You won !")
    else:
        print("You lose !")    

