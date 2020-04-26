location = {0:{"desc":"you are sitting, hehi",
               "exits":{},
               "nameExits":{}},
            1:{"desc":"you are standing",
               "exits":{"W":2,"E":3,"N":5,"S":4,"Q":0},
               "nameExits":{"2": 2, "3": 3, "5": 5, "4": 4}},
            2:{"desc":"you are in the hill",
               "exits":{"N":5,"Q":0},
               "nameExits":{"5": 5}},
            3:{"desc":"you are inside",
               "exits":{"W":1,"Q":0},
               "nameExits":{"1": 1}},
            4:{"desc":"you are in vallege",
               "exits":{"N":1,"W":2,"Q":0},
               "nameExits":{"1": 1, "2": 2}},
            5:{"desc":"you are in the forest",
               "exits":{"W":2,"S":1,"Q":0},
               "nameExits":{"2": 2, "1": 1}}}


vocabulary = { "QUIT":  "Q",
               "NORTH": "N",
               "SOUTH": "S",
               "EAST":  "E",
               "WEST":  "W",
               "ROAD": "1",
               "HILL": "2",
               "BUILDING": "3",
               "VALLEY": "4",
               "FOREST": "5" }
loc = 1
while True:
    #print(exits[loc].keys())#dict_keys(['W', 'E', 'N', 'S', 'Q'])
    #availableExits = ", ".join(exits[loc].keys())#获取字典类型里嵌套的字典的keys,并且把keys里面的除了最后一个key外其他每1个key后缀加上","
    print(location[loc])

    if loc == 0:
        break
    allexists = location[loc]["exits"].copy()#字典allexists内容和exits[loc]一样。改变allexists内容后exits[loc]内容不变化
    allexists.update(location[loc]["nameExits"])#allexists内容被改变，添加了dic "namedExits[loc]"内容，但返回为None
    print("-"*40)
    print(allexists.items())
    direction = input("available exits are {}".format(allexists.keys())).upper()
    if len(direction)>1:

        words = direction.split()#这样只要输入的句子中包含有west,north,south,east就可以识别
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]
                break
        # if direction in vocabulary:
        #     direction = vocabulary[direction]
        # else:
        #     print("you can't go to that direction")

    if direction in allexists:
        loc = allexists[direction]
        print("loc:{}".format(loc))#不能写成print("loc:"+loc),不然会报错str不能和int相连接
    else:
        print("the direction isn't found")

        #veg.update(fruite),返回none,veg变化 ,
        #a.copy().a不变化，返回1个同样的b