from tkinter import *

root = Tk()
root.geometry("1920x1080")
bg=PhotoImage(file="farm1.png")

my_canvas = Canvas(root,width=800,height=500)
my_canvas.pack(fill="both",expand=True)

my_canvas.create_image(0,0,image=bg,anchor="nw")

my_canvas.create_text(400,250, text="AGRO-TECH",font=("Arial",45))

frame = Frame(root)
frame.pack(padx=10,pady=10)
root.mainloop()
