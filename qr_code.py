import qrcode as qr

img = qr.make('https://www.linkedin.com/in/saumya-gupta-009438373/')
img.save('linkedin_qr.png')
print('qr code generated seccessfully')
