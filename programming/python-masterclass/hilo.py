# lower+(upper-lower)/2
# lowest hightest guess answer
# 1       1000     500      707
# 500     1000     750      707
# 500      750     625      707
# 625      750     687      707
# 687      750     687+31=718 707
# 687       718   702
# 702      718    710
# 702      710    706
# 706      710    708
# 706      708    707

import random

lowest = 1
hightest = 1000
# answer = random.randint(lowest, hightest)
answer = 707
print("answer-->{0}".format(answer))
# answer = 707
guess = 0
guess = hightest //   2
count = 0
while hightest != lowest:
    print("\tguessing in the range of {} to {}".format(lowest,hightest))
    count += 1
    if (guess == answer):
        print("guess-->" + str(guess))
        print("well done.{0}".format(count))
        break
    elif (guess > answer):
        hightest = guess-1
    elif (guess < answer):
        lowest = guess+1
    guess = lowest + (hightest - lowest) // 2
    print("highest-->{}".format(hightest))
    print("lowest-->{}".format(lowest))
else:
    print("your guess {} is correct ".format(answer))
    print("you've guess {} times".format(count))
