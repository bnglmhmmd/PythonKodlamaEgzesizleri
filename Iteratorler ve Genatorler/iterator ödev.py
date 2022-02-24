class Kareler():
    def __init__(self,max):
        self.max = max
        self.sayı = 1

    def __iter__(self):
        return self

    def __next__(self):
        if (self.sayı <= self.max):
            sonuc =  self.sayı ** 2
            self.sayı += 1
            return sonuc
        else:
            self.sayı = 1
            raise StopIteration

kareler = Kareler(6)

for i in kareler:
    print(i)