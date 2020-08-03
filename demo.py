def outer(fun):
	def inner(*args,**kwargs):
		print('args is {}'.format(*args),'**kwargs is {}'.format(**kwargs))
		print('hello')
		print('test over')
		return fun

def add(a,b):
	return a+b

sum=add(1,2)
print(sum)

outer(add(1,2))
# print(sum)
