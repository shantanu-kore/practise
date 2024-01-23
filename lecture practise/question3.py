
def celsius_to_f():
    Fahrenheit=(value*9/5)+32
    
    print("your fahrenhit value is:", Fahrenheit)
    return Fahrenheit

def fahrenhit_to_c():
    celsius=(value-32)*5/9
    print("your celsius value is:", celsius)
  
    return celsius

value=eval(input("enter a value to convert:"))

print("choose options:\n 1.celsius to fahrenhit \n2.fahrenhit to celsuis")
option=int(input("enter a option:"))
if option==1:
    celsius_to_f()
        
elif option==2:
    fahrenhit_to_c()
        
else:
    print("choose correct option")


