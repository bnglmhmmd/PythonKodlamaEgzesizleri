def asal_mi(sayı):
    i= 2
    while(i < sayı ):
        if(sayı % i == 0):
            return False
        i +=1
    return True
def asal_genarator():
    i = 2
    while True:
        if(asal_mi(i)):
            yield i
        i+=1

for sayı in asal_genarator():
    if(sayı > 1000):
        break
    print(sayı)



