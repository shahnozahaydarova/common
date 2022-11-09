a = int(input("1-sonni kiriting: "))
b = int(input("2-sonni kiriting: "))
c = 0

# print("Whileda birinchi va ikkinchi sonlar orasigadi sonlarni chiqarish.")
# while a < b:
#     a += 1
#     print(a)
# while a > b:
#     b += 1
#     print(b)
# print("Forda birinchi va ikkinchi sonlar orasigadi sonlarni chiqarish.")
# for x in range(a,b):
#     print(x)
# for x in range(b,a):
#     print(x)



while a < b:
    a += 1
    c += a
while b < a:
    b += 1
    c += b
print("Yig'indi whileda hisoblandi va u",c,"ga teng.")



for x in range(a,b):
    c += x
for x in range(b,a):
    c += x
print("Yig'indi forda hisoblandi va u "+str(c)+"ga teng.")