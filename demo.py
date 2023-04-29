def outer(fun):
	def inner(*args,**kwargs):
		# print('args is {}'.format(args),'**kwargs is {}'.format(**kwargs))
		print('argslwj',*args,'**kwargs',**kwargs)
		print('hello')
		
		a=fun(*args,**kwargs)
		print('a is',a)
		print('test over')
		# return fun
	return inner

@outer
def add(a,b):
	return a+b

# sum=add(1,2)
add(11,2)
# print('sum is {}'.format(sum))
print('====================')
outervalue=outer(add(1,2))
print('====================')
print('装饰器')
print('outervalue is {}'.format(outervalue))


#++++++++++ how to write decorator codes

L = [1, 2, 3, 11, 2, 5, 3, 2, 5, 3]
print( list(set(L)))

# set  去重

# 递归 ：阶乘实现
def a(n):
	if n==1:
		return 1
	else:
		return n*a(n-1)
jiehceng=a(3)
print(jiehceng)

# 匿名函数,可以用变量来调用该函数
a=lambda x:x+1
print(a(3))
print(a)  

mapvalue=list(map(lambda x,y:x+y,[3,6],[8,5]))
print(mapvalue) 


# 中国='china'
# print(中国) 

# print hello
print('==================')
arr=[1, 2, 3, 11, 2, 5, 3, 2, 5, 3]
iterr=arr.__iter__()
print(iterr.__next__())
print(iterr.__next__())


print('==================')
arr={'x':12,'y':56,'c':'lwk'}
iterr=arr.__iter__()
print(iterr.__next__())
print(iterr.__next__())


print('==================')
# class lwjiter:
# 	def __init__(self,*args,**kwargs):
# 		self.values = args;		
# 	def __iter__(self):
# 		self.index = 0;
# 		reutrn self;
# 	def __next__(self):		
# 	    tmp =  self.values[self.index];
# 	    self.index= self.index+1
# 	    return tmp;

 # [1,2,3]*2

 # return;
xx = 5

def lambda1(x):
    return x*2
result = lambda1([1,2,3])
 





