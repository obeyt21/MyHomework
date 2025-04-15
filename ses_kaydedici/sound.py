import sounddevice as sd

from scipy.io.wavfile import write

fre = 44100
sure = 5

print("Kayıt Başlıyor...")

ses = sd.rec(int(sure *fre), samplerate=fre, channels=1)
sd.wait()
print("Kayıt Tamamlandı.")

write("YeniKayit.wav", fre, ses)

print("ses dosyası Kaydedildi")