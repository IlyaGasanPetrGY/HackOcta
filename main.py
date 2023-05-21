# This is a sample Python script.
from tkinter import *
from tkinter import filedialog
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def uploadBtn():
    file = filedialog.askopenfilename()

window = Tk()
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
w = w//2 # середина экрана
h = h//2
w = w - 300 # смещение от середины
h = h - 300
window.geometry('970x600+{}+{}'.format(w, h))
window.resizable(False, False)
# window.configure(background="blue")
window.title("Определение отдельных видов")
# C = Canvas(window, bg="blue", height=250, width=300)
bg = PhotoImage(file="img/bg.PNG")
background_label = Label(window, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
# file = filedialog.askopenfilename()
btn = PhotoImage(file='img/btn.png')
btn_upload = Button(window, image=btn, border=0, command=uploadBtn).place(x=300, y=350)
# btn_upload.pack()
window.mainloop()

# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
