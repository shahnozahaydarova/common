b = input("Ismingizni kiriting: ")
c = input("Failiyangizni kiriting: ")
d = int(input("Kompaniyamizga a'zo bo'lganingizga necha yil bo'ldi: "))
a = (b,c,d)
if d >= 10:
    print("Tabriklatmiz hurmatli ",a[0],a[1],"siz kompaniyamizga a'zo bo'lganingizga",a[2],"yil bo'libdi.Biz sizni kompaniya tomonidan tashkillashtirilgan marosimimizga taklif etamiz.Siz bizning ko'p yillik mijozimiz bo'lganingiz sababli uyerdaqimatbaho sovg'alarga ega bo'lishingiz mumkin. ")
elif d < 10:
    print("Hurmatli",a[0],a[1],"Siz kompaniyamiz tomonidan tashkillashtirilgan marosimda ishtirok etolmaysiz.Chunki kompaniyamizga a'zo bo'lganingizga",d,"yilbo'libdi.",10-d,"yildan keyin ishtirok etishingiz mukin.")
