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
my_canvas.create_text(600,100, text="Wheat",font=("Arial",50))
my_canvas.create_text(187,280, text="Season : October-November",font=("Arial",20), fill="white")
my_canvas.create_text(750,330, text="Soil and Climate Requirement : Temperature must be between 10-15 degrees centigrade at the time of sowing,Loamy Soil",font=("Arial",20), fill="white")
my_canvas.create_text(301,380, text="Irrigation :  Drip and Sprinkler Irrigation systems",font=("Arial",20), fill="white")
my_canvas.create_text(455,460, text="Manures and Fertilizers : NPK fertilizer.\nP and K are the two most important nutrients after N for wheat cultivation.",font=("Arial",20), fill="white")
my_canvas.create_text(750,550, text="Plant Protection : Among the crop protection techniques are tillage, crop rotation, organic and synthetic pesticide use,field \n monitoring,etc",font=("Arial",20), fill="white")
my_canvas.create_text(610,650, text="Harvest :  Harvesting stage comes when normally the plant turns golden yellow and becomes brittle.\n The grains become hard and the straw turns dry.\n The crop should be harvested at physiological maturity when the grain moisture is around 19-20%.",font=("Arial",20), fill="white")

wheat=PhotoImage(file="wheat.png")
label = Label(root,height=180,width=180, image=wheat)
label.place(x=150,y=50)
button7 = Button(root, text="Back", font=("Times New Roman", 10), command=back)
button7_window = my_canvas.create_window(0, 0, anchor=NW, window=button7)
root.mainloop()