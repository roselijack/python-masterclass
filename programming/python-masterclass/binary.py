for i in range(17):
    print("{0:>2} is {0:>08b}".format(i))#输出宽度为8位，右对齐，二进制。
    print("{0:>2} is {0:>08x}".format(i))#输出宽度为8位，右对齐，16进制。
    #hex,decimal,binary
print(0b101010)#42，将二进制转换位10进制。
y = 0x0a #16进制。一般用数字0到9和字母A到F表示，其中:A~F相当于十进制的10~15
x = 0x20


print(x)
print(y)
print(x*y)



print()
