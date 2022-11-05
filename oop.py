class Odam:
    def __init__(self,ism,familiya,yosh):
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh
o1 = Odam("Shukrona","Turobova",1)
o2 = Odam("Abdulaziz","Jabborova",3)
print("Ismi: ",o1.ism,"Familiyasi: ",o1.familiya,"Yoshi: ",o1.yosh)
print("Ismi: ",o2.ism,"FAmiliyasi: ",o2.familiya,"Yoshi",o2.yosh,)


class Hayvon:
    def __init__(self,tur,rang,vazn):
        self.tur = tur
        self.rang = rang
        self.vazn = vazn
    def __str__(self):
        return f"Turi :{self.tur} ,Rangi: {self.rang},Vazni: {self.vazn}"
h1 = Hayvon("ayiq","oq","200kg")
h2 = Hayvon("Panda","oq-qora","150kg")
print(h1)
print(h2)

class Gul:
    def __init__(self,tur,rang,uzunlik):
        self.tur = tur
        self.rang = rang
        self.uzunlik = uzunlik
    def chiqarish(self):
        print( "Turi: ",self.tur,"Rangi: ",self.rang,"Uzunligi: ",self.uzunlik)

g1 = Gul("Atirgul","qizil","70 sm")
g2 = Gul("Lola","sariq","50 sm")
g1.chiqarish()
g2.chiqarish()



print("Odam classi print orqali chiqarilgan.")
print("Hayvon classi str orqali chiqarilgan.")
print("Gul classi yangi def yaratib chiqarilgan.")
