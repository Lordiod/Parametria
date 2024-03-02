import customtkinter as ctk  
from tkinter import filedialog
from PIL import Image, ImageEnhance, ImageTk, ImageFilter, ImageOps
import tkinter.messagebox
import tkinter.simpledialog
from screeninfo import get_monitors

w = ''
h = ''
for i in str(get_monitors()).split(' '):
    if('width=' in i):
        w = str(int(int(i[6:-1])/1.4))
    if('height=' in i):
        h = str(int(int(i[7:-1])/1.4))

def open_image():
    global original_image,display_image, enhanced_image,undo_stack
    file_path = filedialog.askopenfilename()
    if file_path:
        original_image = Image.open(file_path)
        original_image.thumbnail((1460, 860))
        enhanced_image = original_image.copy() 
        undo_stack = [(original_image.copy(), 1.0, 1.0, 0.0)]  
        blur_slider.set(0.0)
        brightness_slider.set(1.0)
        contrast_slider.set(1.0)
        update_image()  


def update_image():
    global original_image, display_image, enhanced_image, undo_stack
    if enhanced_image:
        contrast_value = contrast_slider.get()
        brightness_value = brightness_slider.get()
        blur_value = blur_slider.get()
        
        enhanced_image = ImageEnhance.Contrast(enhanced_image).enhance(contrast_value)
        enhanced_image = ImageEnhance.Brightness(enhanced_image).enhance(brightness_value)
        enhanced_image = enhanced_image.filter(ImageFilter.GaussianBlur(blur_value))
        
        enhanced_image.thumbnail((1460, 860))
        display_image = ImageTk.PhotoImage(enhanced_image)
        img_label_edited.configure(image=display_image)
        img_label_edited.image = display_image
 
def slider_released(event):
    global enhanced_image, undo_stack
    update_image()
    undo_stack.append((enhanced_image.copy(), contrast_slider.get(), brightness_slider.get(), blur_slider.get()))

def adjust_contrast(value=None):
    update_image()  

def adjust_brightness(value=None):
    update_image()  

def adjust_blur(value=None):
    update_image()


def undo_changes():
    global display_image, enhanced_image, undo_stack
    if len(undo_stack) > 1:  # Check if the undo stack is not empty
        undo_stack.pop()# Pop the last state and the values from the undo stack
        enhanced_image, contrast_value, brightness_value, blur_value = undo_stack[-1]  # Get the previous state and the values
        display_image = ImageTk.PhotoImage(enhanced_image)
        img_label_edited.configure(image=display_image)
        img_label_edited.image = display_image
        
        contrast_slider.set(contrast_value)
        brightness_slider.set(brightness_value)
        blur_slider.set(blur_value)

    elif len(undo_stack) <= 1 : 
        enhanced_image = original_image.copy()   
        display_image = ImageTk.PhotoImage(enhanced_image)
        img_label_edited.configure(image=display_image)
        img_label_edited.image = display_image

        contrast_slider.set(1.0)
        brightness_slider.set(1.0)
        blur_slider.set(0)

def save_image():
    global enhanced_image
    if enhanced_image:
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg",
                                                 filetypes=[("JPEG files", ".jpg"), ("PNG files", ".png"), ("BMP files", ".bmp"), ("All files", ".*")])
        if file_path:
            enhanced_image.save(file_path)

def resize_image():
    global original_image, enhanced_image, display_image, undo_stack

    try:
        tkinter.messagebox.showinfo("Resize Image", "Please enter the new width and height of the image.")
        dialog_width = ctk.CTkInputDialog(text="Enter the new width:", title="Resize Image")
        new_width = int(dialog_width.get_input())
        dialog_height = ctk.CTkInputDialog(text="Enter the new height:", title="Resize Image")
        new_height = int(dialog_height.get_input())

        if new_width and new_height:
            #undo_stack.append((enhanced_image.copy(), contrast_slider.get(), brightness_slider.get(), blur_slider.get()))
            resized_image = enhanced_image.resize((new_width, new_height))
            enhanced_image = resized_image.copy()
            undo_stack.append((enhanced_image.copy(), contrast_slider.get(), brightness_slider.get(), blur_slider.get()))
            update_image()

    except ValueError:
        tkinter.messagebox.showerror("Error", "Please enter valid numeric values for width and height.")



