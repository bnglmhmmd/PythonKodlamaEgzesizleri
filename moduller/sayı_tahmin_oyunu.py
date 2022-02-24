import random
import time


print("""***********************

SAYI TAHMİN OYUNU 

1 ile 40 arasında sayıyı tahmin edin ..


*****************************""")


rastgele_sayı = random.randint(1,40)
tahmin_hakkı=7


while True:
    tahmin = int(input("Tahmininiz:"))

    if(tahmin < rastgele_sayı ):
        print("Tahmin sorgulanıyor..")
        time.sleep(1)
        print("Daha yüksek bir sayı tahmin ediniz.")

        tahmin_hakkı -= 1
    elif(tahmin > rastgele_sayı):
        print("Tahmin sorgulanıyor..")
        time.sleep(1)
        print("Daha düşük bir sayı tahmin ediniz.")

        tahmin_hakkı -= 1
    else:
        print("Tahmin sorgulanıyor..")
        time.sleep(1)
        print("TEBRİKLER DOĞRU TAHMİN .. ")
        break
    if(tahmin_hakkı == 0):
        print("Tahmin hakkınız bitti.")
        print("Sayınız:",rastgele_sayı)

        break


