a = input('''Sizga qaysi turdagi mahsulot kerak:        
                1==Mebel  
                2==MaishiyTexnika    
                                              ''')

if a == '1':
    b = input('''Mebellar olamiga xush kelibsiz.Sizga qaysi turdagi mebellar kerak:
                        1==mexmonxona
                        2==oshxona
                                        ''')
    class Mebel:
        def __init(self,tur):
            self.tur = tur
        def __str(self):
            return f"self.tur"

    
    if b == '1':    
        class Mehmonxona(Mebel):
            def __init(self,tur,rang, narx):
                super().__init__(tur)
                self.rang = rang
                self.narx = narx
            def __str(self):
                return f"Turi: {self.tur},Rangi:{self.rang},Narxi:{self.narx}"
        mm1 = Mehmonxona("Mehmonxona","oq","1200$")
        mm2 = Mehmonxona("Mehmonxona","qora","1000$")
        mm3 = Mehmonxona("Mehmonxona","jigarrang","1500$")
        print(mm1)
        print(mm2)
        print(mm3)













# b = input('''Sizga qaysi turdagi MaishiyTexnika kerak: 
#                 1==Konditsioner
#                 2==Gaz plita
#                 3==Kir yuvish mashinasi
#                 4==Muzlatgich''')
# class MaishiyTexnika:
#     def __init__(self,tur,rang,narx):