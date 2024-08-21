p=23
g=9
print('the value of p is:%d'%(p))
print('the value of g is:%d'%(g))
a=4
print('the private key a for alice is:%d'%(a))
x=int(pow(g,a,p))
b=6
print('the private key b for bob is:%d'%(b))
y=int(pow(g,a,p))
ka=int(pow(y,a,p))
kb=int(pow(x,a,b))
print('secert key for the alice is:%d'%(ka))
print('secert key for the bob is:%d'%(kb))

