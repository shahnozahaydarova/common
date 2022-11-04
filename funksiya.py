yil = int(input("Tug'ilgan yilingizni kiriting: "))
maktab = int(input("Maktabni bitirgan yilingizni yozing: "))
def dastur():
    if yil < 2022:
        print("Kiritgan ma'lumotlaringizga qaraganda siz hozirda",2022-yil,"yoshdasiz va maktabni tamomlaganingizga ",2022-maktab,"yil bo'ldi.")
    else:
        print("Tug'ilgan yilingizni noto'g'ri kiritdingiz,kuting va qayta urinib ko'ring.")
        for x in range(5):
            print(x)
dastur()