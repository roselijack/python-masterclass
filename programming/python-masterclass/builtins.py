# a = 12
# b = 4
# print(a + b)和print(a.__add__(b))调用的为同一个底层方法
# print(a.__add__(b))

#python中所有都是对象，
#如果function是class的一部分，称为method
class Kettle(object): #定义1个类
    power_source = "rose"

    def __init__(self,make,price): #类中构造函数
        self.make = make
        self.price = price  
        self.on = False

    def switch_on(self):
        self.on = True

kenwood = Kettle("kenwood",8.99) #实例化一个类
print(kenwood.make)
print(kenwood.price)

hamilton = Kettle("hemilton",14.55)
print(hamilton.make)
print(hamilton.price)
#如下两种写法等价，Kettle:类，kenwood：实例
Kettle.switch_on(kenwood)
kenwood.switch_on()
print(kenwood.on)
print(hamilton.on)

#如下两种写法等效
print("{} {}".format(kenwood.make,kenwood.price))
print("{0.make} {0.price}".format(kenwood))

kenwood.power = 1.5#给实例定义attribute值
print(kenwood.power)
#print(hamilton.power) #AttributeError: 'Kettle' object has no attribute 'power'

#建议在类的方法间间隔1行
#建议模块内的顶级function中间间隔两行
print("switch to atomic power")
Kettle.power_source = "atomic"
print(Kettle.power_source)
print("switch kenwood to gas")
kenwood.power_source = "gas"
print(kenwood.power_source)
print(hamilton.power_source)
print(Kettle.__dict__)#通过attribute __dict__查看该object的namespace
print(kenwood.__dict__)#通过attribute __dict__查看该object的namespace
print(hamilton.__dict__)

#获取实例的变量时，先查找该实例的namespace中是否存在这个变量。如果不存在则到实例的类中去检查是否存在这个变量

