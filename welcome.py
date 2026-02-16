
import qrcode
import os
print(os.getcwd())


project_url = "C:\Users\khoul\welcome.html"  

qr = qrcode.QRCode(
    version=1,  
    error_correction=qrcode.constants.ERROR_CORRECT_H,  
    border=4,    
)
qr.add_data(project_url)
qr.make(fit=True)

img = qr.make_image(fill_color="cyan", back_color="black")  
img.save("project_qrcode.png")


print("QR Code تم إنشاؤه وحفظه باسم project_qrcode.png")
