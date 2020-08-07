# #=== 32
# python os.remove(filename)
# linux rm 

import logging
import time
import datetime    

# datetime 比 time 高级了不少，可以理解为 datetime 基于 time 进行了封装，
# 提供了更多实用的函数。在datetime 模块中包含了几个类:time,date,datetime,timedelta（计算时间跨度）,tzinfo(时区相关)
now_time=time.time()
now_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
now_weekday=datetime.datetime.now().isoweekday()
now_weekday=int(now_weekday)
print(type(now_time),type(now_weekday))
print(' {} 星期 {}'.format(now_time,now_weekday))


#===== 数据库优化不是太懂 外键，索引，联合查询，选择特定字段等待
#====== python 统计图 pychart ,matplotlib

try:
	a=3
	# assert a>5  #=====  
	print(a)
	raise Exception('一般的错误')
	print('抛异常还是输出吗')
except Exception as e:
	print(e)
	# print()
finally:
	print('finally')

print('=====================') #===== 断言错误的写法
# try:
# 	a=3
# 	assert a>5  #=====  
# 	# print(lsssssss)
# 	raise AssertionError('断言错误了')
# 	print('抛异常还是输出吗')
# except AssertionError as e:
# 	print('{} ,{},星期：{},{}'.format(now_time,now_time,now_weekday,now_weekday))	
# 	raise  #=抛出断言的错误
# else:
# 	print('断言成功')

#========== 写一段自定义异常的代码
print('=============')
def aberant():
	try :
		for i in range(8):
			print(i)
		print('i是是不是全局变量，看看能不能打印出来',i)
		if i>3:
			print(i)
			raise Exception('数字大于3了')    #========  为什么大于3还输出4
	except Exception as e:
		print('{} ,星期{} ,异常是{}'.format(now_time,now_weekday,e))
	else:
		print('没有异常发生')
aberant()


fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
   print( '当前水果 :', fruit)
print(fruit)


print('===============')
# a=3
# b=4
# if a>b:
# 	return "3>4"   #================='return' outside function

#[[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]

prc=[[1,2],[3,4],[5,6]]
zz=[j for i in prc for j in i ]
print(zz)

# x="abc",y="def",z=["d","e","f"],分别求出x.join(y)和x.join(z)返回的结果
x="abc"
y="def"
z=["d","e","f"]
print(x.join(y))
print(x.join(z))
# print(z.join(x))        #====== 只有字符串有join属性
print('-'.join(x))


#==========python中交换两个数值
a,b='cuicui','enci'  #=========字符串可迭代  遍历是目的，迭代是手段。
a,b=b,a
print(a,b)

a,b='cuic','enci'
tmp=b
b=a
a=tmp
print(a,b)


#zip()函数在运算时，会以一个或多个序列（可迭代对象）做为参数，返回一个元组的列表
print(list(zip(a,b)))   

aa=[i[0] for i in zip(a,b)]
print(aa)

#====sql语句
# select * from table where XXX
# insert into table (field1,field2) values(value1,value2)
# delete from table where XXX
# update table set filed1=value1 where XXX
# select * from table orderby filed1 desc
# select * from table count(filed1) where orderby filed1
# select sum(filed1) from table 
# select avg(0) from table
# select max(filed1) from table
# select min(field2) from table


# 编码bytes类型
aa=b"hello".decode()   # byte字节类型
bb="您好高".encode()   #===========encode为字节类型
cc='heello'
print(aa,bb,cc)   #b'hello' b'\xe6\x82\xa8\xe5\xa5\xbd\xe9\xab\x98' heello (b是字节符号)
print(type(aa),type(bb),type(cc))
print('============')

#字节和二进制的关系
# 字(Byte)节是bai长度单位。位（bit)也是长度单位。
# 因为du计算机通信和存储的时候zhi都是以010101这样的二进制数据为dao基础的，
# 这儿的一个0和1占的地方就叫bit(位),即一个二进制位。
# 二进制=0111100000  其中1和0都是一个bit，8个bit可以组成1个字节

# python2编码为ascii码，python3为utf-8
# 美国制定了一套字符编码，对英语字符与二进制位之间的关系，做了统一规定。这被称为ASCII码
# UTF-8就是在互联网上使用最广的一种Unicode的实现方式
# UTF-8是Unicode的实现方式之一

# ASCII码使用bai一个字节编码，所以它的范围基本是只有英du文zhi字母、数字和一些特殊符dao号 ，只有256个字符。
# Unicode能够表示全世界所有的字节

