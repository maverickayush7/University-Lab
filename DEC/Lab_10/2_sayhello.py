# 2.Write a simple decorator (which greets neighbors only between 7 a.m to 10 p.m) to extend the functionality of say_hello.
# def say_hello():
#     print("Hello!")

from datetime import datetime
now = int(datetime.now().strftime("%H"))

def seventoten(func):
    def inner(now):
        if now >= 7 and now <= 22:
            func(now)
        else: print("No greeting for you")
    return inner

@seventoten
def sayHello(now):
    print("Hello!")

sayHello(now)