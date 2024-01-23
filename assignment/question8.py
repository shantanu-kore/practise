import random
num1=random.randint(1,10)
num2=random.randint(1,10)
random_list=['+','-','*','/']
opr=random.choice(random_list)
ans=str(num1,opr,num2)
print(ans)
