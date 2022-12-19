'''checking whether the input is a prime or not
by for loop'''

'''a = int(input())
for i in range(2,a):
    if a%i==0:
        print("not prime")
        break
else:
    print("prime")'''


#by while loop
a = int(input())
x=2
while x<a:
    if a%x==0:
        print("not prime")
        break
    x=x+1    
else:
    print("prime")    