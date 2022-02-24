print("""********************

HESAP MAKİNESİNE HOŞGELDİNİZ

İŞLEMLER
1.LOGARİTMA HESAPLAMA
2.TRİGONOMETRİK DEGERLER BULMA
3.FAKTÖRİYEL HESAPLAMA

***********************""")


import math
import time




while True:
    işlem = input("İşlemi seçiniz:")

    sayı = float(input("Bir sayı giriniz:"))



    if(işlem == "1"):
        print("işlem yapılıyor..")
        time.sleep(1)
        print("Logaritma:",math.log(sayı))
    elif(işlem == "2"):
        print("işlem yapılıyor..")
        time.sleep(1)
        print("Trigonometrik Hesaplar:",math.sin(sayı),math.cos(sayı),math.tan(sayı))
    elif(işlem == "3"):
        print("işlem yapılıyor..")
        time.sleep(1)
        print("Faktoriyel:",math.factorial(sayı))
    else:
        print("Geçersiz işlem yaptınız !!")



