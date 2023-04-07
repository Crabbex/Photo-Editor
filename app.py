from PIL import Image, ImageEnhance, ImageFilter
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import ctypes

ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0 )

path = r"Path to my picture"
pathOut = r"Path to where I want the edited photo to go"

Tk().withdraw()
filename = askopenfilename()

for filename in os.listdir(path):
    img = Image.open(fr"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN).convert("L")

    clean_name = os.path.splitext(filename)[0]

    edit.save(f"{pathOut}/{clean_name}_edited.jpg")
