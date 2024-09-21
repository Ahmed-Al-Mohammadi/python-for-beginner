def sum():
    x = int(input("first num : "))
    y = int(input("sec num : "))
    z = x + y
    print("sum = ", z)


def avg(a, b, c):
    d = a + b + c
    avrage = d / 3
    return avrage

def info(**kwargs):
    print (kwargs)
    
sum()
print(avg(3, 15, 9))
info (age = 20 , phone = 10 , name = "ahemd" )