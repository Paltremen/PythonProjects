
def count(firstval=2, step=1):
        x = firstval
        while 1:
            yield x
            x += step

for num in count():
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
       print (num)