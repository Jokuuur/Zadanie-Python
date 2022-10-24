# # #Zad.1
# n = int(input("Podaj aktualny dzień listopada : "))
# if(n>30):
#     print("Listopad nie ma 31+ dni")
# for i in range(n,31):
#     print(i , 'Listopada 2022')
# #Zad.2
# n = (int(input("Podaj n : ")))
# if(n%2 == 1):
#     for i in range(1):
#         print(n**2)
# if(n%2 == 0 ):
#     print("Podano liczbe parzystą ")
# #Zad.3
# for i in range(1000,10000):
#     if i % 379 == 0:
#         print(i)
# #Zad.4
# for i in range(1000,10000):
#     if(i%5 == 0 or i%6 == 0 or i%11 == 0 ):
#         print(i)
#         print("Tak więc wypisało wszystkie liczby w przedziale 1000 - 10000 podzielne przez 4,5 bądź 11")
# #Zad.5
# n = int(input("Podaj ilość liczb : "))
# n2 = []
# for i in range(0,n):
#     temp = int(input(f"Podaj {i+1} liczbę: "))
#     n2.append(temp)
# print(f"Suma: {sum(n2)}")
# # Zad.6
# n = int(input("Podaj liczby: "))
# suma = 0
# for i in range(2,(n*2)+2,+2):
#     suma += i
# print(f"Wynik: {suma}")

# #Zad.7
# n = int(input("Podaj liczby: "))
# suma = 0
# for i in range(11,(n*2)+11,+2):
#     suma += i
# print(f"Wynik: {suma}")

# #Zad.9
# n = int(input("Podaj ilość liczb: "))
# x = 21
# suma = 0
# for i in range(0,n+1):
#     for a in range(0,i,x):
#         print(x)
#         suma += x
#         x += 100
# print(f"Wynik: {suma}")

# #Zad.10
# from cmath import sqrt
# for i in range(1,1000):
#     if i - (i//10)*10 == sqrt(i):
#         print(i)
#     if i - (i//100)*100 == sqrt(i):
#         print(i)