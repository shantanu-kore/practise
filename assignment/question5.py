def ms_hr():
    speed=float(input("enter km/hr:"))
    meter_sec=speed*1000/3600
    print(meter_sec)

def km_hr():
    speed=float(input("enter a m/s:"))
    kilm_hr=speed*3600/1000
    print(kilm_hr)

i=0
while i==0:
    print("choose option \n 1.hm/hr to m/s \n 2.m/s to km/hr")
    option=int(input("enter your choise:"))
    if option==1:
        ms_hr()
    elif option==2:
        km_hr()
    else:
        print("choose correct option")
    
