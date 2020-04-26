#c124
import time
from time import perf_counter as my_timer
import  random
# print(time.gmtime(0))
# print(time.localtime(time.time()))
# print(time.time())
# time_here =time.localtime()
# print(time_here)
# print("year",time_here[0],time_here.tm_year)

# print("year",time_here[1],time_here.tm_mon)
# print("year",time_here[2],time_here.tm_mday)
input("press enter to start")
#wait_time = random.randint(1,6)
wait_time = 1

time.sleep(wait_time)
start_time = my_timer()
input("press enter to stop")
end_time = my_timer()
print("started at "+time.strftime("%X",time.localtime(start_time)))#%X:19:45:48,%x:04/18/20
print("ended at "+time.strftime("%X",time.localtime(end_time)))

print("your reaction time was {} seconds".format(end_time-start_time))

# time.gmtime(0)表示把0加上1970年1月1号0时0分0秒表示的时间转换为UTC格式的time tuple
# time.time()返回当前时间距离epoch时间的秒
# print(time.localtime(time.time()))把自从epoch开始过去了多少秒，转变为time tuple。
# 产生随机数字[1,6]。random.randint(1,6)
# from time import time as my_timer；start_time = my_timer()等同于start_time=time.time()
# time.strftime("%X",time.localtime(start_time))把time turple转变为指定格式的string,#%X:19:45:48,%x:04/18/20
# https://docs.python.org/zh-cn/3/library/time.html#time.strftime
# 如果想计算过了多久。最好的方法是用perf_counter
# 如果想知道任务在cpu上花了多久时间，最好方法是process_time
# 处理实际的时间而不是统计过去了多久时间，用time
