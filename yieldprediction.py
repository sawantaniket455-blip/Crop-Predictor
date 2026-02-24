from tkinter import *

def wheat1(a,b,c,d):
    yield0=(a*b*c)/d  # B:average num of grains per pod C:weight of 100 grains of wheat
    return yield0
def back():
    root.destroy()
    import front

root = Tk()
root.title("Mini Project")
root.geometry("1920x1080")
bg = PhotoImage(file="farm1.png")
my_canvas = Canvas(root,width=1920,height=1080)

my_canvas.pack(fill="both",expand=True)

#set image in canvas
my_canvas.create_image(0,0,image=bg,anchor="nw")

def predict0():
    value0=entry1.get()
    value0=int(value0)
    value1=entry2.get()
    value1=int(value1)
    value2 = entry3.get()
    value2 = int(value2)
    value3 = entry4.get()
    value3 = int(value3)


    yield1=wheat1(value0,value1,value2,value3)
    yield1=str(yield1)
    my_canvas.create_text(700,600, text="Expected yield will be "+yield1+" Kgs/acre",font=("Times New Roman Bold",30), fill="red")

my_canvas.create_text(800,80, text="Enter the following Details :-",font=("Times New Roman",45),fill="green")
my_canvas.create_text(500,160, text=" Enter average number of pods/heads per m^2                    ",font=("Times New Roman",30),fill="white")
my_canvas.create_text(500,230, text="  Enter average number of grains per pod/head                  ",font=("Times New Roman",30),fill="white")
my_canvas.create_text(500,300, text="   Enter weight of 100 grains                             ",font=("Times New Roman",30),fill="white")
my_canvas.create_text(500,370, text="   Enter area of field ",font=("Times New Roman",30),fill="white")
my_canvas.create_text(1100,160, text=":",font=("Times New Roman",30),fill="white")
my_canvas.create_text(1100,230, text=":",font=("Times New Roman",30),fill="white")
my_canvas.create_text(1100,300, text=":",font=("Times New Roman",30),fill="white")
my_canvas.create_text(1100,370, text=":",font=("Times New Roman",30),fill="white")

entry1 = Entry(root, font="30", bd=3)
my_canvas.create_window(1250, 160, window=entry1)
entry2= Entry(root, font="30", bd=3)
my_canvas.create_window(1250, 230, window=entry2)
entry3 = Entry(root, font="30", bd=3)
my_canvas.create_window(1250, 300, window=entry3)
entry4 = Entry(root, font="30", bd=3)
my_canvas.create_window(1250, 370, window=entry4)


button1 = Button(root, text="Predict", font=("Times New Roman", 25),command=predict0)
button_window = my_canvas.create_window(800, 500, window=button1)
button2 = Button(root, text="Back", font=("Times New Roman", 15),command=back)
button_window = my_canvas.create_window(20, 20, window=button2)

root.mainloop()