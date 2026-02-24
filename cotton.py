from tkinter import *

root = Tk()

root.title('Agro-Tech')
root.geometry("1920x1080")
def back():
    root.destroy()
    import crop_analysis

# define image
bg = PhotoImage(file="farm1.png")

#create a canvas
my_canvas = Canvas(root,width=1920,height=1080)
my_canvas.pack(fill="both",expand=True)

#set image in canvas
my_canvas.create_image(0,0,image=bg,anchor="nw")

#add a label
my_canvas.create_text(600,100, text="Cotton",font=("Arial",50))
my_canvas.create_text(220,280, text="    Season : Kharif",font=("Arial",20), fill="white")
my_canvas.create_text(700,350, text=" Soil and Climate Requirement : Cotton is grown on a variety of soils ranging from well drained\n deep alluvial soils in the north to black clayey soils of varying depth in central region\n and in black and mixed black and red soils in south zone.",font=("Arial",20), fill="white")
my_canvas.create_text(301,420, text="       Irrigation :  Ridges and furrrows" ,font=("Arial",20), fill="white")
my_canvas.create_text(630,480, text="   Manures and Fertilizers : Liquid fertilizers used in Cotton crops are cow urine, slurry\n   (from cow dung or biogas), vermi-wash, Amruth pani, Jeev amruth. ",font=("Arial",20), fill="white")
my_canvas.create_text(700,550, text="   Plant Protection : Sticky traps may be useful for detecting whitefly movement into cotton fields. ",font=("Arial",20), fill="white")
my_canvas.create_text(780,630, text="Harvest : Cotton is machine harvested beginning in July  and in October in more northern areas of the Belt.\n Stripper harvesters, have rollers or mechanical brushes that remove the entire boll from the plant.\n In the rest of the Belt, spindle pickers are used ",font=("Arial",20), fill="white")

cotton=PhotoImage(file="cotton.png")
label = Label(root,height=180,width=180, image=cotton)
label.place(x=150,y=50)
button7 = Button(root, text="Back", font=("Times New Roman", 10), command=back)
button7_window = my_canvas.create_window(0, 0, anchor=NW, window=button7)
root.mainloop()