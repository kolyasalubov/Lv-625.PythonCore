# x1 = 1
# x2 = 2
# x3 = 3
# x4 = 4
# glob_color = 'red'
# my_list = [x1, x2, x3, x4]
# my_list2 = []

# my_list2.append([x1, x2, x3, x4, "fill =", glob_color])


# # for i in my_list:
   
# print(my_list2)

#######################################################################################

# import tkinter
# #
# #
# def many_button(event):
#     next_ = int(event.widget["text"][-2:]) + 1
#     if not buttons[next_].winfo_manager():
#         buttons[next_].grid(row=next_, column=0)
#         buttons[next_]["bg"] = "red"
#         buttons[next_].master.update_idletasks()
#     elif not int(event.widget["text"][-2:]) % 2:
#         buttons[next_].grid_forget()
#     new_height = buttons[next_].master.winfo_height()
#     canv.config(scrollregion=(0, 0, 200, new_height))
# #
# root = tkinter.Tk()
# root.geometry("400x400+100+100")
# #
# canv = tkinter.Canvas(root, width=194, height=400)
# canv.pack(side="left")
# #
# frame = tkinter.Frame(canv)
# frame.pack()
# buttons = []
# for i in range(20):
#     but = tkinter.Button(frame, text=u"Кнопка %02d" % i, width=21)
#     if not i % 2:
#         but.grid(row=i, column=0)
#     but.bind("<Button-1>", many_button)
#     buttons.append(but)
# #
# scr = tkinter.Scrollbar(root, orient="vertical", takefocus=False)
# scr.pack(side="left", fill="y")
# scr["command"] = canv.yview
# #
# canv.create_window((0, 0), window=frame, anchor="nw")
# canv.config(yscrollcommand=scr.set, scrollregion=(0, 0, 200, 400))
# #
# root.mainloop()


#######################################################################################


# import tkinter, random
# class App:
#     def __init__(self, t):
#         self.i = tkinter.PhotoImage(width=100,height=100)
#         colors = [[random.randint(0,255) for i in range(0,3)] for j in range(0,10000)]
#         row = 0; col = 0
#         for color in colors:
#            self.i.put('#%02x%02x%02x' % tuple(color),(row,col))
#            col += 1
#            if col == 100:
#                row +=1; col = 0        
#         c = tkinter.Canvas(t, width=100, height=100); c.pack()
#         c.create_image(0, 0, image = self.i, anchor=tkinter.NW)

# t = tkinter.Tk()
# a = App(t)    
# t.mainloop()


#######################################################################################


# from tkinter import *
# import random

# def RGBs(num):
#  # random list of list RGBs
#  return [[random.randint(0,255) for i in range(0,3)] for j in range(0,num)]

# def rgb2Hex(rgb_tuple):
#     return '#%02x%02x%02x' % tuple(rgb_tuple)

# def drawGrid(w,colors):
#  col = 0; row = 0
#  colors = [rgb2Hex(color) for color in colors]
#  for color in colors:
#   w.create_rectangle(col, row, col+1, row+1, fill=color, outline=color)
#   col+=1
#   if col == 100:
#    row += 1; col = 0

# root = Tk()
# w = Canvas(root)
# w.grid()
# colors = RGBs(5000)
# drawGrid(w,colors)
# root.mainloop()


#######################################################################################

# import tkinter, random
# import random

# class App:
#     def __init__(self, t):
#         self.width = 320
#         self.height = 200
#         self.i = tkinter.PhotoImage(width=self.width,height=self.height)
#         rgb_colors = ([random.randint(0,255) for i in range(0,3)] for j in range(0,self.width*self.height))
#         pixels=" ".join(("{"+" ".join(('#%02x%02x%02x' %
#             tuple(next(rgb_colors)) for i in range(self.width)))+"}" for j in range(self.height)))
#         self.i.put(pixels,(0,0,self.width-1,self.height-1))
#         c = tkinter.Canvas(t, width=self.width, height=self.height); c.pack()
#         c.create_image(0, 0, image = self.i, anchor=tkinter.NW)

# t = tkinter.Tk()
# a = App(t)    
# t.mainloop()


#######################################################################################

# from tkinter import *

# canvas_width = 300
# canvas_height =80

# master = Tk()
# canvas = Canvas(master, 
#            width=canvas_width, 
#            height=canvas_height)
# canvas.pack()

# bitmaps = ["error", "gray75", "gray50", "gray25", "gray12", "hourglass", "info", "questhead", "question", "warning"]
# nsteps = len(bitmaps)
# step_x = int(canvas_width / nsteps)

# for i in range(0, nsteps):
#    canvas.create_bitmap((i+1)*step_x - step_x/2,50, bitmap=bitmaps[i])
# master.mainloop()

#######################################################################################

# import tkinter as tk

# RELIEFS = [tk.SUNKEN, tk.RAISED, tk.GROOVE, tk.RIDGE, tk.FLAT]


