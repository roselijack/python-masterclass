with open("sample1.txt","a") as jaccob: #a表示追加，默认是text file

    for i in range(2,13):
        for j in range(1,13):
            print("{} times {} is {}".format(j,i,i*j),file=jaccob)
        print("-"*40,file=jaccob)#named argument必须等于jaccob，指定向哪个文件输出