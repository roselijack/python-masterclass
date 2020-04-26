a = "rose","jack",1988#turple:有序的数据集，不可改变。逗号是元祖必须的，括号只是为了避免歧义才需要，不是必须
#1. a dictionary key requires immutalbe object 2.list包含的元素是相同类型，元祖包含的元素可以是不同类型。
print(a)#('rose', 'jack', 1988)，说明返回的是元祖
print(a[0])#rose,元祖支持索引和分片
print("a","b","c")# a b c
print(("a","b","c"))#("a","b","c"),用括号表示元祖是为了避免歧义，建议尽量使用元祖

bad = "bad","good",2020#元祖的元素能包含不同的数据类型
#bad[0] = "bad1"#会报错，元祖的元素不能被重新赋值。tuple object does not support item assignment
#print("=="+bad)#a type being immutable means that you can't change the contents of an object once you've created.but
#it doesn't mean that your variable can't be assigned a new object of that ype
bad = bad[0],"good1",bad[2]#不会报错。整个元祖可以赋新值。
print(bad)

a = ["rose","jack",1989]
print(a)
a[0] = "rose1"
print(a2)
title ,artist,year = a2 #unpacking turple
print(title)
print(artist)
print(year)
