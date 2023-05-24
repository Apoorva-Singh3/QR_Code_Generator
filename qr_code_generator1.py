import pyqrcode
from pyqrcode import QRCode

url = 'https://youtube.com'

path = pyqrcode.create(url)
path.png('qrimg2.png', scale = 10)
