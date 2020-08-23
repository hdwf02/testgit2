def outer(somefun):
	def inner(*args):
		print('before somefun')
		ret=somefun(*args)
		print(ret)
		# return ret+1

	return inner   #=======  return func name

def foo():
	return 1

@outer
def tes(a,b):
	return a+b



decorated=outer(foo)
decorated()

tes(3,5)