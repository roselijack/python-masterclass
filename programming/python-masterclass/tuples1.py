test = "1",2,"new","old"
#a,b,c = test #unpacking turple时左边变量的个数必须和右边元祖的元素个数一直。如果左边变量个数较少，会报错ValueError: too many values to unpack
a,b,c,d = test #a:1 b:2 c:new d:old
print("a:{} b:{} c:{} d:{}".format(a,b,c,d))

imdeda = "more may","ime may", 2001,(
    (1, "pulling"),(2,"psycho"),(3,"mayhem"),(4,"ken"))
name, artist, year, tracks = imdeda
print("{}   {}  {}  {}".format(tracks[0][1],tracks[1][1],tracks[2][1],tracks[3][1]))
#用for a in tuple:来轮询1个数组
for song in tracks: #song是tracks元祖中的元祖
    number,title = song
    print("number:{} title:{}".format(number,title))

#如果tuple中某个元素是list，则该list是可以被改变的。
imdeda1 = "more may","ime may", 2001,[
    (1, "pulling"),(2,"psycho"),(3,"mayhem"),(4,"ken")]
name1, artist1, year1, tracks1 = imdeda1
tracks1.append((5,"rose"))
for song in tracks1:
    number,title = song
    print("number:{} title:{}".format(number,title))


lista = [1,2,3]
listb = [1,3,2]
print(listb == lista) #False,相同的列表需要有相同的元素和相同的顺序

numbers = range(13)

new_range = numbers[1::2]
for i in new_range:
    print(i, end=', ')

even = range(0, 20, 2)

for number in even[::-1]:
    print(number, end=', ')
#The slice [::-1] reverses the range, which was counting from 0 up to (but not including) 20, in steps of 2.