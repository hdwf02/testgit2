import random
import numpy 
import re
from collections import Counter

ok=0
for i in range(1,101):
	ok=i+ok
print(ok)


# ===   等价写法
print(range(10))    #=== 返回的是列表   有问题：返回的是迭代器，可以节约内存
print(list(range(10)))  #====返回的是列表 
print(tuple(range(5)))

s=sum(range(101))   #===   range里面参数是 start,stop,step  默认从0开始 ，默认步长是1
print(s)  

print(sum([4,5,6]))  #=====   sum里面需要展示可迭代对象

print(sum([9,9,9],4))  #========  元组和列表是可迭代对象


#=== 如何在一个函数内部修改全局变量,有问题
# whole=None
# def lwjfun():
# 	whole="lwj"
# 	print('fun 内',whole)
# lwjfun()
# print('fun 外',whole)

#=== 如何在一个函数内部修改全局变量
print('=============')
whole=None
def lwjfun(self):
	whole="lwj"
	# print('fun 内',whole)
	print(self)
	# print(self.whole)  #====AttributeError: 'str' object has no attribute 'whole'
lwjfun("(1,2,3)")
print('fun 外',whole) 

#=== 如何在一个函数内部修改全局变量
print('=============')
whole=None
def lwjfun(self):
	whole="lwj"
	print(self)
	return whole        #====== return无效，未返回
	# print(self.whole)  #====AttributeError: 'str' object has no attribute 'whole'
lwjfun("(1,2,3)")
print('fun 外',whole) 

#=== 如何在一个函数内部修改全局变量
print('=============')
whole=None
def lwjfun(self):
	global whole       #======= global需要先声明
	whole='right lwj'
	print(self)
	return whole        #====== return生效
lwjfun("(1,2,3)")
print('fun 外',whole) 

#=== 列出5个python标准库
# os,datetime,sys,re,math


#=== 字典如何删除键和合并两个字典
print('=============')
lwjdict0={'key1':'value1','key2':'value2'}
lwjdict1={'key1':'value1','key2':'value2','age':18}
del lwjdict0['key1']          #== 删除使用del
print(lwjdict0)
print(lwjdict1)
lwjdict0.update(lwjdict1)      #===  更新使用update
# 更新后
print(lwjdict0,'update之后')
print(lwjdict1,'update之后')


#====== python GIL  ：Global Interpreter Lock
# 多进程时，多个进程可以同时运行
# 多线程时，多个线程运行有先后顺序，并不是同步进行，缺点：进程系统资源开销大


#===== python去重
print('=============')
lwjlist=[2,3,4,5,5,5,5,6]
print(lwjlist,'去重前')

after=set(lwjlist)
print(list(after),'去重后')

# python 2,3区别
print('=============')
print(range(5))    # 返回的是迭代器，节约内存，python2返回的是列表

# 能够使用装饰器的语言
# 函数可以作为参数传递的语言，可以使用装饰器

# python内建数据类型
# 6种：
# 整型  int   
# 布尔型 bool 
# 字符串 str 
# 列表list 
# 元组tuple
# 字典dict

# _new_和_init_区别
print('=============')
class BaseClass:
	def __init__(self,name,age):    
		self.name=name     #  执行时没有输出而已
		print('init 实例化时会执行')

	def my_name(self):
		print('my self.name is {}'.format(self.name))
		print('my self is {}'.format(self))

	def __new__(cls,name,age):              #必须要有一个cls参数
		print('this is cls ID',id(cls))
		print('this is cls new method',object.__new__(cls))
		# return 1        #必须要有一个返回值
		return object.__new__(cls)  

BaseClass('lwj实例化类1',0)              #  __init__方法在对象实例化的时候会执行，执行时没有输出而已
print('=============')
BaseClass('lwj实例化类2调用方法',1).my_name()    #  自定义方法在调用的时候才会执行，print才会有输出

print('静态方法————new___',BaseClass.__new__)        #  __new__ 是类的静态方法（可以不用添加静态方法装饰器），在类准备将自身实例化时调用的

print('静态方法————new___',BaseClass.my_name)    #================ 为啥这个属性没有报错，不是方法吗？
# 如果__new__创建的是当前类的实例，会自动调用__init__函数，通过return语句里面调用的__new__函数的第一个参数是cls来
# 保证是当前类实例，如果是其他类的类名，；那么实际创建返回的就是其他类的实例，
# 其实就不会调用当前类的__init__函数，也不会调用其他类的__init__函数

# 正常写法：
print('=============')
try:
	f=open('README.txt',mode='w')    #====== 注意参数格式及对应字符串
	f.write('\nhello')
	print(f)
except Exception as e:
	raise e
finally:
	f.close()
	print('aa')


with open('README.txt',mode='r+') as d:
	d.write('3')                    #======= 必须是字符串，数字参数是不正确的

# 使用map函数和列表推导式   map() 会根据提供的函数对指定序列做映射。
# 列表推导式的执行顺序：各语句之间是嵌套关系，左边第二个语句是最外层，依次往右进一层，左边第一条语句是最后一层。
print('=============')
new_list=list(range(1,6))
# print(new_list)
mapfun=map(lambda x:x*x,new_list)
print(list(mapfun))

#正常写法
print('=============')
def square1(x):
	return x*x
map_square=list(map(square1,[1,2,3,4,5]))
print(map_square,'if 筛选前')
map_square=[i for i in map_square if i>10]  #====  列表推导式原理
print(map_square,'if 筛选后')


