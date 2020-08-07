#============  super practice python3

class Base:
	def __init__(self,name,age=10):
		self.name=name
		self.age=age

	def whois(self):
		# print('i am {}'.format(self.name))
		# print('=====',self.name)
		print(self.age)
		print(self.name)

class Person(Base):
	def __init__(self,name):
	    super().__init__(self,name)
	    super().whois()

	    # print('=====',self.name)
	    # print('i am {}'.format(self.name))
	    # pass

# aa=Base('lily').whois()
# print(aa)
# bb=Person('lucy') 
# 水仙花1
for a in range(1,10):
    for b in range(0,10):
        for c in range(0,10):
            if a*100+b*10+c==a**3+b**3+c**3:
                print(a*100+b*10+c)


print('====================')
# 水仙花1
arr=[]
for i in range(100,1000):
    # gewei
    a=i%10
    # shiwei
    b=int(i/10)%10
    # baiwei
    c=int(i/100)
    # print(a,b,c)
    # print(arr)
    if i==a*a*a+b*b*b+c*c*c:    	
        arr.append(i)
        print(arr)
        # return arr       #============   SyntaxError: 'return' outside function
        
print(arr)