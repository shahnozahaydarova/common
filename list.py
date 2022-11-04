list = ["Shahnoza","Gulhahor","Gulxayo","Umida",["Haydarova","Ergasheva","Xalilova","Xamroyeva"],[19,19,21,20]]
ll = input('''Sizga dugonalar haqidagi qaysi ma'lumot kerak:  
        ismlari
        familiyalari
        yoshlari
                                ''')
if ll == 'ismlari':
    print(list[0],list[1],list[2],list[3])
elif ll == 'familiyalari':
    print(list[4][0],list[4][1],list[4][2],list[4][3])
elif ll == 'yoshlari':
    print(list[5][0],list[5][1],list[5][2],list[5][3]) 