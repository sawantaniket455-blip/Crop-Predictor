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
my_canvas.create_text(600,100, text="Rice",font=("Arial",50))
my_canvas.create_text(300,280, text="Season : Kharif or Winter",font=("Arial",20), fill="white")
my_canvas.create_text(600,330, text="  Soil and Climate Requirement : Hot and Humid Climate, Clay or Clay Loams",font=("Arial",20), fill="white")
my_canvas.create_text(300,380, text="Irrigation : Drip Irrigation",font=("Arial",20), fill="white")
my_canvas.create_text(720,460, text="Manures and Fertilizers : Ammonium Sulphate is used for completing the need of Nitrogen and \nSulphate to meet the needs of nutritional value",font=("Arial",20), fill="white")
my_canvas.create_text(770,580, text="Plant Protection : The plant hoppers can be controlled by spraying 40 ml Confidor 200 SL (imidacloprid)\n or 800 ml Ekalux/Quinguard 25 EC (quinalphos) or one litre Coroban/Dursban 20 EC (chlorpyriphos) or \n560 ml Thiodan/ Endocel 35 EC (endosulfan) in 100 litres of water per acre.\n Repeat the spray if necessary.",font=("Arial",20), fill="white")
my_canvas.create_text(780,690, text="Harvest : November to February is the sowing season for rice and March to June is the harvesting time.",font=("Arial",20), fill="white")

rice=PhotoImage(file="rice.png")
label = Label(root,height=180,width=180, image=rice)
label.place(x=150,y=50)

button7 = Button(root, text="Back", font=("Times New Roman", 10), command=back)
button7_window = my_canvas.create_window(0, 0, anchor=NW, window=button7)
root.mainloop()