import time

a = int(input("Mahalliy vaqtni bilish uchun misolni  bajaring: 1*40*2*10*0*10*2 =="))
if a == 0:
    print("Siz misolni to'g'ri ishladingiz.Mahalliy vaqtni ko'rishngiz mumkin.")
    mv =time.localtime()
    print(mv)
else:
    print("Afsuski misolni xato ishladingiz. 5s kuting va qayta urinib ko'ring.")
    for x in range(5):
        print(x)
        time.sleep(1)
    print("Qayta urinib ko'rishingiz mumkin.")
       