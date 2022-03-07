# Graphical user interfaces, args and kwargs
import tkinter

window = tkinter.Tk() #creating a window
window.title("My First GUI program")
# the window will scale in size to fit all the components inside it but we can change the size specs if we don't have a lot to offer
window.minsize(width=500, height=300)
window.maxsize(width=500, height=300)

# label
my_label = tkinter.Label(text="I am a Label", font=("Verdana",24, "bold"))
# my_label.pack()#placing and automatically centering in the screen: side="left" expand = true
my_label["text"] = "New label text"
# my_label.place(x=100, y=3)
my_label.grid(column=0, row=0)

# buttons
def button_clicked():
    my_label.config(text="You Clicked The Button")

button = tkinter.Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

# inpput component
input = tkinter.Entry()
# input.pack()
input.grid(column=2, row=2)
input.config(width=10)
def change_label_with_input():
    my_label["text"] = input.get()

button.config(command=change_label_with_input)

window.mainloop() #keeps the window

# functions with unlimited arguements
def add(*args): #args can be any name
    for n in args:
        print(n)
add(10, 3, 4, 8)

def add_digits(*digits):
    # print(digits[1]) #we can also print the specific item
    total = 0
    for digit in digits:
        total += digit
    return total

print(add_digits(10, 15, 33, 88))
print(add_digits(10, 15))

# in the above examples, *args and *digits are tuples

# Many keyword arguements
def calculate(**kwargs):
    # print(kwargs)
    for (key, value) in kwargs.items():
        print(key)
        print(value)


calculate(add=3, multipy=5, subtract=8)#this is just a dictionary being created with the arguements
# {'add': 3, 'multipy': 5, 'subtract': 8}
def arithmetics(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(f"Value of n is {n}")
arithmetics(5, add=3, multiply=5, subtract=8)

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]
        self.tyres = kw.get("tyres")
        self.color = kw.get("color") #if we dont specify it and try to acces it, it will simply return none, ie if we use get()

my_car = Car(make="Nissan", model="GT-R")
print(my_car.make)
print(my_car.model)
print(my_car.color)


    
