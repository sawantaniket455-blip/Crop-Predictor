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
my_canvas.create_text(600,100, text="Orange",font=("Arial",50))
my_canvas.create_text(660,280, text="Season : The ideal temperature range for orange farming is between 15°C and 38°C.",font=("Arial",20), fill="white")
my_canvas.create_text(740,340, text="  Soil and Climate Requirement : Oranges grow best in warm, sunny climates with moderate humidity\n    The soil should be rich in organic matter, and able to retain moisture.",font=("Arial",20), fill="white")
my_canvas.create_text(300,400, text="Irrigation : Drip Irrigation",font=("Arial",20), fill="white")
my_canvas.create_text(710,470, text="Manures and Fertilizers : Phosphate fertilizer is important for newly planted orange trees and \n fertile soils with a pH range of 6 to 7.5",font=("Arial",20), fill="white")
my_canvas.create_text(740,590, text="Plant Protection : Protect young trees by wrapping their trunks with burlap, blankets or cardboard,\n but inspect regularly for ant or other insect infestation",font=("Arial",20), fill="white")
my_canvas.create_text(730,690, text="   Harvest :  In the north, orange season is from December to February; in the South, the season is\n notably longer from October through March.",font=("Arial",20), fill="white")

orange = PhotoImage(file="C:\\Users\\ASUS\\Downloads\\orange (2).png")
label = Label(root,height=180,width=180, image=orange)
label.place(x=150,y=50)

button7 = Button(root, text="Back", font=("Times New Roman", 10), command=back)
button7_window = my_canvas.create_window(0, 0, anchor=NW, window=button7)
root.mainloop()