#python function默认返回None
# def center_text(text): #定义function
#     width = 80
#     tex = str(text)
#     left_margin = (80-len(str(tex)))//2
#     print(" "*left_margin+tex)
# text = " ".join(12) #TypeError: can only join an iterable
# print(text)
def center_text(*args, end_test='\n', file_test=None, flush_test=False): #*args表示传入多个参数，可以进行迭代

    text = ""

    # text = " ".join(str(args))
    for arg in args:
        text += str(arg) +"rose"
    left_margin = (80-len(text))//2
    return " "*left_margin+text
    #print(" " * left_margin, text, end=end_test, file=file_test, flush=flush_test) #将print内容写入至文件file_test,with open("centered",mode='w') as centered_file:,file_test = centered_file;
with open("centered",mode='w') as centered_file:
    s1 = center_text("hello")
    print(s1,file=centered_file)
    # center_text("hello",file_test=centered_file) #调用function
    # center_text("sdgfdgfdggfh",file_test=centered_file)
    # center_text(12,file_test=centered_file)
    # center_text("sdfssfdsdsfdsfdsf",file_test=centered_file)
    # print(center_text(3,file_test=centered_file))
    # center_text("1","2","3",file_test=centered_file)
