import pyqrcode
from pyqrcode import QRCode

url = 'https://youtube.com'

path = pyqrcode.create(url)
path.svg('qrimg.svg', scale = 10)