# *首先要搞清楚，字符串在Python内部的表示是unicode编码，因此，在做编码转换时，通常需要以unicode作为中间编码，
# 即先将其他编码的字符串解码（decode）成unicode，再从unicode编码（encode）成另一种编码。
# =================字节与字符串的转换

aa="中文".encode()    #=======默认字符串编码转换为encode
# aa="中文".decode()    ======='str' object has no attribute 'decode'
print(aa,type(aa))

bb=aa.decode('utf-8') #========字节转码为字符串
# bb=aa.encode() #========字节转码为字符串  'bytes' object has no attribute 'encode'
print(bb,type(bb))


print('=============')
# [1,2,3]+[4,5,6]的结果是多少？
a=[1,2,3]
b=[4,5,6]
c=[i[0]+i[1] for i in zip(a,b) ]
print(c)
print(a+b)

# 提高python运行效率的方法
# 1、使用生成器，因为可以节约大量内存 
# 2、循环代码优化，避免过多重复代码的执行 
# 3、核心模块用Cython  PyPy等，提高效率 
# 4、多进程、多线程、协程 
# 5、多个if elif条件判断，可以把最有可能先发生的条件放到前面写，这样可以减少程序判断的次数，提高效率

# mysql和redis的区别
# redis: 内存行数据库，存在内存中，速度kuai
# mysql:关系型数据库，存在硬盘中，检索时，会有一定的io操作较慢

# # list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]  冒泡排序写法
# arrlist=[2,3,5,4,9,6]
# arr=[]
# for i in range(len(arrlist)):
# 	for j in 

# 写一个单例模式  
class Singleton(object):

  __instance =None

  def  __new__  (cls, age,  name ):

  #如果类属性__instance的值为None,

  #那么就创建一个对象，并且赋值为这个对象的引用，保证下次调用这个方法时能够知道之前已经创建过对象了，这样就保证了只有1个对象

     if not cls.__instance:

         cls.__instance =object.__new__ (cls)

     return cls.__instance

a = Singleton(18, "dongGe" )

b = Singleton(8, "dongGe")

print(id(a))

print(id(b))

a.age=19#给a指向的对象添加一个属性

print(b. age)#获取b指向的对象的age属性


# 保留两位浮点数   注意编写细节

num=1.5555
print('num is %.2f'%num)   
print(round(float(num),2))


# ==============
print('==============')
A = zip(("a","b","c","d","e"),(1,2,3,4,5))
# A0 = list(A)  #====A0 [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
A0 = dict(A)
print('A0',A0)
A1=range(10)
A2=[i for i in A1 if i in A0]
A3=[A0[s] for s in A0]

# print(list(zip(("a","b","c","d","e"),(1,2,3,4,5))))
print('A2',A2)
print(A3)

print('==============')  #============为假的元素
# [],{},(),'',None,0,False没有Null的语法

# any,all区别
# any(iterable)
print(any([1,2,3,'']))
print(all([1,2,3,'']))

# copy与deepcopy的区别

# 1、复制不可变数据类型，不管copy还是deepcopy,都是同一个地址当浅复制的值是不可变对象（数值，字符串，元组）时和=“赋值”的情况一样，对象的id值与浅复制原来的值相同。
# 2、复制的值是可变对象（列表和字典）
# 浅拷贝copy有两种情况：
# 第一种情况：复制的 对象中无 复杂 子对象，原来值的改变并不会影响浅复制的值，同时浅复制的值改变也并不会影响原来的值。原来值的id值与浅复制原来的值不同。
# 第二种情况：复制的对象中有 复杂 子对象 （例如列表中的一个子元素是一个列表）， 改变原来的值 中的复杂子对象的值  ，会影响浅复制的值。

# 深拷贝deepcopy：完全复制独立，包括内层列表和字典

import copy

profiles_info = {
    "name" : "lianglian",
    "age"  : 12,
    "job"  : "IT",
    "hobby": {
        "book"    : "三国演义",
        "movement": "skateboard"
    }
}
new_info = profiles_info.copy( )
new_profiles_info = copy.deepcopy(profiles_info)
print(new_info)
print(new_profiles_info)

profiles_info['age'] = 16
profiles_info['hobby']['book'] = '三体'
print(new_info)  # 只复制第一层，所以第二层会改变
print(new_profiles_info)  # 复制全部，所以不会改变
print(id(profiles_info))
print(id(new_info))
print(id(new_profiles_info))

print('==========')  #魔法方法






