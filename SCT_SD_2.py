import random
guesses_took=0
max_guesses=3
print("Hi Dear! May I know Your Beautiful Name : ")
naam=input()
n=random.randint(1,30)
print('Dear  '+naam+',I am thinking one number between 1 to 30.')
while guesses_took<max_guesses:
    print(f"Can You Guess My number.You have {max_guesses-guesses_took} chances in your hand.Make a Guess {naam} :")
    gu=input()
    g=int(gu)
    guesses_took+=1
    if g==n:
        print("BOOYAH!!! You Nailed it.")
        print(f"Nice Job,{naam}.You took {guesses_took} guesses to guess my number.")
        break
    else:
        print("OOPS!!! your guess is Incorrect.")


if g!=n:
    n=str(n)
    print("Sorry Your guesses are over.")
    print('But Well Tried,'+naam+'.I would like to reveal my number,i.e.,'+n)
    