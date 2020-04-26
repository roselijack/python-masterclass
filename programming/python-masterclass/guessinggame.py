import random

hightest = 10
answer = random.randint(1,hightest)
#print(answer)

print("please guess number between 1 and {}:".format(hightest))
guess = int(input())
if(guess == answer):
    print("your answer is correct!")
else:
    if guess> answer:
        print("please guess lower:")
    else:
        print("please guess higher")
    guess = int(input())
    if guess== answer:
        print("well done")
    else:
        print("sorry, your answer isn't correct")