def grayscale_image():
    global enhanced_image, display_image, undo_stack
    if enhanced_image:
        enhanced_image = ImageOps.grayscale(enhanced_image)  # Create a grayscale version
        undo_stack.append((enhanced_image.copy(), contrast_slider.get(), brightness_slider.get(), blur_slider.get()))
        update_image()

def reset_image():
    global original_image, display_image, enhanced_image, undo_stack
    enhanced_image = original_image.copy()
    undo_stack = [(enhanced_image, 1.0, 1.0, 0.0)]  
    contrast_slider.set(1.0)
    brightness_slider.set(1.0)
    blur_slider.set(0.0)
    update_image()
    

root = ctk.CTk()
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
root.title("Image Editor")
w = w+'x'+h
root.geometry(w)
root.resizable(1,1)


picframe = ctk.CTkFrame(master=root,width=1500,height=860,corner_radius=10)
picframe.place(relx=0.01, rely=0.02)

toolsframe = ctk.CTkFrame(master=root,width=350,height=860,corner_radius=10)
toolsframe.place(relx=0.99, rely=0.02, anchor="ne")

original_image = None
display_image = None
enhanced_image = None
undo_stack = [] 

open_button = ctk.CTkButton(root, text="Open Image", command=open_image)
open_button.pack()
open_button.place(relx=0.935, rely=0.09, anchor="ne")

contrast_label = ctk.CTkLabel(root, text="Adjust Contrast:")
contrast_label.pack()
contrast_label.place(relx=0.923, rely=0.15, anchor="ne")

contrast_slider = ctk.CTkSlider(root, from_=0.1, to=2, number_of_steps=19, orientation="horizontal")
contrast_slider.set(1.0)
contrast_slider.pack()
contrast_slider.bind("<ButtonRelease-1>", slider_released)
contrast_slider.place(relx=0.951, rely=0.20, anchor="ne")


brightness_label = ctk.CTkLabel(root, text="Adjust Brightness:")
brightness_label.pack()
brightness_label.place(relx=0.927, rely=0.25, anchor="ne")


brightness_slider = ctk.CTkSlider(root, from_=0.1, to=2, number_of_steps=19, orientation="horizontal")
brightness_slider.set(1.0)
brightness_slider.pack()
brightness_slider.bind("<ButtonRelease-1>", slider_released)
brightness_slider.place(relx=0.951, rely=0.30, anchor="ne")

blur_label = ctk.CTkLabel(root, text="Adjust Blur:")
blur_label.pack()
blur_label.place(relx=0.918, rely=0.35, anchor="ne")

blur_slider = ctk.CTkSlider(root, from_=0.0, to=5.0, number_of_steps=50, orientation="horizontal")
blur_slider.set(0.0)
blur_slider.pack()
blur_slider.bind("<ButtonRelease-1>", slider_released)
blur_slider.place(relx=0.951, rely=0.40, anchor="ne")

undo_button = ctk.CTkButton(root, text="Undo", command=undo_changes)
undo_button.pack()
undo_button.place(relx=0.890, rely=0.55, anchor="ne")

reset_button = ctk.CTkButton(root, text="Reset Image", command=reset_image)
reset_button.pack()
reset_button.place(relx=0.935, rely=0.60, anchor="ne")

save_button = ctk.CTkButton(root, text="Save Image", command=save_image)
save_button.pack()
save_button.place(relx=0.980, rely=0.55, anchor="ne")

resize_button = ctk.CTkButton(root, text="Resize Image", command=resize_image)
resize_button.pack()
resize_button.place(relx=0.935, rely=0.50, anchor="ne")

grayscale_button = ctk.CTkButton(root, text="Grayscale Image", command=grayscale_image)
grayscale_button.pack()
grayscale_button.place(relx=0.935, rely=0.45, anchor="ne")

img_label_edited = ctk.CTkLabel(picframe,text="‎")
img_label_edited.pack()
img_label_edited.place(relx=0.4, rely=0.5, anchor="center")

root.mainloop()