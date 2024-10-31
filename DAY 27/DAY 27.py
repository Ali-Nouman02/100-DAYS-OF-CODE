# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
#
# print(add(10, 30, 10))


# from tkinter import *
#
# window = Tk()
# window.title("My First GUI Program")
# window.minsize(width = 500, height = 300)
#
#
# #Label
#
# my_label = Label(text = "I am a Label", font = ("Arial", 24, "bold"))
# #position the label
# # my_label.pack(side = 'left')
# #grid does the same thing but you can not use both at the same time
# my_label.grid(column= 0, row = 0)
#
#
# #change the label to new text option 1
# my_label['text'] = "New Text"
# #change the label to new text option 2
# my_label.config(text = "New Text")
#
# # Button
#
# def button_clicked():
#     value = input.get()
#     my_label.config(text=value)
#
# button = Button(text = "Click Me", command= button_clicked)
# button.grid(column= 1, row = 1)
# # button.pack()
#
#
# # #Entry
# #
# # input = Entry(width = 10 )
# # input.grid(column= 3, row = 3)
# # # input.pack()
# # print(input.get())
#
#
# #Second Button
#
# button_2 = Button(text = "Click Me", command= button_clicked)
# button_2.grid(column= 2, row = 0)
# # button.pack()
#
#
#
# window.mainloop()

######## DAY 27 PROJECT  ########
#MILES TO KM CONVERTER GUI USING TKINTER
from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width = 300, height = 150)


#Entry

input = Entry(width = 10 )
input.grid(column= 1, row = 0)

#my_label- "MILES"
my_label_miles = Label(text = "Miles", font = ("Arial", 12))
my_label_miles.grid(column= 2, row = 0)

#my_label
my_label = Label(text = "is equal to", font = ("Arial", 12))
my_label.grid(column= 0, row = 3)

#my_label- Result
my_label_result = Label(text = "0", font = ("Arial", 12))
my_label_result.grid(column= 1, row = 3)

#my_label- KM
my_label_km = Label(text = "Km", font = ("Arial", 12))
my_label_km.grid(column= 2, row = 3)

#Button
def button_clicked():
    m = int(input.get())
    km = m * 1.609344
    my_label_result.config(text=km)

button = Button(text = "Calculate", command= button_clicked)
button.grid(column= 1, row = 4)

window.mainloop()