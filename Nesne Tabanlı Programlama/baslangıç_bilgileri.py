class ögrenci():
    def __init__(self,isim,soyisim,numara,sınıf,dersler):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.sınıf = sınıf
        self.dersler = dersler
    def bilgileri_göster(self):
        print("""
        Öğrenci bilgileri:
        
        İsim = {}
        
        Soyisim = {}
        
        Numara = {}
        
        Sınıf = {}
        
        Dersler = {}
        
        """.format(self.isim,self.soyisim,self.numara,self.sınıf,self.dersler))

        ögrenci = ögrenci("Adem","Kaya",34243,"Teknoloji sınıfı",["Analitik","Yazılım ","Elektronik","Sensorler"])