class LwjClass:
	def __init__():
		"""
		__init__:对象初始化方法
		"""
		pass
	def __new__():

		# __new__:创建对象时候执行的方法，单列模式会用到 
		pass

	# def __str__():
	#     # __str__:当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打
	#     # 印从在这个方法中return的数据
 #    	pass

     # def __del__():
     # 	 # __del__:删除对象执行的方法
     # 	 pass
 #    def __str__():

	# 	# __new__:创建对象时候执行的方法，单列模式会用到 
	# 	pass
	# def __del__():

	# 	# __new__:创建对象时候执行的方法，单列模式会用到 
	# 	pass

LwjClass

import sys

print(sys.argv)  # 输出文件名及对应的文件参数，以列表形式展示

print('=======') #将列表推导式修改为生成器（即特殊的迭代器）
aa=[i for i in range(5)]
print(aa)
aa=( i for i in range(5))   #方括号改为小括号，即变为生成器了，生成器要遍历才能显示对应的元素
print((range(5)),'python3里面的迭代器')   #python2 range(1,10)返回列表，python3中返回迭代器，节约内存
for i in range(5):
	print(i,"迭代器元素")
print(aa,'自己生成的一个生成器元素')
for i in aa:
	print(i,'aa生成器元素自己进行遍历和访问')


#生成器
# def lwj_genereate_fun():
# 	for i in range(5):
# 		yield i
# 		print(i)

# print(lwj_genereate_fun()) 

# 列表推导式
names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
         ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
name_filter=[name for index in names for name in index if name.count('e')>=2]

print(name_filter)


# 迭代器和生成器的关系：生成器是特殊的迭代器！！！！
# 生成器表达式和列表推导式的区别:
# 列表推导式比较耗内存,所有数据一次性加载到内存。而.生成器表达式遵循迭代器协议，逐个产生元素。
# 得到的值不一样,列表推导式得到的是一个列表.生成器表达式获取的是一个生成器
# 列表推导式一目了然，生成器表达式只是一个内存地址。


#====a = "  hehheh  ",去除首尾空格
a = "       hehheh "
bb=a.strip('h') #==移除字符串头尾指定的字符序列,默认是空格或者换行符
cc=bb.strip('h')
print(a)
print(bb)
print(cc)


# 对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4],使用lambda函数从小到大排序
foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
# foo.sort()
print(foo)
foo_new=sorted(foo,key=lambda i:i)
# sorted(iterable, key=None, reverse=False)  

# 使用lambda函数对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]，输出结果为[0,2,4,8,8,9,-2,-4,-4,-5,-20]，正数从小到大，负数从大到小

cc=sorted(foo,key=lambda i:(i<0,abs(i)))
# key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
print(cc)

# 列表嵌套字典的排序，分别根据年龄和姓名排序
foo = [{"name":"zs","age":19},{"name":"ll","age":54},{"name":"wa","age":17},{"name":"df","age":23}]
# foo_new=[ person for person in foo ]
foo_new=sorted(foo,key=lambda x:x['name'])   #按名称进行排序
foo_age=sorted(foo,key=lambda x:x['age'])
print(foo_new)
print(foo_age)
# foo_new=sorted(foo)


print('==========')
# 列表嵌套元组，分别按字母和数字排序
foo = [("zs", 19), ("ll", 54),("wa",17), ("df", 23)]
foo_ca=sorted(foo,key=lambda x:x[0])
foo_num=sorted(foo,key=lambda x:x[1])
print(foo_ca)
print(foo_num)

print('==========')
# 列表嵌套列表排序，年龄数字相同怎么办？
foo = [["zs", 19], ["ll", 54],["wa",23], ["df", 23],["xf",23]]
foo_num=sorted(foo,key=lambda x:(x[1],x[0]))
print(foo_num)

print('==========')
#根据键对字典排序   根据dict的items方法
dic = {"name":"zs","sex":"man" ,"city":"bj"}
tran=dic.items()    #============返回可遍历的(键, 值) 元组数组。
trans=list(tran)
print(trans)
# print(list(tran))
new_dict=sorted(trans,key=lambda x:x[0])
print(new_dict)


print('==========')
#根据键对字典排序   根据zip方法
dic = {"name":"zs","sex":"man" ,"city":"bj"}
print(dic.keys(),dic.values())
new_dic=zip(dic.keys(),dic.values())
print(new_dic)
new_dic=list(new_dic)
print(new_dic,'yyyyyyyyy')
new_sort=sorted(new_dic,key=lambda x:x)
print(new_sort,'xxxxxxxxxx')
# 在转变为字典格式
new_dic={i[0]:i[1] for i in new_sort}
print(new_dic)

 		
