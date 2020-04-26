#********************************************************
# Hand Written Digit Identifier 
#********************************************************

import tkinter as tk
from PIL import ImageTk,Image,ImageDraw
from matplotlib import pyplot as plt
import numpy as np
import cv2

#function for drowing
def event(event):

    x=event.x
    y=event.y

    x1=x-30
    y1=y-30
    
    x2=x+30
    y2=y+30
    
    canvas.create_oval((x1,y1,x2,y2),fill='black')
    img_draw.ellipse((x1,y1,x2,y2),fill='white')


#function for clear the canvse
def clear():

    global img,img_draw
    canvas.delete('all')
    img=Image.new('RGB',(400,400),(0,0,0))
    img_draw=ImageDraw.Draw(img)
    label_predict.config(text='PREDICTION : NONE')

#function for prediction
def predict():

    img_array=np.array(img) #converting to numpy array
    img_array=cv2.cvtColor(img_array,cv2.COLOR_BGR2GRAY) #converting into a gray image
    img_array=cv2.resize(img_array,(8,8)) #resizing into 8x8

    plt.imshow(img_array,cmap='binary')
    
    img_array=np.reshape(img_array,(1,64))  #reshaping into 1x64
    img_array=img_array/255.0*15.0

    result=clsfr.predict(img_array)
    label_predict.config(text='PREDICTION :'+ str(result))

    
   
from sklearn.datasets import load_digits

#load the dataset
dataset=load_digits()
data=dataset.data
target=dataset.target


from sklearn import svm

clsfr=svm.SVC(kernel='linear')
clsfr.fit(data,target)




frame=tk.Tk()
#frame size
frame.geometry('500x500')
pic=tk.PhotoImage(file="original.gif")
tk.Label(frame,image=pic,bg="black").place(x=0,y=240)

frame.title("Hand Written digit Identifier")
frame.configure(background="black")

#make the canvas 
canvas=tk.Canvas(frame,width=500,height=400,bg='white')
canvas.grid(row=0,column=0,columnspan=4) #note columnspan !!

canvas.bind('<B1-Motion>',event)

img=Image.new('RGB',(400,400),(0,0,0))
img_draw=ImageDraw.Draw(img)


tk.Label(frame,text="Please Press & Drow slowly using mouse ",bg='white',fg="red",font="none 12 bold").place(x=50, y=0)

tk.Button(frame,width=10,text='Predict',fg='blue',bg='green2',font="none 12 bold",command=predict).place(x=8,y=410)
tk.Button(frame,bg='firebrick2',text='Clear',width=10,fg='white',font="none 12 bold",command=clear).place(x=8,y=455)
tk.Button(frame,text='Close',bg='red',fg='white',font="none 14 bold",command=frame.destroy).place(x=390,y=455)

label_predict=tk.Label(frame,text='PREDICTION : NONE',bg='black',fg='white',font='Helvetica 18 bold')
label_predict.place(x=150,y=410)
frame.mainloop()
