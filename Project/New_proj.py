import tkinter as tk


root = tk.Tk()
HEIGHT = 800
WIDTH = 800
x1 = 0
y1 = 0
x2 = 0
y2 = 0
coordinat_list =[]
glob_color = 'black'
last_mpos = None
mx = None
mx1 = None
my1  = None
my = None


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="white")
        canvas.pack()

        frame = tk.Frame(root, bg="#f0f0f0", bd=5)
        frame.place(relx=0.5, y=0, relwidth=1, height=100, anchor='n')


        button = tk.Button(frame, 
                        text="Pencil", 
                        bg="gray", fg="white", 
                        font=('Courier', 12), 
                        #    command=lambda: get_weather(entry_field.get()))
                        command=lambda: my_pencil())
        button.place(relx=0.0, rely=0, relwidth=0.1, relheight=1)


        button = tk.Button(frame, 
                        text="Oval", 
                        bg="gray", fg="white", 
                        font=('Courier', 12), 
                        #    command=lambda: get_weather(entry_field.get()))
                        command=lambda: my_oval())
        button.place(relx=0.1, rely=0, relwidth=0.1, relheight=1)

        button = tk.Button(frame, 
                        text="line", 
                        bg="gray", fg="white", 
                        font=('Courier', 12), 
                        #    command=lambda: get_weather(entry_field.get()))
                        command=lambda: my_line())
        button.place(relx=0.2, rely=0, relwidth=0.1, relheight=1)


        button = tk.Button(frame, 
                        text="red", 
                        bg="red", fg="white", 
                        font=('Courier', 12), 
                        #    command=lambda: get_weather(entry_field.get()))
                        command=lambda: take_color('red'))
        button.place(relx=0.3, rely=0, relwidth=0.1, relheight=1)
        button = tk.Button(frame, 
                        text="green", 
                        bg="green", fg="white", 
                        font=('Courier', 12), 
                        #    command=lambda: get_weather(entry_field.get()))
                        command=lambda: take_color('green'))
        button.place(relx=0.4, rely=0, relwidth=0.1, relheight=1)
        button = tk.Button(frame, 
                        text="blue", 
                        bg="blue", fg="white", 
                        font=('Courier', 12), 
                        #    command=lambda: get_weather(entry_field.get()))
                        command=lambda: take_color('blue'))
        button.place(relx=0.5, rely=0, relwidth=0.1, relheight=1)


        def take_color(color):
            global glob_color
            glob_color = color

        def new_coord1(event):
            global x1, y1, x2, y2
            x1 = event.x
            x2 = x1
            y1 = event.y
            y2 = y1
        def new_coord2(event):
            global x1, y1, x2, y2
            x2 = event.x
            y2 = event.y
            create_figure(x1, y1, x2, y2, 'oval')
            
            x1, y1, x2, y2 = 0, 0, 0, 0

        def new_coord_line(event):
            global x1, y1, x2, y2
            x2 = event.x
            y2 = event.y
            create_figure(x1, y1, x2, y2, 'line')
            x1, y1, x2, y2 = 0, 0, 0, 0

        def new_coord_penc(event):
            global x1, y1, x2, y2
            x1 = event.x
            y1 = event.y
            create_figure(x1, y1, x1, y1, 'oval')
            x1, y1, x2, y2 = 0, 0, 0, 0

        def cre_ov(event):
            global x1, y1, x2, y2
            canvas.create_oval(x1,y1,x2,y2,outline = 'white', width=1)
            x2 = event.x
            y2 = event.y
            canvas.create_oval(x1,y1,x2,y2, width=1)

        def cre_line(event):
            global x1, y1, x2, y2
            canvas.create_line(x1,y1,x2,y2,fill = 'white', width=1)
            x2 = event.x
            y2 = event.y
            canvas.create_line(x1,y1,x2,y2, width=1)

        def cre_penc(event):
            global x1, y1, x2, y2
            canvas.create_(x1,y1,x2,y2,outline = 'white', width=1)
            x2 = event.x
            y2 = event.y
            canvas.create_oval(x1,y1,x2,y2, width=1)


        def create_figure(x1, y1, x2, y2, figure):
            
            coordinat_list.append([figure, x1, y1, x2, y2, glob_color])
            for i in coordinat_list:
                if i[0] == 'line':
                    canvas.create_line(i[1], i[2], i[3], i[4], fill = i[5], width=2)
                elif i[0] == 'oval':
                    canvas.create_oval(i[1], i[2], i[3], i[4], outline = i[5], width=2)


        def my_oval():
            canvas.bind('<Button-1>', new_coord1)
            canvas.bind('<B1-Motion>',cre_ov)
            canvas.bind('<ButtonRelease-1>', new_coord2)

        def my_line():
            canvas.bind('<Button-1>', new_coord1)
            canvas.bind('<B1-Motion>',cre_line)
            canvas.bind('<ButtonRelease-1>', new_coord_line)

        def my_pencil():
            canvas.bind('<Button-1>', new_coord1)
            canvas.bind('<B1-Motion>', new_coord_penc2)
            # canvas.bind('<ButtonRelease-1>', new_coord_penc)     
        

        def new_coord_penc2 (event):
            global x1, y1, x2, y2
            x1 = x2
            y1 = y2
            x2 = event.x
            y2 = event.y
            canvas.create_line(x1, y1, x2, y2, fill = glob_color, width=2)
            


if __name__ == "__main__":
    app = App()
    app.mainloop()