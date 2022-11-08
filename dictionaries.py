a = int(input("1-son: "))
b = int(input("2-son: "))
amal =input("Amalni tanlang: ")
kalk = {
    "qoshish" : a+b,
    "ayirish" : a-b,
    "kopaytirish" : a*b,
    "bolish" : a/b
}
if amal == '+':
    print("Natija: ",kalk["qoshish"])
elif amal == '-':
    print("Natija: ",kalk["ayirish"])
elif amal == '*':
    print("Natija: ",kalk["kopaytirish"])
elif amal == '/':
    print("Natija: ",kalk["bolish"])
else:
    print("Siz noto'g'ri amal kiritdingiz.Kuting va qayta urinib ko'ring.")
    for x in range(6):
        print(x)
