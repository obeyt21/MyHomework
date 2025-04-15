import time

def geri_sayim(saniye):
    while saniye>0:
        print(f"Kalan Süre: {saniye} saniye")
        time.sleep(1)
        saniye -=1
    print("süre bitti")
while True:
    try:
        sure = int(input("Lütfen Süreyi girin: "))
        geri_sayim(sure)
        break
    except ValueError:
         print("Sadece Sayı girin")