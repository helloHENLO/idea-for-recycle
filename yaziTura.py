import random
def yaziTura(sayi):
    secenek="yazi","tura"

    sonuc=""
    for i in range(sayi):
        sonuc = sonuc + random.choice(secenek)


        
    return sonuc