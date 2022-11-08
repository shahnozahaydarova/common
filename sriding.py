import threading
import time

i = input("Ismingizni kiriting: ")
def ism():
    for x in range(30):
        time.sleep(0.3)
        print(i)
        


f = input("Familiyangizni kiriting: ")
def familiya():
    for x in range(30):
        time.sleep(0.3)
        print(f)

o = input("Otangizning ismini kiriting:")

j = input("Jinsingizni kiriting: ")
def jins():
    if j == 'ayol':
        for x in range(30):
            time.sleep(0.3)
            print(o,"qizi")
    elif j == 'erkak':
        for x in range(30):
            time.sleep(0.3)
            print(o,"o'g'li")

t1 = threading.Thread(target=ism)
t2 = threading.Thread(target=familiya)
t3 = threading.Thread(target=jins)
t1.start()
t2.start()
t3.start()