#随机数方法  随机整数，随机小数，0-1之间的小数
print('=============')
print(random.random())   #默认0-1之间 ，不能加参数  
print(random.randint(10,30))  #10-30之间的随机数
print(numpy.random.randn(5))  #生成5个小数

#原始字符串
print('=============\n*******')
print(r'*******=============\n*******')  #使原始字符串强制不转义  raw strings

str='<div class="nam">中国</div>'

res=re.findall(r'<div class=".*">(.*?)</div>',str)  #============  为什么不返回类名,()是什么作用

print(res)   


#============  异常输出
aabb=3
assert aabb>2
# assert aabb==5    #===
# try:
# 	assert aabb==5
# 	raise Exception
# except Exception as e:      #=========  为什么没有输出异常
# 	print(e)



# try:
# 	assert aabb==3
# except:
# 	print('异常出现')

# assert aabb==3


# python2和python3的区别
# python2编码为ascii码，python3为utf-8
# 美国制定了一套字符编码，对英语字符与二进制位之间的关系，做了统一规定。这被称为ASCII码
# UTF-8就是在互联网上使用最广的一种Unicode的实现方式
# UTF-8是Unicode的实现方式之一

# 1、Python3 使用 print 必须要以小括号包裹打印内容，比如 print('hi')
# Python2 既可以使用带小括号的方式，也可以使用一个空格来分隔打印内容，比如 print 'hi'
# 2、python2 range(1,10)返回列表，python3中返回迭代器，节约内存
# 3、python2中使用ascii编码，python3中使用utf-8编码
# 4、python2中unicode表示字符串序列，str表示字节序列
#      python3中str表示字符串序列，byte表示字节序列
# 5、python2中为正常显示中文，引入coding声明，python3中不需要
# 6、python2中是raw_input()函数，python3中是input()函数
# Pyhton2.7 返回列表，Python3.x 返回迭代器对象，具体内容可以查看：Python3 filter() 函数


# 可变数据类型

# 不可变数据类型 元组，字符串型，数值型
lwjstring='lwjstring'
ccdd='lwjstring'

print(lwjstring)
print(ccdd)
print(id(lwjstring))   
print(id(ccdd))        #算是浅拷贝还是怎么样？ 

ee=(4,5,6)
print(ee)

ff=(4,5,6)
print(ff)
print(id(ee),'ee')
print(id(ff),'ff')

ee=(4,5,6,7,8,9)
print(ee)
print(id(ee),'ee')
print('=============')

ee1=[4,5,6]
print(ee1)

ff1=[4,5,6]
print(ff1)
print(id(ee1),'ee')
print(id(ff1),'ff')

ee1=[4,5,6,7,8,9]
print(ee1)
print(id(ee1),'ee')

ee1.append('append')
print(ee1)
print(id(ee1),'ee')

conarr=ff1.append(ee1)


# 去重s = "ajldjlajfdljfddd"
s = "ajldjlajfdljfddd"
sss=list(set(s))
print(sss)
ssort=sss.sort(reverse=True)
# print(sss.sort())      #list排序后并不返回新的列表
print(sss,'list 排序后对原列表做了修改')
aa=''.join(sss)    #str.join(sequence)  sequence -- 要连接的元素序列。 返回值生成新的字符串
print(type(aa))
print(aa) 

#lambda实现数相加
abcd=lambda x,y:x+y
print(abcd(3,5))

#dict根据键从大到小排序
dic={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
print(dic.items(),'dic.items()方法值展示')

bb=sorted(dic.items(),key=lambda i:i[0])   #lambda函数意思： 获取每个元组的key  
print(bb)

print(dict(bb))



complexvar=[('name', 'zs'), ('age', 18), ('city', '深圳'), ('tel', '1362626627')]
for i in complexvar:
	print(i)
	print(i[0])
tuplevar=('lwj','miaomiao')
print(tuplevar[1])     # ======  元组获取值方式与列表一致

print('=============') #======= 利用counter方法，统计每个单词的个数
#====== longstrkjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h
longstr='kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h'
# dd=re.search((;),longstr)
# print(dd)

sums_long=Counter(longstr)
print(sums_long)

print('=============') #filter方法求出列表所有奇数并构造新列表
short_list=[1,2,3,4]

def oddfn(x):
	return x%2==1
aa=filter(oddfn,short_list)     #======= 返回的是filter object对象
print(list(aa))


print('=============') #列表推导式求列表所有奇数并构造新列表
short_list=[1,2,3,4,1,2,3,4,9,3,6,111]
long_list=[i for i in short_list if i%2==1]  #第一个语句是最后返回，第二个语句就是固定的for语句，其他的语句0或多个
print(long_list)

print('=============') #a=（1，）b=(1)，c=("1") 分别是什么类型的数据？
print(type(((((((1,))))))))
print(type((((((((1)))))))))
print(type(((((((("1")))))))))  
# <class 'tuple'>
# <class 'int'>
# <class 'str'>
#====== 列表合并的方法 append 以列表的形式追加到一个元素的位置
print(conarr,'合并后的列表')
print(ff1,'合并后的列表')
# print(ee1,'合并后的列表')
conarr=ff1.extend(ee1)       #===  在原列表内进行修改
print(conarr,'合并后的列表')
print(ff1,'合并后的列表')