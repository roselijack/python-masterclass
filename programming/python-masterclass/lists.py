# a.count(x),total number of occurrence of x in a
# a.append(b), append b for list a
# c = a + b , add every elements in list a and list b into list c
# a.sort(),改变a的排序，不返回任何信息，不是新创建1个新的列表
# sorted(a),将list a元素排序不变，但是返回排好序的列表
# print(a) 输出列表
#print("c===>{0}".format(c))输出列表
# if a == b，判断两个列表是否相等
a = ["ab","bc","cd","ab"]
a.append("ef")
print("a======>{0}".format(a))
print("a.count(\"ab\")=======>{0}".format(a.count("ab")))
c = [1,3,2]
d = [4,5,6]
e = c+d
print("e=====>{0}".format(e))

# c2 = c.sort()
# print("c===>{0}".format(c))
#
# print("c2===>{0}".format(c2))
# if(c2 == c):
#     print("c2 ==c")
# else:
#     print("c2 != c")#
c1 = sorted(c)
print("c===>{0}".format(c))
print("c1===>{0}".format(c1))
if(c1 == c):
    print("c1 == c")
else:
    print("c1 != c")#


