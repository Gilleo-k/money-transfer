x=0  # global

def hello():
    print("hello Serge")
    print(x)

def custormHello(name,age):
    x=10  # local
    print(f"hello {name} and you are {age} old ")

def addition(x,y):
    print(x+y)
    
def substraction(x,y):
    return x-y 

if __name__=='__main__':
    
    hello()
    a=substraction(2,5)
    print(a)