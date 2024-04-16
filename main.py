import customtkinter as ctk
from PIL import Image, ImageTk
import os.path
from customtkinter import filedialog
import pytesseract
import os
import cv2
import numpy as np


tessdata_dir = r"C:\Program Files\Tesseract-OCR\tessdata"
os.environ["TESSDATA_PREFIX"] = tessdata_dir

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


app = ctk.CTk()
app.title("OCR-App")
app.geometry("560x450")
app.resizable(False, False)

def add_image():
    file = filedialog.askopenfile(mode="r", filetypes=[("Image files", "*.jpg *.png *.jpeg")])
    if file is not None:
        filepath = os.path.abspath(file.name)
        En1.insert(0, filepath)

def extract_text():
    image_path = En1.get()
    save_path = En2.get()
    language = En3.get()
    text = pytesseract.image_to_string(image_path, lang=language)
    with open(save_path, "w") as file:
        file.write(text)


# Frame setup
frame1 = ctk.CTkFrame(app, width=560, height=450, bg_color="white")
frame1.place(x=1, y=1)

# Labels and entries
label = ctk.CTkLabel(frame1, text="OCR-App:", font=("Arial", 22))
label.place(x=1, y=4)

En1_text = ctk.CTkLabel(frame1, text="Enter the path of the image:", font=("Arial", 18))
En1_text.place(x=10, y=51)
En1 = ctk.CTkEntry(frame1, width=200, font=("Arial", 16), bg_color="white", fg_color="black")
En1.place(x=250, y=50)

btn_1 = ctk.CTkButton(frame1, text="---->ADD<----", bg_color="blue", fg_color="white", command=add_image)
btn_1.place(x=450, y=50)

En2_text = ctk.CTkLabel(frame1, text="Enter the path for the Save:", font=("Arial", 18))
En2_text.place(x=10, y=84)
En2 = ctk.CTkEntry(frame1, width=200, font=("Arial", 16), bg_color="white", fg_color="black")
En2.place(x=250, y=84)

En3_text = ctk.CTkLabel(frame1, text="Language", font=("Arial", 18))
En3_text.place(x=10, y=117)
En3 = ctk.CTkEntry(frame1, width=200, font=("Arial", 16), bg_color="white", fg_color="black", placeholder_text="eng")
En3.place(x=250, y=117)

button_1 = ctk.CTkButton(frame1, text="Extract Text", bg_color="blue", fg_color="white", command=extract_text)
button_1.place(x=275, y=150)

# Load and resize the image
image_path = "logo.jpg"
img = Image.open(image_path)
img = img.resize((500, 240), Image.ANTIALIAS)  # Resize the image
photo = ImageTk.PhotoImage(img)

# Display resized image
label = ctk.CTkLabel(frame1, image=photo)
label.image = photo  # Keep a reference to avoid garbage collection
label.place(x=30, y=200)

app.mainloop()
