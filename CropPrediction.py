from tkinter import *
import pyttsx3  # Importing pyttsx3 library to convert text into speech.
import pandas as pd  # Importing pandas library
from sklearn import preprocessing  # Importing sklearn library. This is a very powerfull library for machine learning. Scikit-learn is probably the most useful library for machine learning in Python. The sklearn library contains a lot of efficient tools for machine learning and statistical modeling including classification, regression, clustering and dimensionality reduction.
from sklearn.neighbors import KNeighborsClassifier  # Importing Knn Classifier from sklearn library.
import numpy as np  # Importing numpy to do stuffs related to arrays
import PySimpleGUI as sg  # Importing pysimplegui to make a Graphical User Interface.

def predict0():
    values0 = entry_widget1.get()
    values0 = int(values0)
    values1 = entry_widget2.get()
    values1 = int(values1)
    values2 = entry_widget3.get()
    values2 = int(values2)
    values3 = entry_widget4.get()
    values3 = int(values3)
    values4 = entry_widget5.get()
    values4 = int(values4)
    values5 = entry_widget6.get()
    values5 = int(values5)
    values6 = entry_widget7.get()
    values6 = int(values6)

    excel = pd.read_excel('crop.xlsx', header=0)  # Importing our excel data from a specific file.
    print(excel)  # Printing our excel file data.
    print(excel.shape)  # Checking out the shape of our data.

    engine = pyttsx3.init('sapi5')  # Defining the speech rate, type of voice etc.
    voices = engine.getProperty('voices')
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 20)
    engine.setProperty('voice', voices[0].id)


    def speak(audio):  # Defining a speak function. We can call this function when we want to make our program to speak something.
        engine.say(audio)
        engine.runAndWait()


    le = preprocessing.LabelEncoder()  # Various machine learning algorithms require numerical input data, so you need to represent categorical columns in a numerical column. In order to encode this data, you could map each value to a number. This process is known as label encoding, and sklearn conveniently will do this for you using Label Encoder.
    crop = le.fit_transform(list(excel["CROP"]))  # Mapping the values in weather into numerical form.

    NITROGEN = list(excel["NITROGEN"])  # Making the whole row consisting of nitrogen values to come into nitrogen.
    PHOSPHORUS = list(excel["PHOSPHORUS"])  # Making the whole row consisting of phosphorus values to come into phosphorus.
    POTASSIUM = list(excel["POTASSIUM"])  # Making the whole row consisting of potassium values to come into potassium.
    TEMPERATURE = list(excel["TEMPERATURE"])  # Making the whole row consisting of temperature values to come into temperature.
    HUMIDITY = list(excel["HUMIDITY"])  # Making the whole row consisting of humidity values to come into humidity.
    PH = list(excel["PH"])  # Making the whole row consisting of ph values to come into ph.
    RAINFALL = list(excel["RAINFALL"])  # Making the whole row consisting of rainfall values to come into rainfall.

    features = list(
        zip(NITROGEN, PHOSPHORUS, POTASSIUM, TEMPERATURE, HUMIDITY, PH, RAINFALL))  # Zipping all the features together
    features = np.array([NITROGEN, PHOSPHORUS, POTASSIUM, TEMPERATURE, HUMIDITY, PH,RAINFALL])  # Converting all the features into a array form

    features = features.transpose()  # Making transpose of the features
    print(features.shape)  # Printing the shape of the features after getting transposed.
    print(crop.shape)  # Printing the shape of crop. Please note that the shape of the features and crop should match each other to make predictions.

    model = KNeighborsClassifier(n_neighbors=3)  # The number of neighbors is the core deciding factor. K is generally an odd number if the number of classes is 2. When K=1, then the algorithm is known as the nearest neighbor algorithm.
    model.fit(features,crop)  # fit your model on the train set using fit() and perform prediction on the test set using predict().

    print(values0)
    nitrogen_content = values0  # Taking input from the user about nitrogen content in the soil.
    phosphorus_content = values1  # Taking input from the user about phosphorus content in the soil.
    potassium_content = values2  # Taking input from the user about potassium content in the soil.
    temperature_content = values3  # Taking input from the user about the surrounding temperature.
    humidity_content = values4  # Taking input from the user about the surrounding humidity.
    ph_content = values5  # Taking input from the user about the ph level of the soil.
    rainfall = values6  # Taking input from the user about the rainfall.
    predict1 = np.array([nitrogen_content, phosphorus_content, potassium_content, temperature_content, humidity_content, ph_content,rainfall])  # Converting all the data that we collected from the user into a array form to make further
    # predictions.
    print(predict1)  # Printing the data after being converted into a array form.
    predict1 = predict1.reshape(1,-1)  # Reshaping the input data so that it can be applied in the model for getting accurate results.
    print(predict1)  # Finally printing out the results.
    predict1 = model.predict(predict1)
    print(predict1)
    crop_name = str()
    if predict1 == 0:  # Above we have converted the crop names into numerical form, so that we can apply the machine learning model easily. Now we have to again change the numerical values into names of crop so that we can print it when required.
        crop_name = 'Apple(सेब)'
    elif predict1 == 1:
        crop_name = 'Banana(केला)'
    elif predict1 == 2:
        crop_name = 'Blackgram(काला चना)'
    elif predict1 == 3:
        crop_name = 'Chickpea(काबुली चना)'
    elif predict1 == 4:
        crop_name = 'Coconut(नारियल)'
    elif predict1 == 5:
        crop_name = 'Coffee(कॉफ़ी)'
    elif predict1 == 6:
        crop_name = 'Cotton(कपास)'
    elif predict1 == 7:
        crop_name = 'Grapes(अंगूर)'
    elif predict1 == 8:
        crop_name = 'Jute(जूट)'
    elif predict1 == 9:
        crop_name = 'Kidneybeans(राज़में)'
    elif predict1 == 10:
        crop_name = 'Lentil(मसूर की दाल)'
    elif predict1 == 11:
        crop_name = 'Maize(मक्का)'
    elif predict1 == 12:
        crop_name = 'Mango(आम)'
    elif predict1 == 13:
        crop_name = 'Mothbeans(मोठबीन)'
    elif predict1 == 14:
        crop_name = 'Mungbeans(मूंग)'
    elif predict1 == 15:
        crop_name = 'Muskmelon(खरबूजा)'
    elif predict1 == 16:
        crop_name = 'Orange(संतरा)'
    elif predict1 == 17:
        crop_name = 'Papaya(पपीता)'
    elif predict1 == 18:
        crop_name = 'Pigeonpeas(कबूतर के मटर)'
    elif predict1 == 19:
        crop_name = 'Pomegranate(अनार)'
    elif predict1 == 20:
        crop_name = 'Rice(चावल)'
    elif predict1 == 21:
        crop_name = 'Watermelon(तरबूज)'

    if int(humidity_content) >= 1 and int(humidity_content) <= 33:  # Here I have divided the humidity values into three categories i.e low humid, medium humid, high humid.
        humidity_level = 'low humid'
    elif int(humidity_content) >= 34 and int(humidity_content) <= 66:
        humidity_level = 'medium humid'
    else:
        humidity_level = 'high humid'

    if int(temperature_content) >= 0 and int(temperature_content) <= 6:  # Here I have divided the temperature values into three categories i.e cool, warm, hot.
        temperature_level = 'cool'
    elif int(temperature_content) >= 7 and int(temperature_content) <= 25:
        temperature_level = 'warm'
    else:
        temperature_level = 'hot'

    if int(rainfall) >= 1 and int(rainfall) <= 100:  # Here I have divided the humidity values into three categories i.e less, moderate, heavy rain.
        rainfall_level = 'less'
    elif int(rainfall) >= 101 and int(rainfall) <= 200:
        rainfall_level = 'moderate'
    elif int(rainfall) >= 201:
        rainfall_level = 'heavy rain'

    if int(nitrogen_content) >= 1 and int(nitrogen_content) <= 50:  # Here I have divided the nitrogen values into three categories.
        nitrogen_level = 'less'
    elif int(nitrogen_content) >= 51 and int(nitrogen_content) <= 100:
        nitrogen_level = 'not to less but also not to high'
    elif int(nitrogen_content) >= 101:
        nitrogen_level = 'high'

    if int(phosphorus_content) >= 1 and int(phosphorus_content) <= 50:  # Here I have divided the phosphorus values into three categories.
        phosphorus_level = 'less'
    elif int(phosphorus_content) >= 51 and int(phosphorus_content) <= 100:
        phosphorus_level = 'not to less but also not to high'
    elif int(phosphorus_content) >= 101:
        phosphorus_level = 'high'

    if int(potassium_content) >= 1 and int(potassium_content) <= 50:  # Here I have divided the potassium values into three categories.
        potassium_level = 'less'
    elif int(potassium_content) >= 51 and int(potassium_content) <= 100:
        potassium_level = 'not to less but also not to high'
    elif int(potassium_content) >= 101:
        potassium_level = 'high'

    if float(ph_content) >= 0 and float(ph_content) <= 5:  # Here I have divided the ph values into three categories.
        phlevel = 'acidic'
    elif float(ph_content) >= 6 and float(ph_content) <= 8:
        phlevel = 'neutral'
    elif float(ph_content) >= 9 and float(ph_content) <= 14:
        phlevel = 'alkaline'

    print(crop_name)
    print(humidity_level)
    print(temperature_level)
    print(rainfall_level)
    print(nitrogen_level)
    print(phosphorus_level)
    print(potassium_level)
    print(phlevel)

    # speak(
    #     "Sir according to the data that you provided to me. The ratio of nitrogen in the soil is  " + nitrogen_level + ". The ratio of phosphorus in the soil is  " + phosphorus_level + ". The ratio of potassium in the soil is  " + potassium_level + ". The temperature level around the field is  " + temperature_level + ". The humidity level around the field is  " + humidity_level + ". The ph type of the soil is  " + phlevel + ". The amount of rainfall is  " + rainfall_level)  # Making our program to speak about the data that it has received about the crop in front of the user.
    # window['-OUTPUT1-'].update(
    #     'The best crop that you can grow : ' + crop_name)  # Suggesting the best crop after prediction.
    # speak("The best crop that you can grow is  " + crop_name)  # Speaking the name of the predicted crop.
    print(crop_name)

