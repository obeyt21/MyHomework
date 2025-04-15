from PIL import Image

import imageio
import os

#fotoğraf klasörü
image_klasor = 'Gorseller'

image_dosya = sorted([f for f in os.listdir(image_klasor) if f.endswith(('.png', '.jpg', '.jpeg'))])

images = []

for dosya_name in image_dosya:
    dosya_path = os.path.join(image_klasor, dosya_name)
    image = Image.open(dosya_path)
    images.append(image)


cikis_path = "yeni.gif"

images[0].save(
    cikis_path,
    save_all=True,
    append_images=images[1:],
    duration=300,
    loop=0
)

print(f"{cikis_path} başarıyla oluşturuldu")