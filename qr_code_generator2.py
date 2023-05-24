import qrcode 

url = 'https://youtube.com'
img = qrcode.make(url)
img.save('qrimg3.png')
img.show('qrimg3.png')