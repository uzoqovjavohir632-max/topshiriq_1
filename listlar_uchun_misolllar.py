# def orta(a, b, c):
#     print("O'rtacha qiymat:", (a + b + c) / 3)

# a = float(input("1-sonni kiriting: "))
# b = float(input("2-sonni kiriting: "))
# c = float(input("3-sonni kiriting: "))

# orta(a, b, c)



# def kvadrad(a ):
#     print("sonning kvadrati = ", a**2)
# a = float(input(" a sonni kiriting: "))
# kvadrad(a)


# def kub(a):
#     print("sonning kvadrati = ", a**3)
# a = float(input(" a sonni kiriting: "))
# kub(a)



# def katta(a, b):
#     if a > b:
#         print("Katta son:", a)
#     elif b > a:
#         print("Katta son:", b)
#     else:
#         print("Ikkala son teng")

# a = float(input("1-sonni kiriting: "))
# b = float(input("2-sonni kiriting: "))

# katta(a, b)


# def farangeyt ( t ):
#     harorat = (t * 9/5) + 32    
#     print("farangeyt boyicha harorat: " , harorat)  
# selsiy = float(input("haroratni kiriting:  "))
# farangeyt(selsiy)

# def jadval(n):
#     for i in range(1, 10+1):
#         print(n, "*", i, "=", n * i)

# son = int(input("Sonni kiriting: "))
# jadval(son)


# def kvadrat(x):
#     return x ** 2

# son = float(input("Sonni kiriting: "))
# natija = kvadrat(son)
# print("Kvadrati:", natija)


# def yigindi( a, b):
#     c= a+ b 
#     return c 
# a= float(input("1-sonni kiriting:  "))
# b= float(input("2-sonni kiriting:  "))
# natija = yigindi(a, b)
# print("Yig'indi:", natija)


# def juft_toqlikka_tekshirish (son):
#     if son % 2 == 0 :
#           return "juft"
#     else :
#          return  "toq"

# n= int (input(" sonni kiriting:  "))

# victus= juft_toqlikka_tekshirish (n )
# print ("kiritilgan son" , victus)


def kattasi(a , b , c ):
    katta =a 
    if b > katta :
        katta = b 
    if c > katta :
        katta = c
    return katta 
x = int(input('1- sonni kiriting:  '))
y = int(input('2- sonni kiriting:  '))
z = int(input('3- sonni kiriting:  '))
natija = kattasi(x , y , z )
print ('eng katta son:  ' , natija)