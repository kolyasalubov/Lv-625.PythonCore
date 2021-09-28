##### QR code (pip install qrcode, pip install Image)

def make_QR_code(data = input(str("Enter your info for QR code: "))):
    import qrcode
    img = qrcode.make(data)
    file_name = input(str("Enter file name for QR code: "))
    img.save(f'C:/Users/kitpes/python/olha/MyGitHub/Lv-625.PythonCore/Lv-625.PythonCore/PROJECT/KitO/{file_name}.png')

first = make_QR_code()