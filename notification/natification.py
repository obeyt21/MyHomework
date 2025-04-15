import time

from plyer import  notification

while True:
    notification.notify(
        title ="💧 Su İçmeyi Unutma",
        message = "Böbrek sağlığın için kalk bir bardak su iç hemen 💦",
        app_name="Su Hatırlatıcısı",
        timeout=10
    )
    time.sleep(120*120)

#iki saate bir su içe hatırlatma bildirimi verir

