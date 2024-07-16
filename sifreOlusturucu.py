import random 

def sifreOlusturucu(sayi):
    
    karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    
    sifre = ""


    for i in range(sayi):
        sifre = sifre + random.choice(karakterler)


    return sifre

tokenn=""