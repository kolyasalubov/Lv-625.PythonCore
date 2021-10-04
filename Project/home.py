from tkinter import *
from tkinter import filedialog

from cv2 import filter2D

window = Tk()
window.title("Face Detection")
window.geometry('500x300')

lbl = Label(window, text="To start tracking please click on button", font=("Poppins", 20), anchor=CENTER)
lbl.pack()

def openWindow():
    window.destroy()
    from face_detection_camera import face_from_camera
    face_from_camera()

button_photo = Button(window, text="Start Traking", command = openWindow)
button_photo.pack()

window.mainloop()