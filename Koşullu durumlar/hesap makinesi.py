print("""*********************

Hesap Makinesi Programi

İşlemler:

1.Toplama işlemi 

2.Çıkarma işlemi

3.Çarpma işlemi 

4.Bölme işlemi






*************************
""")

a = int(input("Birinci sayi:"))
b = int(input("İkinci sayi:"))

işlem = input( "işlemi giriniz:")

if işlem == "1":
    print("{} ile {} toplami = {}".format(a,b,a+b))
elif işlem == "2":
    print("{} ile {} farki = {}".format(a, b, a -b))
elif işlem == "3":
    print("{} ile {} çarpimi = {}".format(a, b, a* b))
elif işlem == "4":
    print("{} ile {} bölümü = {}".format(a, b, a / b))

else:
    print("girdiginiz işlem bulunamadı..")
