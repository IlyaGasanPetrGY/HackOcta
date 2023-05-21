# This is a sample Python script.
from tkinter import *
from tkinter import filedialog
import os
import shutil
from PIL import Image, ImageTk
import torch
# from PIL import Image
import cv2
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

ORIGIN_PATH = os.getcwd()
print(ORIGIN_PATH)
def uploadBtn():
    file = filedialog.askopenfilename()
    filename = file.split('/')[-1]
    file_dir = file[0:-len(filename)-1]
    # print(filename, file_dir, file)
    new_img = Image.open(file)
    new_img.save(f'{ORIGIN_PATH}\\storage\\{filename}')
    window.title('Ожидайте')
    os.system(f'python ./yolov5/detect.py --weights ./models/best.pt  --img 640 --source ./storage/{filename}')

    # for file in os.listdir('./yolov5/runs/detect/'):
    # print(os.listdir('./yolov5/runs/detect/')[-1])

    img = Image.open(f'./yolov5/runs/detect/' + os.listdir('./yolov5/runs/detect/')[-1] + '/' + filename)
    img.show()


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
