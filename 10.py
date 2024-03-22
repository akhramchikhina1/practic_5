pin=input()
a=int((int(pin))//1000)
d=int(int(pin)%10)
c=int((int(pin)%100-d)/10)
b=int((int(pin)%1000-d-(int(pin)%100-d))/100)
print(a,b,c,d)
if int(pin) in range(1000,10000) or str(pin)=='0'+ str(pin):
    if int(pin) not in range(1900,2050+1):
        if a!=b and a!=c and a!=d and b!=c and b!=d and c!=d:
            print('OK')
        else:
            print('ERROR')
    else:
        print('ERROR')
else:
    print('ERROR')


