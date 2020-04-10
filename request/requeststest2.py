import requests
from io import BytesIO
from PIL import Image

r = requests.get("https://www.elsetge.cat/myimg/f/3-34818_download-free-hd-earth-from-space-desktop-wallpaper.png")

print("Status code:", r.status_code)

image = Image.open(BytesIO(r.content))

path = "./image1.jpg"

print(image.size, image.format, image.mode)

try:
    image.save(path, image.format)
except IOError:
    print("Cannot save it")