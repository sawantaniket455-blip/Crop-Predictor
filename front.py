from tkinter import *


root = Tk()

root.title('This is our Mini-Project')
root.geometry("1920x1080")
def crop_suggest():
   try:
       root.destroy()
       import CropPrediction1
   except:
      print("Hi")

def crop_yield():
   try:
      root.destroy()
      import yieldprediction
   except:
      print("Hi")

def analysis():
   try:
      root.destroy()
      import crop_analysis
   except:
      print("Hi")

# define image
bg = PhotoImage(file="farm1.png")
crop_predictor=PhotoImage(file="crop.png")
yield_predictor = PhotoImage(file="yield.png")
crop_analysis= PhotoImage(file="analysis.png")
#create a canvas
my_canvas = Canvas(root,width=1920,height=1080)

my_canvas.pack(fill="both",expand=True)

#set image in canvas
my_canvas.create_image(0,0,image=bg,anchor="nw")

#add a label
my_canvas.create_text(770,100, text="AGRO-TECH",font=("Arial",45),fill="Dark green")

#event
img_label1= Label(image=crop_predictor)
img_label2= Label(image=yield_predictor)
img_label3= Label(image=crop_analysis)
#add some butons
button1 = Button(root, image=crop_predictor,width=268,height=168, command=crop_suggest)
button2 = Button(root, image=yield_predictor,width=270,height=171, command=crop_yield)
button3 = Button(root, image=crop_analysis,width=280,height=150, command=analysis)

#Import the image using PhotoImage function click_btn= PhotoImage(file='clickme.png')

button1_window = my_canvas.create_window(550,350,window=button1)
button2_window = my_canvas.create_window(845,260,anchor="nw",window=button2)
button3_window = my_canvas.create_window(775,635,window=button3)
root.mainloop()
