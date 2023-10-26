from tkinter import *



def print_stars():
    print
    "**************"

def print_hi(name):
    app = Tk()
    app.title("Base Gui")
    app.geometry("200x100+400+300")
    app.configure(bg="green")

    Label(app, text="Number to convert:").pack()
    numToConvert = Entry(app)
    numToConvert.pack()
    app.mainloop()
    num = int(numToConvert.get())
    print(num)


if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
