try:
    a = int(input("1-son: "))
    b = int(input("2-son: "))
    print(a/b)
except ValueError:
    print("Siz int qiymat o'rniga str qiymat kiritdingiz.")
except ZeroDivisionError:
    print("Sonni nolga bo'lib bo'lmaydi bu qoidani hech qachon unutmang.")
except NameError:
    print("Siz kiritgan fayl nomi topilmadi.")
except TypeError:
    print("Tur xatoligi bor.")
except IndentationError:
    print("Kod joylashuvidagi xatolik.")
except SyntaxError:
    print("Sintaksis xatolik mavjud.")