def back():
    root.destroy()
    import front

root = Tk()
root.geometry("1920x1080")

bg = PhotoImage(file="farm1.png")

my_canvas = Canvas(root, width=1920, height=1080)
my_canvas.pack(fill="both", expand=True)

my_canvas.create_image(0, 0, image=bg, anchor="nw")
my_canvas.create_text(800, 80, text="Enter the following Details :-", font=("Times New Roman", 45), fill="green")
my_canvas.create_text(500, 160, text=" Enter ratio of Nitrogen in the soil                    ",
                      font=("Times New Roman", 30), fill="white")
my_canvas.create_text(500, 230, text="  Enter ratio of Potassium in the soil                  ",
                      font=("Times New Roman", 30), fill="white")
my_canvas.create_text(500, 300, text="   Enter ratio of Phosphorus in the soil                 ",
                      font=("Times New Roman", 30), fill="white")
my_canvas.create_text(500, 370, text="           Enter Average Temperature around the field            ",
                      font=("Times New Roman", 30), fill="white")
my_canvas.create_text(500, 440, text="                 Enter Average Percentage of Humidity around the field ",
                      font=("Times New Roman", 30), fill="white")
my_canvas.create_text(500, 510, text="   Enter the pH value of the soil                            ",
                      font=("Times New Roman", 30), fill="white")
