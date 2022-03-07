# miles to kilometer converter application
import tkinter
win = tkinter.Tk()
win.title("Mile to Km Converter")
win.minsize(width=400, height=400)
win.maxsize(width=400, height=400)

def convert_and_set():
    CONST = 1.60934
    miles_value = int(input.get())
    km_value = int(miles_value*CONST)
    lable_output["text"] = km_value

input = tkinter.Entry()
input.grid(column=1, row=0)

label_miles = tkinter.Label(text="Miles")
label_miles.grid(column=2, row=0)

label_equal = tkinter.Label(text="is equal to")
label_equal.grid(column=0, row=1)

lable_output = tkinter.Label(text="0")
lable_output.grid(column=1, row=1)

label_kilometers = tkinter.Label(text="Km")
label_kilometers.grid(column=2, row=1)

button = tkinter.Button(text="Calculate")
button.grid(column=1, row=2)
button.config(command=convert_and_set)

win.mainloop()