from tkinter import *

root = Tk()
root.geometry("1920x1080")
def predict_op():
    root.destroy()
    import reg

def back():
    try:
        root.destroy()
        import front
    except:
        print("Hi")

bg=PhotoImage(file="farm1.png")

my_canvas = Canvas(root,width=1920,height=1080)
my_canvas.pack(fill="both",expand=True)

my_canvas.create_image(0,0,image=bg,anchor="nw")
my_canvas.create_text(800,80, text="Enter the following Details :-",font=("Times New Roman",45),fill="green")
my_canvas.create_text(500,160, text=" Enter ratio of Nitrogen in the soil                    ",font=("Times New Roman",30),fill="white")
my_canvas.create_text(500,230, text="  Enter ratio of Potassium in the soil                  ",font=("Times New Roman",30),fill="white")
my_canvas.create_text(500,300, text="   Enter ratio of Phosphorus in the soil                 ",font=("Times New Roman",30),fill="white")
my_canvas.create_text(500,370, text="           Enter Average Temperature around the field            ",font=("Times New Roman",30),fill="white")
my_canvas.create_text(500,440, text="                 Enter Average Percentage of Humidity around the field ",font=("Times New Roman",30),fill="white")
my_canvas.create_text(500,510, text="   Enter the pH value of the soil                            ",font=("Times New Roman",30),fill="white")
my_canvas.create_text(500,580, text="              Enter Average amount of Rainfall around the field     ",font=("Times New Roman",30),fill="white")
my_canvas.create_text(1420,370, text="Celsius",font=("Arial",20),fill="white")
my_canvas.create_text(1420,440, text="%",font=("Times New Roman",20),fill="white")
my_canvas.create_text(1420,580, text="mm",font=("Times New Roman",20),fill="white")
my_canvas.create_text(1100,160, text=":",font=("Times New Roman",30),fill="white")
my_canvas.create_text(1100,230, text=":",font=("Times New Roman",30),fill="white")
my_canvas.create_text(1100,300, text=":",font=("Times New Roman",30),fill="white")
my_canvas.create_text(1100,370, text=":",font=("Times New Roman",30),fill="white")
my_canvas.create_text(1100,440, text=":",font=("Times New Roman",30),fill="white")
my_canvas.create_text(1100,510, text=":",font=("Times New Roman",30),fill="white")
my_canvas.create_text(1100,580, text=":",font=("Times New Roman",30),fill="white")


entry_widget1 = Entry(root, font="30", bd=3)
my_canvas.create_window(1250, 160, window=entry_widget1)
entry_widget2 = Entry(root, font="30", bd=3)
my_canvas.create_window(1250, 230, window=entry_widget2)
entry_widget3 = Entry(root, font="30", bd=3)
my_canvas.create_window(1250, 300, window=entry_widget3)
entry_widget4 = Entry(root, font="30", bd=3)
my_canvas.create_window(1250, 370, window=entry_widget4)
entry_widget5 = Entry(root, font="30", bd=3)
my_canvas.create_window(1250, 440, window=entry_widget5)
entry_widget6 = Entry(root, font="30", bd=3)
my_canvas.create_window(1250, 510, window=entry_widget6)
entry_widget7 = Entry(root, font="30", bd=3)
my_canvas.create_window(1250, 580, window=entry_widget7)

button1 = Button(root, text="Predict", font=("Times New Roman", 25),command=predict_op)
button1_window = my_canvas.create_window(750, 700, window=button1)
button2 = Button(root, text="Back", font=("Times New Roman", 10), command=back)
button2_window = my_canvas.create_window(0, 0, anchor=NW, window=button2)


root.mainloop()
