import qrcode
img=qrcode.make("https://www.linkedin.com/in/barathprem12")
img.save("Qrcode.jpg")
print("Successfull Qrcode Created")
