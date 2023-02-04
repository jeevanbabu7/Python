from pyqrcode import create
import png
from PIL import Image
link = input("Enter data to generate QRcode : ")
qrcode = create(link)
qrcode.png("QRcode.png",scale = 10)
Image.open("Qrcode.png")