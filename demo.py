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


# 

