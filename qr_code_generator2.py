import qrcode 

img = qrcode.make('https://youtube.com')
img.save('qrimg1.png')
img.show('qrimg1.png')