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
my_canvas.create_text(600,100, text="Maize",font=("Arial",50))
my_canvas.create_text(550,280, text="Season : Kharif (monsoon), post monsoon, Rabi (winter) and spring",font=("Arial",20), fill="white")
my_canvas.create_text(770,350, text="   Soil and Climate Requirement : The optimum temperature for the growth of maize is 18 degrees Celsius to\n   27 degrees Celsius during the day and 14 to 15 degrees Celsius at the night,Variety of soils ranging\n   from loamy sand to clay loam.",font=("Arial",20), fill="white")
my_canvas.create_text(330,420, text="   Irrigation :  Drip Irrigation systems",font=("Arial",20), fill="white")
my_canvas.create_text(820,490, text="Manures and Fertilizers : The quantity of fertilizers to be applied depends mainly on soil fertility and the preceding\n field management. In general, a balanced application of 120:60:40 kg/ha of NPK is recommended.",font=("Arial",20), fill="white")
my_canvas.create_text(820,560, text="  Plant Protection : The most important and effective measure is the selection of a resistant maize hybrid. \n  Additionally, the farmer can apply crop rotation, use of systemic fungicides, spray, and seed treatment applications",font=("Arial",20), fill="white")
my_canvas.create_text(690,620, text="     Harvest :  Sowing in rows is generally done with drill or by dropping the seed behind the plough.",font=("Arial",20), fill="white")

maize=PhotoImage(file="maize.png")
label = Label(root,height=180,width=180, image=maize)
label.place(x=150,y=50)
button7 = Button(root, text="Back", font=("Times New Roman", 10), command=back)
button7_window = my_canvas.create_window(0, 0, anchor=NW, window=button7)
root.mainloop()