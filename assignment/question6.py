import math
def test():
    a=int(input("enter value of 'a':"))
    b=int(input("enter value of 'b':"))
    c=int(input("enter value of 'c':"))

    delta=(b*b)-4*a*c
    sq=math.sqrt(delta)
    root1=(-b +sq)/(2*a)
    root2=(-b -sq)/(2*a)
    print(root1)
    print(root2)

test()