# class ButtonsApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.img = tk.PhotoImage(file="python.gif")
#         self.btn = tk.Button(self, text="Кнопка с изображением",
#                              image=self.img, compound=tk.TOP,
#                              command=self.disable_btn)
#         self.btns = [self.create_btn(r) for r in RELIEFS]
#         self.btn.pack()
#         for btn in self.btns:
#             btn.pack(padx=10, pady=10, side=tk.LEFT)

#     def create_btn(self, relief):
#         return tk.Button(self, text=relief, relief=relief)

#     def disable_btn(self):
#         self.btn.config(state=tk.DISABLED)


# if __name__ == "__main__":
#     app = ButtonsApp()
#     app.mainloop()


#######################################################################################


# import tkinter as tk

# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Демо иконки курсора")
#         self.resizable(0, 0)
#         self.label = tk.Label(self, text="Нажмите для старта")
#         self.btn_launch = tk.Button(self, text="Старт   !",
#                                     command=self.perform_action)
#         self.btn_help = tk.Button(self, text="Помощь",
#                                   cursor="question_arrow")

#         btn_opts = {"side": tk.LEFT, "expand": True, "fill": tk.X,
#                     "ipadx": 30, "padx": 20, "pady": 5}
#         self.label.pack(pady=10)
#         self.btn_launch.pack(**btn_opts)
#         self.btn_help.pack(**btn_opts)

#     def perform_action(self):
#         self.btn_launch.config(state=tk.DISABLED)
#         self.btn_help.config(state=tk.DISABLED)
#         self.label.config(text="Запуск...")
#         self.after(3000, self.end_action)
#         self.config(cursor="watch")

#     def end_action(self):
#         self.btn_launch.config(state=tk.NORMAL)
#         self.btn_help.config(state=tk.NORMAL)
#         self.label.config(text="Готово!")
#         self.config(cursor="arrow")

#     def set_watch_cursor(self, widget):
#         widget._old_cursor = widget.cget("cursor")
#         widget.config(cursor="watch")
#         for w in widget.winfo_children():
#             self.set_watch_cursor(w)

#     def restore_cursor(self, widget):
#         widget.config(cursor=widget.old_cursor)
#         for w in widget.winfo_children():
#             self.restore_cursor(w)

# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

#######################################################################################

# import tkinter as tk

# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         label_a = tk.Label(self, text="Label A", bg="yellow")
#         label_b = tk.Label(self, text="Label B", bg="orange")
#         label_c = tk.Label(self, text="Label C", bg="red")
#         label_d = tk.Label(self, text="Label D", bg="green")
#         label_e = tk.Label(self, text="Label E", bg="blue")

#         label_a.place(relwidth=0.25, relheight=0.25)
#         label_b.place(x=100, anchor=tk.N,
#                       width=100, height=50)
#         label_c.place(relx=0.5, rely=0.5, anchor=tk.CENTER,
#                       relwidth=0.5, relheight=0.5)
#         label_d.place(in_=label_c, anchor=tk.N + tk.W,
#                       x=2, y=2, relx=0.5, rely=0.5,
#                       relwidth=0.5, relheight=0.5)
#         label_e.place(x=200, y=200, anchor=tk.S + tk.E,
#                       relwidth=0.25, relheight=0.25)

# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

############################################################################################

# from tkinter import *

# root = Tk()
# c = Canvas(root, width=640, height=480, bd=0, highlightthickness=0)
# c.create_line(0,240,640,240, fill='blue')
# c.pack()

# #pil image with transparency
# try:
#     from PIL import Image, ImageTk
# except ImportError:
#     pass
# else:
#     # pim = Image.new('RGBA', (5,100), (0,255,0,64))
#     pim = Image.new('RGBA', (40,200), (0,255,0,255))
#     photo = ImageTk.PhotoImage(pim)
#     c.create_image(200,200, image=photo, anchor='nw')

# #blank standard photoimage with red vertical borders
# im = PhotoImage(width=7, height=480)
# dat = ('red',)*480
# im.put(dat, to=(0,0))
# im.put(dat, to=(6,0))

# box = c.create_image(0, 0, image=im, anchor='nw')

# def on_motion(event):
#     left,top = c.coords(box)
#     dx = event.x - (left+7)
#     c.move(box, dx, 0)

# c.bind('<Motion>', on_motion)
# root.mainloop()


#######################################################################

# import tkinter as tk


# root = tk.Tk()

# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         self.canvas = tk.Canvas(self, width=500, height=200, bd=0, highlightthickness=0)
#         self.canvas.create_rectangle(245,50,345,150, fill='white')

#         self.image = tk.PhotoImage(file='chess.png')
#         self.image_id = self.canvas.create_image(50,50, image=self.image)

#         self.canvas.move(self.image_id, 245, 100)

# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

#############################################################################

