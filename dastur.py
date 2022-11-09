q = input('''Виберыту язику: 
            Ru
            En
            Uz
                        ''')
if q.lower() == 'uz':
    w = input('''Siz o'zbek tilini tanladingiz.Sizga qaysi dasturlash tili haqida ma'lumot kerak.
                python
                javascript
                php
                c++
                            ''')
    if w.lower() == 'python':
        e = input('''Siz python dasturlash tilini tanladingiz.Sizga python haqida qanaqa ma'lumot kerak.
                    1 == Python dasturlash tili haqida ma'lumot:
                    2 == Python beginner darslari(BASIC):
                    3 == Python intermediate darslari(OOP):
                    4 == MySQL:
                    5 == Django:
                                                        ''') 
        if e.lower() == '1':
            print("Siz bu yerda python dasturlash tili haqida ma'lumotga ega bo'lishingiz mumkin.Python dasturlash tili sodda va o'qilishi oddiy bo'lgan dasturlash tili bo'lib u inglizcha so'zlarni qo'llab quvvatlaydi kalit so'zlar o'rnida shuning uchun bu boshqacha ko'rinishga ega")
        elif e.lower() == '2':
            r = input('''Siz pyton beginner darslar bo'limini tanladingiz.Sizga beginner darslardan qaysi mavzusida kiritilgan dastur kerak.
                1-dars -- Data type
                2-dars -- Arifmetik va taqqoslash operatorlar
                3-dars -- Shart operatorlar
                4-dars -- Takrorlanuvchi operatorlar
                5-dars -- Listlar
                6-dars -- Funksiya
                7-dars -- Exception
                                            ''')
            if r == '1':
                print("Siz bu yerda Pythonda data type mavzusida tayyorlangan ishlarni  ko'rishingiz mumkin. ")
                from data_type import *
            elif r =='2':
                print("Siz bu yerda pythonda arifmetik amallar mavzusida tayorlangan ishlarni ko'rishingiz mumkin. ")
                import arifmetik
            elif r == '3':
                print("Siz bu yerda Pythonda shart operatorlari mavzusida tayyorlangan kiritilgan son juft yoki toqligini chiqaruvchi dasturni ko'rishingiz mumkin.")
                import shart
            elif r == '4':
                print("Siz bu yerda Pythonda takrorlanuvchi operatorlari mavzusida tayyorlangan,kiritilgan l va k sonlar orasidagi sonlarni va ularning yig'ndisini chiqaruvchi dasturni ko'rishingiz mumkin.")
                import takrorlanish   #xato borrrrrrrrrr
            elif r == '5':
                print("Siz bu yerda Pythonda Listlar mavzusida tayyorlangan,shart operatorlari bilan birga kiritilgan dugonalar haqidagi dasturni ko'rishingiz mumkin.")
                import listе
            elif r == '6':
                print("Siz bu yerda Pythonda funksiya mavzusi orqali tayyorlangan tug'ilgan yilingiz va maktabni tugatgan yilingizni kiritganda yoshingiz va maktab tugatganingizga necha yil bo'lganini chiqarib beruvchi dasturni ko'rishingiz mumkin.")
                import funksiya
            elif r =='7':
                print("Siz bu yerda Pythonda Exception mavzusi bo'yicha tayyorlangan 2ta sonni bir-biriga bo'lganda kelib chiadiganxatoliklarni ko'rishingiz mumkin.")
                import exception
        elif e.lower() == '3':
            t = input('''Siz python intermediate bo'limini tanladingiz.Sizga Intermediate darslardan qaysi mavzusida kiritilgan dastur kerak.
                1-dars -- OOP
                2-dars -- Inhertiance
                3-dars -- Tuple
                4-dars -- Dictonaries
                5-dars -- Import
                6-dars -- Threading
                                            ''')
            if t == '1':
                print("Siz bu yerda classlarning yozilishini 3 xil ko'rinishini ko'rishingiz mumkin.")
                import oop
            elif t== '2':
                print("Siz bu yerda MaishiyTexnika va Mebel clasi asosida yaratilgan inheritance classlarni ko'rishingiz mumkin. ")
                import inhertiance
            elif t == '3':
                print("Siz bu yerda kompaniya tomonidan tashkil etilgan marosimda kompaniya a'zolarining qaysilari ishtirok etishini ko'rishingiz mumkin.")
                import tuple
            elif t == '4':
                print("Siz bu yerda dictionaries mavzusi aosida tuzilgan kalkulatorni ko'rishingiz mumkin.")
                import dictionaries
            elif t == '5':
                print("Siz bu yerda import time kutubxonasining funksiyalarida tuzilgan dasturni ko'rishingiz mumkin.")
                import importt
            elif t == '6':
                print("Siz bu yerda Threading mavzusida tayyorlangan dasturni ko'rishingiz mumkin.")
                import sriding
        elif e.lower() == '4':
            print("Siz python MySQL bo'limini tanladingiz.Tez orada bu bo'limga ma'lumot joylanadi.")
        elif e.lower() == '5':
            print("Siz python Django bo'limini tanladingiz.Tez orada bu bo'limga ma'lumot joylanadi.")
        else:
            print("Mavjud bo'lmagan bo'limni tanladingiz.")
    elif w.lower() == 'javascript':
        print("Siz Java Script dasurlash tilini tanladingiz .Bizda hozircha Java Script dasturlash tili haqida ma'lumot kiritilmagan.Kutishingizni iltimos qilamiz va tez orada sizga javob qaytaramiz.")                     
    elif w.lower() == 'php':
        print("Siz php dasturlash tilini tanladingiz.Bizda hozircha bu dasturlash tili haqida ma'lumot kiritilmagan.Kutishingizni iltimos qilamiz va tez orada sizga javob qaytaramiz.")                    
    elif w.lower() == 'c++':
        print("Siz c++ dasturlash tilini tanladingiz.Bizda hozircha bu dasturlash tili haqida ma'lumot kiritilmagan.Kutishingizni iltimos qilamiz va tez orada sizga javob qaytaramiz.")
    else:
        print("Siz kiritgan dasturlash tili haqida bizda ma'lumot yetarli emas.")                   
else:
    print("Mavjud bo'lmagan buyruqni tanladingiz.")    