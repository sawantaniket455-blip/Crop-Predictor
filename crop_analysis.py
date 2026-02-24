# Import module
from tkinter import *

root = Tk()

root.title('This is our Mini-Project')
root.geometry("1920x1080")

def back():
    root.destroy()
    import front

def wheat1():
    root.destroy()
    import wheat

def rice1():
    root.destroy()
    import rice

def orange():
    root.destroy()
    import orange

def maize1():
    root.destroy()
    import maize

def sugarcane1():
    root.destroy()
    import sugarcane

def cotton1():
    root.destroy()
    import cotton

# define image
bg = PhotoImage(file="farm1.png")

wheat=PhotoImage(file="wheat.png")
rice = PhotoImage(file="rice.png")
og = PhotoImage(file="C:\\Users\\sawan\\Downloads\\orange.png")
maize=PhotoImage(file="maize.png")
sugarcane = PhotoImage(file="sugarcane.png")
cotton= PhotoImage(file="cotton.png")

#create a canvas
my_canvas = Canvas(root,width=1920,height=1080)
my_canvas.pack(fill="both",expand=True)

#set image in canvas
my_canvas.create_image(0,0,image=bg,anchor="nw")
my_canvas.create_text(770,100, text="Select a Crop",font=("Arial",45),fill="green")
'''img_label1= Label(image=wheat)
img_label2= Label(image=rice)
img_label3= Label(image=orange)
img_label1= Label(image=maize)
img_label2= Label(image=sugarcane)
img_label3= Label(image=cotton)'''
#add some butons
button1 = Button(root, image=wheat,width=268,height=168, command=wheat1)
button2 = Button(root, image=rice,width=268,height=168, command=rice1)
button3 = Button(root, image=og,width=268,height=168, command=orange)
button4 = Button(root, image=maize,width=268,height=168, command=maize1)
button5 = Button(root, image=sugarcane,width=268,height=168, command=sugarcane1)
button6 = Button(root, image=cotton,width=268,height=168, command=cotton1)



button1_window = my_canvas.create_window(450,320,window=button1)
button2_window = my_canvas.create_window(1095,320,window=button2)
button3_window = my_canvas.create_window(775,320,window=button3)
button4_window = my_canvas.create_window(450,520,window=button4)
button5_window = my_canvas.create_window(1095,520,window=button5)
button6_window = my_canvas.create_window(775,520,window=button6)

button7 = Button(root, text="Back", font=("Times New Roman", 10), command=back)
button7_window = my_canvas.create_window(0, 0, anchor=NW, window=button7)



root.mainloop()