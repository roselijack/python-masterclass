a = ['123','aabce',"abccd","abcdef"]
result = []

for i in range(len(a)):

    if len(a[i])==5:
        print(a[i])
        dic = {}
        for j in range(5):
            if a[i][j] in dic:
                count = dic.get(a[i][j])
                count = count+1
                dic[a[i][j]] = count
            else:
                count = 1
                dic[a[i][j]] = 1
        result.append(dic)
        for b in dic:
            print(b+"-"+str(dic.get(b)))
print(result)
# for i in result:
#     for j in result[i]:
#         print(j+"-"+result[i].get(j))



