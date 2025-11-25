#2 Massivdagi eng katta elementni topish

# sonlar = [1, 2, 3, 4, 9]
# n = 5

# eng_kattasi = sonlar[0]

# for i in range(1, n):
#     if sonlar[i] > eng_kattasi :
#         eng_kattasi = sonlar[i]

# print("Eng katta element:", eng_kattasi)

## 3 massivdagi eng kichik elementni topish
# sonlar = [2, 4, 8, 34, 5]
# eng_kichik  = sonlar[0]
# n = 5
# for i in range (1, n) :
#   if sonlar[i] < eng_kichik :
#     eng_kichik = sonlar[i]
# print ("eng kichig element:" , eng_kichik ) 

## 4 Massivdagi juft sonlar sonini sanab beruvchi 
# my_list = [3, 5, 8, 56, 78, 89, 790]

# juft_sonlar_soni = 0
# for son in my_list :
#     if  son %2 ==0 :
#      juft_sonlar_soni+= 1
# print ("massivda ",juft_sonlar_soni ,"ta  juft element bor")

## 5 massivdagi elementlar yig'indisini topib beruvchi
# list = [55, 90, 8,78 , 85, 46 ]
# yigindi = 0
# for son in list :
#   yigindi+=son   
# print("Elementlar yig'indisi:", yigindi)


## 6 Massivdagi elementlarni teskari tartibda chiqarip beruvchi

# my_list = [4, 5, 6, 7, 45, 67, 68]
# print (my_list [::-1])

## 7 Massivdagi eng katta va eng kichik elementlar indeksini topuvchi
# massiv = [3, 5, 65, 46, 78, 98]
# eng_kichik_qiymat= massiv[0]
# eng_kichik_indeks=0

# eng_katta_qiymat= massiv[0]
# eng_kata_indeks= 0

# n=len(massiv)

# for i in range(1, n, ):
#    if massiv[i] > eng_katta_qiymat :
#         eng_katta_qiymat = massiv[i]
#         eng_katta_indeks= i
#    if massiv[i]< eng_kichik_qiymat :
#       eng_kichik_qiymat = massiv[i]   
#       eng_katta_indeks = i


# print("Eng kichik element:", eng_kichik_qiymat, ", indeksi:", eng_kichik_indeks)
#print("Eng katta element:", eng_katta_qiymat, ", indeksi:", eng_katta_indeks)


##  8  MASSIV ichidagi elementlarni o'rnini almashtirish
# sonlar = [2, 4, 8, 34, 5]

# sonlar[1], sonlar[3] = sonlar[3], sonlar[1]

# print(sonlar)

## 9 Faqat toq indeksdagi elementlarni cjhiqaruvchi
# massiv = [4, 5, 7, 34, 56, 76, 89]
# for i in range(len(massiv) ) :
#  if i % 2 == 1 :
#   print(massiv[i])

## 10 massivni tartiblovchi kod
# massiv = [34, 56, 23, 432, 543, 593, ]
# massiv.sort ()
# print(massiv) 

## 11 Massivdagi takrorlangan elementlarni topuvchi









## 12 massivda berilgan son nechinchi indexda ekanini topuvchi
# massiv = [2, 43, 98, 340, 576]
# qidiriladigan = int(input("elementni kiriting:  ")) 
# if qidiriladigan in massiv:
#     indeks = massiv.index(qidiriladigan)
#     print("Element indeksi:", indeks)
# else:
#     print("Bu element ushbu massivda mavjud emas  ")

## 13 Massivda faqat manfiy sonlarni alohida massivga ajratuvchi
# massiv = [-3, 78, -65, -54, 35, 65, -89]
# manfiy_elementlar=[]
# for i in massiv :
#   if i<0 :
#     manfiy_elementlar.append(i)
# print ("manfiy sonlar massivi " ,manfiy_elementlar  )       

## 14 Massivdagi har bir elementni 2 martadan oshiruvchi
# massiv = [45, 67, 456, 4, 67, 89]

# yangi_massiv = []
# for i in massiv :
#     yangi_massiv.append (i * 2)

# print("2 marta oshirilgan massiv: ", yangi_massiv)

## 15 ikkita massivni birlashtirib bitta massiv qiluvchi
# massiv_1 = [3, 5, 56, 65, 34, 23]
# massiv_2 = [43, 78, 908, 90, 98, 78 ] 
# massiv_1. extend (massiv_2)
# print (massiv_1)

arr = [2, 5, 3, 2, 8, 5, 2]
n = len(arr)

print("Takrorlangan elementlar:")

for i in range(n):
    counted = False
    for k in range(i):
        if arr[k] == arr[i]:
            counted = True
            break

    if counted:
        continue

    count = 0
    for j in range(n):
        if arr[i] == arr[j]:
            count = count+ 1

    if count > 1:
        print(f"{arr[i]} → {count} marta")