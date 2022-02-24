def ekstra(fonk):

    def wrapper(sayılar):
        çift_sayılar = 0
        çiftlerin_toplamı = 0
        tek_sayılar = 0
        teklerin_toplamı = 0
        for sayı in sayılar:

            if(sayı % 2 == 0 ):
                çiftlerin_toplamı +=sayı
                çift_sayılar +=1
            else:
                teklerin_toplamı += sayı
                tek_sayılar +=1
        print("Teklerin Ortalaması:", teklerin_toplamı/tek_sayılar)
        print("Çiftlerin Ortalamsı:", çiftlerin_toplamı/çift_sayılar)
        fonk(sayılar)
    return wrapper












@ekstra
def ortalama_bul(sayılar):
    toplam = 0
    for sayı in sayılar:
        toplam += sayı
    print("Genel Ortalama: ",toplam/len(sayılar))
ortalama_bul([25,23,56,48,156,7894,15,76])


