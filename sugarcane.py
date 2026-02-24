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
my_canvas.create_text(600,100, text="Sugarcane",font=("Arial",50))
my_canvas.create_text(780,300, text="Season : Sugarcane planting is done in December-February for the 12-month crop which is called Eksali,\nin October-November for the 15 to 16 month crop which is called Preseasonal,\nand in July-August for the 18-month crop, which is called Adsali",font=("Arial",20), fill="white")
my_canvas.create_text(835,385, text="  Soil and Climate Requirement : Sugarcane grows well in tropical regions with 100-150 cm of rainfall well distributed\n  throughout the year. This crop is grown well in drained rich alluvial, heavy loams or lava soils.",font=("Arial",20), fill="white")
my_canvas.create_text(460,430, text="Irrigation :  Subsurface drip irrigation (SDI) systems",font=("Arial",20), fill="white")
my_canvas.create_text(800,500, text="Manures and Fertilizers : Large organic manures such as compost, Farmyard Manure, and press mud\nmust be added to the soil at the rate of 15 to 25 tons per hectare before planting. Sunn hemp green manure\ncan be grown as an intercrop and added to the soil 30 to 45 days after planting.",font=("Arial",20), fill="white")
my_canvas.create_text(680,590, text="Plant Protection : The inflorescence of sugarcane is a terminal panicle which possesses \ntwo spikelets and seeds protected by husks (glumes) covered in silky hair.",font=("Arial",20), fill="white")
my_canvas.create_text(720,660, text="Harvest : Sugarcane is harvested by mechanical harvester which move along the rows of cane\nremoving the leafy tops of the cane and cutting the stalk into short pieces or billets",font=("Arial",20), fill="white")

sg=PhotoImage(file="sugarcane.png")
label = Label(root,height=180,width=180, image=sg)
label.place(x=150,y=50)
button7 = Button(root, text="Back", font=("Times New Roman", 10), command=back)
button7_window = my_canvas.create_window(0, 0, anchor=NW, window=button7)
root.mainloop()