my_canvas.create_text(500, 580, text="              Enter Average amount of Rainfall around the field     ",
                      font=("Times New Roman", 30), fill="white")
my_canvas.create_text(1420, 370, text="Celsius", font=("Arial", 20), fill="white")
my_canvas.create_text(1420, 440, text="%", font=("Times New Roman", 20), fill="white")
my_canvas.create_text(1420, 580, text="mm", font=("Times New Roman", 20), fill="white")
my_canvas.create_text(1100, 160, text=":", font=("Times New Roman", 30), fill="white")
my_canvas.create_text(1100, 230, text=":", font=("Times New Roman", 30), fill="white")
my_canvas.create_text(1100, 300, text=":", font=("Times New Roman", 30), fill="white")
my_canvas.create_text(1100, 370, text=":", font=("Times New Roman", 30), fill="white")
my_canvas.create_text(1100, 440, text=":", font=("Times New Roman", 30), fill="white")
my_canvas.create_text(1100, 510, text=":", font=("Times New Roman", 30), fill="white")
my_canvas.create_text(1100, 580, text=":", font=("Times New Roman", 30), fill="white")

'''
content1_value=StringVar
content2_value=StringVar
content3_value=StringVar
content4_value=StringVar
content5_value=StringVar
content6_value=StringVar
content7_value=StringVar
'''
# values=[[0,1,2,3,4,5,6]]
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


button1 = Button(root, text="Predict", font=("Times New Roman", 25),command=predict0)
button1_window = my_canvas.create_window(750, 700, window=button1)
button2 = Button(root, text="Back", font=("Times New Roman", 10), command=back)
button2_window = my_canvas.create_window(0, 0, anchor=NW, window=button2)

'''label = Label(root, text='')
label_window = my_canvas.create_window(0, 0, anchor=NW, window=label)
answer = Label(root, text='')
answer.pack(pady=20)'''

root.mainloop()



