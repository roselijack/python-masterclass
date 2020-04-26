numbers = [1,45,32,12,60]
for number in numbers:
    if number%8 ==0:
        print("the number {} is unacceptable".format(number))
        break
else:
    print("all the number are acceptable")