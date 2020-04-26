adventure_direct = ["W","S","E","N"]
original = ""
while original not in adventure_direct:
    original = input("please input your direction")
    if original.casefold()=="quit":
        print("game over")
        break
    #如下三句不需要达到效果也一样
    # if original not  in adventure_direct:
    #     print("not correct exit")
    #     original = input("please input your direction")
else:
    print("aren't you glad to exit")
