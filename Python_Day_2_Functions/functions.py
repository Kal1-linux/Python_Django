def demo():
    print("hello this is basic functions")
def add(no1,no2):
    print(no1+no2)

def sub(no1=100,no2=50):
    print(no1-no2)
def mul(n1=100,n2=5):
    return n1*n2
def arbitary(*data):
    print(len(data))
    print(data[1])
    print(data[2])
    print(data[3])
    print(data[4])

def listfunc(data):
    print(len(data))
    print(data[0])
    print(data[1])
    print(data[2])
    print(data[3])
    print(data[4])

def kwrg(**data):
    print(data)
    print(data["id"])
    print(data["name"])
    print(data["email"])

def nullfunc():
    pass


demo()
add(100,100)
sub(no1=200)
print(mul())
arbitary(1,"hello","python","ahm",380006)
listfunc([1,"hello","python","ahm",380006])
kwrg(id=1,name="hitesh",email="xyz@gmil.com")
nullfunc()