print("""******************************************

ATM MAKİNESİNE HOŞGELDİNİZ.

İşlemler;

1. Bakiye Sorgulama

2.Para Yatırma

3.Para Çekme

Programdan çıkmak için 'q' ya basınız.
*****************************************""")

bakiye = 1000

while True:
    işlem = input("İşlemi seçiniz:")

    if(işlem == 'q' ):
        print("yine bekleriz..")
        break
    elif(işlem == "1"):
        print("Bakiyeniz {} tl dir".format(bakiye))
    elif(işlem == "2"):
        miktar = int(input("miktarı giriniz:"))

        bakiye += miktar
    elif(işlem == "3"):
        miktar = int(input("miktarı giriniz:"))
        if(bakiye - miktar < 0 ):
            print("istenilen tutar bakiyeden fazladır.")
            continue
        bakiye -= miktar
    else:
        print("Gecersiz işlem..")



















