value=int(input("enter a seconds:"))
ans=value//3600
minutes = (value % 3600) / 60
second=value%60
print(ans,"hours,",minutes,"minutes,",second,"second")