# import tkinter as tk
# # Python 2 import tkinter as tk # Python 3 
# root = tk.Tk() # The image must be stored to Tk or it will be garbage collected. 
# root.image = tk
# tk.PhotoImage(file='IMG_5444.gif')
# label = tk.Label(root, image=root.image, bg='white')
# root.overrideredirect(True)
# root.geometry("+250+250")
# root.lift()
# root.wm_attributes("-topmost", True)
# root.wm_attributes("-disabled", True)
# root.wm_attributes("-transparentcolor", "white")
# label.pack()
# label.mainloop() 

#################################################################################

# import tkinter as tk
# from PIL import Image
# from PIL import ImageDraw

# # import Image as my_img
# # import ImageDraw

# class ImageGenerator:
#     def __init__(self,parent,posx,posy,*kwargs):
#         self.parent = parent
#         self.posx = posx
#         self.posy = posy
#         self.sizex = 200
#         self.sizey = 200
#         self.b1 = "up"
#         self.xold = None
#         self.yold = None 
#         self.drawing_area=tk.Canvas(self.parent,width=self.sizex,height=self.sizey)
#         self.drawing_area.place(x=self.posx,y=self.posy)
#         self.drawing_area.bind("<Motion>", self.motion)
#         self.drawing_area.bind("<ButtonPress-1>", self.b1down)
#         self.drawing_area.bind("<ButtonRelease-1>", self.b1up)
#         self.button=tk.Button(self.parent,text="Done!",width=10,bg='white',command=self.save)
#         self.button.place(x=self.sizex/7,y=self.sizey+20)
#         self.button1=tk.Button(self.parent,text="Clear!",width=10,bg='white',command=self.clear)
#         self.button1.place(x=(self.sizex/7)+80,y=self.sizey+20)

#         self.image=Image.new("RGB",(200,200),(255,255,255))
#         self.draw=ImageDraw.Draw(self.image)

#     def save(self):
#         filename = "temp.jpg"
#         self.image.save(filename)

#     def clear(self):
#         self.drawing_area.delete("all")
#         self.image=Image.new("RGB",(200,200),(255,255,255))
#         self.draw=ImageDraw.Draw(self.image)

#     def b1down(self,event):
#         self.b1 = "down"

#     def b1up(self,event):
#         self.b1 = "up"
#         self.xold = None
#         self.yold = None

#     def motion(self,event):
#         if self.b1 == "down":
#             if self.xold is not None and self.yold is not None:
#                 event.widget.create_line(self.xold,self.yold,event.x,event.y,smooth='true',width=3,fill='blue')
#                 self.draw.line(((self.xold,self.yold),(event.x,event.y)),(0,128,0),width=3)

#         self.xold = event.x
#         self.yold = event.y

# if __name__ == "__main__":
#     root=tk.Tk()
#     root.wm_geometry("%dx%d+%d+%d" % (400, 400, 10, 10))
#     root.config(bg='white')
#     ImageGenerator(root,10,10)
#     root.mainloop()


    ##########################################################################################################


# from tkinter import *
# from tkinter import messagebox
# top = Tk()

# C = Canvas(top, bg="red", height=250, width=300)
# filename = PhotoImage(file = "imageName.png")
# background_label = Label(top, image=filename)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)
# C.pack()
# Label.create_line(10, 20, 200, 250, fill = 'green', width=20)

# top.mainloop()

##################################################################################################

# # import Tkinter as tk # Python 2
# import tkinter as tk # Python 3
# root = tk.Tk()
# # The image must be stored to Tk or it will be garbage collected.
# root.image = tk.PhotoImage(file='imageName.png')
# label = tk.Label(root, image=root.image, bg='white')
# # root.overrideredirect(True)
# root.geometry("+250+250")
# # root.lift()
# # root.wm_attributes("-topmost", True)
# # root.wm_attributes("-disabled", True)
# # root.wm_attributes("-transparentcolor", "white")
# label.pack()
# label.mainloop()


############################################################################################

import tkinter
from PIL import Image, ImageTk

class App:
    def __init__(self):
        self.root = tkinter.Tk()

        # создаем рабочую область
        self.frame = tkinter.Frame(self.root)
        self.frame.grid()

        # Добавим метку
        self.label = tkinter.Label(self.frame, text="Hello, World!").grid(row=1, column=1)

        self.image = Image.open("chess.png")
        self.photo = ImageTk.PhotoImage(self.image)

        # вставляем кнопку
        self.but = tkinter.Button(self.frame, text="Кнопка", command=self.my_event_handler).grid(row=1, column=2)

        # Добавим изображение
        self.canvas = tkinter.Canvas(self.root, height=600, width=700)
        self.c_image = self.canvas.create_image(0, 0, anchor='nw', image=self.photo)
        self.canvas.grid(row=2, column=1)
        self.root.mainloop()

    def my_event_handler(self):
        print("my_event_handler")
        self.image = Image.open("imageName.png")
        self.photo = ImageTk.PhotoImage(self.image)
        self.c_image = self.canvas.create_image(0, 0, anchor='nw', image=self.photo)
        self.canvas.grid(row=2, column=1)

app= App()
