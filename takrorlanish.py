l = int(input("l sonni kiriting: "))
k = int(input("k sonni kiriting: "))
j = 0
# while l < k:
#     l += 1
#     print(l)
# while l > k:
#     k += 1
#     print(k)
# for x in range(l,k):
#     print(x)
# for x in range(k,l):
#     print(x)


while l < k:
    l += 1
    j += l
print("Yig'indi whileda hisoblandi va u",j,"ga teng.")

while k < l:
    k += 1
    j += k
print("Yig'indi whileda hisoblandi va u",j,"ga teng.")

for x in range(l,k):
    j += x
    print("Yig'indi forda hisoblandi va u",j,"ga teng.")
for x in range(k,l):
    j += x
    print("Yig'indi forda hisoblandi va u",j,"ga teng.")