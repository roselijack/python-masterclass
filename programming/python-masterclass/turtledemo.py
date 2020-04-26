#import turtle
from turtle import *
import time
def done():
    print(1)
#noinspection PyUnresolvedReferences能够让编译器不报UnresolvedReferences的warning
forward(150)
right(250)
forward(150)
done()
#done() 新出来的ui窗口不立即关闭，点击出来的图形窗口放大健进行放大，缩小键进行缩小，关闭键进行关闭

#time.sleep(4) #停止4秒后关闭程序
 #点击出来的图形窗口放大健进行放大，缩小键进行缩小，关闭键进行关闭


#done()
#noinspection PyUnresolvedReferences能够让编译器不报UnresolvedReferences的warning
# 效果等同于修改analyze->configure current code analyze->configure inspections->inspections->unresolved references
# 两种import module中method的方法
# 1.from turtle import forward,right
# forward(500)
# 2.import turtle
# turtle.forward(500)
# 如果不是写交互设计的代码，不建议用 from turtle import *，因为不清楚turtle中有哪些方法，万一和代码中自定义的方法名产生冲突，则难以排查
# import time
# time.sleep(4) #停止4秒后关闭程序