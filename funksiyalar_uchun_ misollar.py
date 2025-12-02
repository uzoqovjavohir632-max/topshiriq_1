# def funksiya():
#     print("Hello World")
# funksiya()    


# def ismim():
#     print("JAVOHIR")
# ismim()    


# def funksiya():
#  son= float(input("sonni kiriting:  "))
#  print ("siz kiritgan son: " ,son) 
# funksiya() 


# def funksiya():
#     son = float(input("Sonni kiriting: "))

#     if son > 0:
#         print("Bu son musbat.")
#     elif son < 0:
#         print("Bu son manfiy.")
#     else:
#         print("Bu son 0 ga teng.")

# funksiya()


# def funksiya():
#  a = float(input(" 1-sonni kiriting:  ") )
#  b = float(input(" 2-sonni kiriting:  ") )
#  c=a+b 
#  print ("yigindi", c , "ga teng")
# funksiya()


# def funksiya():
#  a = float(input(" 1-sonni kiriting:  ") )
#  b = float(input(" 2-sonni kiriting:  ") )
#  c=a+b 
#  print ("yigindi", c , "ga teng")
# funksiya()

# def funksiya():
#  a = float(input(" 1-sonni kiriting:  ") )
#  b = float(input(" 2-sonni kiriting:  ") )
#  c=a+b 
#  print ("yigindi", c , "ga teng")
# funksiya()


# def funksiya():
#  a = float(input(" 1-sonni kiriting:  ") )
#  b = float(input(" 2-sonni kiriting:  ") )
#  c=a+b 
#  print ("yigindi", c , "ga teng")
# funksiya()

# def funksiya():
#      a = float(input(" 1-sonni kiriting:  ") )
#      b = float(input(" 2-sonni kiriting:  ") )
#      c=a-b 
#      print ("ayirma", c , "ga teng")
# funksiya()


# def matn():
#     n= input("matnni kiriting: ")
#     print("matn uzunligi" ,len(n))
# matn()    


# def funksiya():
#     n=int(input("sonni kiriting:  "))
#     if n % 2 == 0 :
#       print("bu son juft")      
#     else:
#        print("bu son juft emas")  
# funksiya()       


# def funksiya():
#     n=int(input("sonni kiriting:  "))
#     if n % 2 == 1 :
#       print("bu son toq")      
#     else:
#        print("bu son toq emas")  
# funksiya()   
# def ism():
#    ism=input("ismni kiriting:  ")
#    print("Xush kelipsiz", ism )
# ism()



# def funksiya():
#     a=int(input(" 1-sonni kiriting:  "))
#     b=int(input(" 2-sonni kiriting:  "))
#     c=int(input(" 3-sonni kiriting:  "))
#     d=(a+b+c)/3
#     print("bu sonlarning o'rta qiymati: " ,d)
# funksiya()


# def funksiya():
#     son = float(input("Sonni kiriting: "))
#     d = son ** 2
#     print("sonning kvadrati:  " , d)

# funksiya()


# def funksiya():
#     son = float(input("Sonni kiriting: "))
#     d = son ** 3
#     print("sonning kubi :  " , d)

# funksiya()


# def funksiya():

#     a=int(input(" 1-sonni kiriting:  "))
#     b=int(input(" 2-sonni kiriting:  "))
    
#     if a > b:
#         print(a , " soni   katta")
#     elif b > a:
#         print(b,  " soni  katta")
#     else:
#         print("Ikkala son teng.")
# funksiya()        


# def funksiya():

#      t=float(input(" haroratni selsiyda kiriting: "))
    
#      f = (t * 9/5) + 32    
#      print (t ,"C=", f , "F" )    
# funksiya ()   


# def funksiya():
#     matn = input("Matn kiriting: ")
#     teskari = matn[::-1]
#     print("Teskari matn:", teskari)

# funksiya()


# def birinchi_harf():
#     matn= input("matnni kiriting:  ")
#     if len(matn) > 0:
#        print("Matnning birinchi harfi:", matn[0])
#     else:
#         print("Matn bo'sh!")

# birinchi_harf()


# def funksiya (son):

#     for i in range (1 , 11 ):
#         v = son * i
#         print(f"{son} x {i} = {v}")

# son = int(input("sonni kiriting  "))
# funksiya(son)


# def funksiya(son):
#     natija =  son **2 
#     return natija
# n= int (input("n sonni kiriting "))

# natija = funksiya(n) 
# print ("sonning kvadrati", natija)


# def yigindi ():
#     a=int(input("a sonni kiriting : "))
#     b=int(input("b sonni kiriting : "))
#     return a+b 
    # natija = yigindi() 
# print ( "yigindi =", natija) 
    

# def juft_yoki_toq ():
#     n=int(input("n sonni kiriting "))
#     if n % 2 == 0 :
#        return "juft"
#     else:
#         return "toq"
# natija = juft_yoki_toq ()
# print ( natija)


# def funksiya():
#     a = float(input("1-sonni kiriting: "))
#     b = float(input("2-sonni kiriting: "))
#     c = float(input("3-sonni kiriting: "))

#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c

# natija = funksiya()
# print("Eng katta son =", natija)


# def musbat():
#     n=int(input("sonni kiriting:  "))
#     if n>0 :
#         return "true "
#     else:
#         return "False"
# natija =  musbat()
# print(natija)

# def matn_uzunligi(): 
#     matn = input ("matnni kiriting :  ")
#     return len(matn )
# natija= matn_uzunligi()
# print ( "matn uzunligi= " , natija)


# def eng_kichik_top():
#     royxat = list(map(int, input("Sonlarni bo'sh joy bilan kiriting: ").split()))
#     return min(royxat)

# natija = eng_kichik_top()
# print("Eng kichik son =", natija)


# def eng_katta_top():
#     royxat = list(map(int, input("Sonlarni bo'sh joy bilan kiriting: ").split()))
#     return max(royxat)

# natija = eng_katta_top()
# print("Eng katta son =", natija)


# def faktorial():
#     n=int(input("sonni kiriting:  "))
#     s=1 
#     for i in range (1 , n+1):
#        s= s*i 
#     return   s
# natija = faktorial()
# print (  natija)


# def soliq( ):
#     narx= int(input("narxni kiriting:  "))
#     soliqli_narx = narx * 1.12
#     return soliqli_narx 
# nimadir = soliq( )
# print ( "soliq qoshib hisoblangan narx =", nimadir)


# def yil (): 
#     yil = int(input("yilni kiriting:  "))
#     if yil % 4 == 0 :
#         return "kabisa yili "
#     else:
#         return "kabisa yili emas"
# natija = yil()
# print ("kiritilgan yil " , natija )    



# def kod():
#     parol= input("parolni kiriting:  ")
#     if len( parol) > 8 :
#         return "parol kuchli"
#     else :
#         return "parol kuchli emas"
# parollar = kod()
# print ( "siz kiritgan " , parollar)



def sanash(matn):
    son = matn.count("a")
    return son

matn = input("Matn kiriting: ")
print("a harflar soni:", sanash(matn))

