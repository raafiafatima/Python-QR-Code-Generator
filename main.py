import qrcode
from customtkinter import * 
from PIL import Image

def QR_code(text):
    if text == '':
        CTkLabel(win, text = 'Enter text', text_color = 'white', font = ('Arial', 30, 'bold'), bg_color = '#B4D9E7').place(x = 130, y = 200)
        return
    qr = qrcode.QRCode(
        version = 1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,  
        box_size=10,  
        border=4,
    )
    qr.add_data(text)
    qr.make(fit = True)
    img = qr.make_image(fill_color='skyblue', back_color='white')  
    img.save("QR_CODE_APP/qr_img.png")  
    img = CTkImage(dark_image = Image.open("QR_CODE_APP/qr_img.png"), size=(300, 300))
    CTkLabel(win, image = img, text = '').place(x = 50, y = 80)

set_default_color_theme("D:\\raafia fatima\\Python (1st Semester)\\QR_CODE_APP\\breeze.json")

set_appearance_mode('light')

win = CTk()
win.geometry("400x430")
win.title('QR Code Generator')

entry = CTkEntry(win, width = 260, height = 30)
entry.place(x = 25, y = 20)

frame = CTkFrame(win, width = 350, height = 350)
frame.place(x = 25, y = 60)

btn = CTkButton(win, width=80, height = 30, text = 'Generate', command = lambda: QR_code(entry.get()))
btn.place(x = 295, y = 20)

win.mainloop()
