##### QR code (pip install pyzbar, pip install Image)

def read_QR_code(myqrcode = input(str("Enter path to QR code with file name: "))):
    from pyzbar.pyzbar import decode
    from PIL import Image
    img = Image.open(myqrcode)
    result = decode(img)
    print(result)

# C:/Users/kitpes/python/olha/MyGitHub/Lv-625.PythonCore/Lv-625.PythonCore/PROJECT/KitO/Olga.png
second_step = read_QR_code()

# [Decoded(data=b'Olga Kit, Kyiv, Ukraine', type='QRCODE', 
# rect=Rect(left=42, top=42, width=247, height=247), 
# polygon=[Point(x=42, y=42), Point(x=42, y=287), Point(x=289, y=289), Point(x=287, y=42)])]