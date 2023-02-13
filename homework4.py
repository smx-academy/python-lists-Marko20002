#1
# lista=[]
# zbir=0
# for i in range (0,10):
#     x=int (input())
#     lista.append(x)
# for i in range (0,10):
#     zbir+=lista[i]
# print(zbir)

#2
# lista=[]
# zbir=0
# y=int(input("vnesete kolku broevi sakate da stavite vo listata"))
# for i in range (0,y):
#     x=int (input())
#     lista.append(x)
# print(max(lista))
#3
# lista=[]
# zbir=0
# y=int(input("vnesete kolku broevi sakate da stavite vo listata "))
# for i in range (0,y):
#     x=int (input())
#     lista.append(x)
# print(lista)
# while True:

#     print("napisete koi elementi sakate da se izbirsat od listata dokolku ste zavrseni napiste NE")
#     tmp=str(input())
    
#     if str ==  "NE":
#         break
#     elif int(tmp) in lista:
#         x=int(tmp)
#         lista.remove(x)
#     elif not lista:
#         print("nemate vekje elemtti vo listata")
#         break
#     else:
#         print("nema takoj element")
#         continue
#     print(lista)
# #4
# x=int (input())
# lista=[]
# for i in range (0,x):
#     name=str(input())
#     lista.append(name)
# print(max(lista,key=len))

#5
# x=int (input())
# lista=[]
# name_s=str
# for i in range (0,x):
#     name=str(input())
#     lista.append(name)

# lista1 = []
# lista1.append(sorted(list, key=len)[-2])
# print(lista1)

#6
korisnik = 500
lista1 =[] 
lista2 =[]
prasanje="NE"
while (prasanje=="NE"):
    proizvodi = str(input("vnesete koj proivod sakate da kupitee? "))
    cena = int(input("negova cena "))
    print("dali sakate da platite?(NE ako sakate da prodolzite)")
    prasanje=str(input())
    lista1.append(cena)
    lista2.append(proizvodi)
zbir=0
for price in lista1:
    zbir+=price
print(lista2)
print(korisnik-zbir,"Kusur: ")