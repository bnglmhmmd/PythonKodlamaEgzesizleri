print("""******************
Kullanıcı Girişi
******************""")

sys_kullanıcı_adı = "tacuman"
sys_parola = "123456"

kullanıcı_adı = input("Kullanıcı Adı:")
parola = input("Parola:")


if(sys_kullanıcı_adı != kullanıcı_adı and sys_parola == parola ):
    print("Kullanıcı Adınızı Yanlış Girdiniz..")
elif(sys_kullanıcı_adı ==kullanıcı_adı and sys_parola != parola ):
    print("Parolanızı Yanlış Girdiniz..")
elif(sys_kullanıcı_adı != kullanıcı_adı and sys_parola != parola):
    print("Kullanıcı Adınızı ve Parolanızı Yanlış girdiniz..")
else:
    print("Başarılı giriş.")





