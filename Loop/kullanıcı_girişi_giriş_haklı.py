print("""****************

KUULLANICI GİRİŞİ 
********************""")


sys_kullanıcı_adı = "muhammed"
sys_parola = "123456"

giriş_hakkı = 3

while True:
    kullanıcı_adı = input("Kullanıcı Adı:")
    parola = input("Parola:")

    if(sys_kullanıcı_adı != kullanıcı_adı and sys_parola == parola):
        print("Kulanıcı Adınızı Yanlış Girdiniz.")
        giriş_hakkı -=1
    elif(sys_kullanıcı_adı == kullanıcı_adı and sys_parola != parola ):
        print("Parolanızı yanlış girdiniz.")
        giriş_hakkı -=1
    elif(sys_kullanıcı_adı != kullanıcı_adı and sys_parola != parola):
        print("Kullanıcı adı ve parola yanlış.")
    else:
        print("Sisteme Başarılı Giriş Yapıldı.")
        break
    if(giriş_hakkı == 0):
         print("Giriş Hakkınız Bitmiştir...")
         break
