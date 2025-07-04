import customtkinter as ctk  
from tkinter import filedialog
from PIL import Image, ImageEnhance, ImageTk, ImageFilter, ImageOps
import tkinter.messagebox
import tkinter.simpledialog

# Try to import screeninfo, fallback to default size if not available
try:
    from screeninfo import get_monitors
    w = ''
    h = ''
    for i in str(get_monitors()).split(' '):
        if('width=' in i):
            w = str(int(int(i[6:-1])/1.4))
        if('height=' in i):
            h = str(int(int(i[7:-1])/1.4))
    if not w or not h:
        w, h = '1200', '800'
except ImportError:
    # Default window size if screeninfo is not available
    w, h = '1200', '800'

def open_image():
    global original_image, display_image, enhanced_image, undo_stack
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp *.tiff"), ("All files", "*.*")]
    )
    if file_path:
        try:
            original_image = Image.open(file_path)
            original_image.thumbnail((1460, 860))
            enhanced_image = original_image.copy() 
            undo_stack = [(original_image.copy(), 1.0, 1.0, 0.0)]  
            blur_slider.set(0.0)
            brightness_slider.set(1.0)
            contrast_slider.set(1.0)
            update_image()
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Error opening image: {str(e)}")


def update_image():
    global original_image, display_image, enhanced_image, undo_stack
    if original_image:
        try:
            contrast_value = contrast_slider.get()
            brightness_value = brightness_slider.get()
            blur_value = blur_slider.get()
            
            # Always start from the original image to avoid cumulative effects
            temp_image = enhanced_image.copy()
            temp_image = ImageEnhance.Contrast(temp_image).enhance(contrast_value)
            temp_image = ImageEnhance.Brightness(temp_image).enhance(brightness_value)
            if blur_value > 0:
                temp_image = temp_image.filter(ImageFilter.GaussianBlur(blur_value))
            
            # Create a copy for display
            display_temp = temp_image.copy()
            display_temp.thumbnail((1460, 860))
            display_image = ImageTk.PhotoImage(display_temp)
            img_label_edited.configure(image=display_image)
            img_label_edited.image = display_image
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Error updating image: {str(e)}")
 
def slider_released(event):
    global enhanced_image, undo_stack
    try:
        # Apply the current slider values to create the new enhanced image
        contrast_value = contrast_slider.get()
        brightness_value = brightness_slider.get()
        blur_value = blur_slider.get()
        
        # Start from original and apply all effects
        temp_image = original_image.copy()
        temp_image = ImageEnhance.Contrast(temp_image).enhance(contrast_value)
        temp_image = ImageEnhance.Brightness(temp_image).enhance(brightness_value)
        if blur_value > 0:
            temp_image = temp_image.filter(ImageFilter.GaussianBlur(blur_value))
        
        enhanced_image = temp_image.copy()
        update_image()
        undo_stack.append((enhanced_image.copy(), contrast_value, brightness_value, blur_value))
    except Exception as e:
        tkinter.messagebox.showerror("Error", f"Error applying changes: {str(e)}")

def adjust_contrast(value=None):
    if original_image:
        update_image()

def adjust_brightness(value=None):
    if original_image:
        update_image()

def adjust_blur(value=None):
    if original_image:
        update_image()


def undo_changes():
    global display_image, enhanced_image, undo_stack
    try:
        if len(undo_stack) > 1:  # Check if there are previous states
            undo_stack.pop()  # Remove current state
            enhanced_image, contrast_value, brightness_value, blur_value = undo_stack[-1]  # Get previous state
            
            # Update sliders to match the previous state
            contrast_slider.set(contrast_value)
            brightness_slider.set(brightness_value)
            blur_slider.set(blur_value)
            
            # Update the display
            update_image()
        elif len(undo_stack) <= 1 and original_image:
            # Reset to original image
            enhanced_image = original_image.copy()   
            contrast_slider.set(1.0)
            brightness_slider.set(1.0)
            blur_slider.set(0.0)
            undo_stack = [(enhanced_image.copy(), 1.0, 1.0, 0.0)]
            update_image()
    except Exception as e:
        tkinter.messagebox.showerror("Error", f"Error undoing changes: {str(e)}")

def save_image():
    global enhanced_image
    if enhanced_image:
        try:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".jpg",
                filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("BMP files", "*.bmp"), ("All files", "*.*")]
            )
            if file_path:
                # Apply current slider settings to get the final image
                contrast_value = contrast_slider.get()
                brightness_value = brightness_slider.get()
                blur_value = blur_slider.get()
                
                # Create final image with all effects
                final_image = enhanced_image.copy()
                final_image = ImageEnhance.Contrast(final_image).enhance(contrast_value)
                final_image = ImageEnhance.Brightness(final_image).enhance(brightness_value)
                if blur_value > 0:
                    final_image = final_image.filter(ImageFilter.GaussianBlur(blur_value))
                
                final_image.save(file_path)
                tkinter.messagebox.showinfo("Success", "Image saved successfully!")
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Error saving image: {str(e)}")
    else:
        tkinter.messagebox.showwarning("Warning", "No image to save. Please open an image first.")

def resize_image():
    global original_image, enhanced_image, display_image, undo_stack

    if not enhanced_image:
        tkinter.messagebox.showwarning("Warning", "No image to resize. Please open an image first.")
        return

    try:
        tkinter.messagebox.showinfo("Resize Image", "Please enter the new width and height of the image.")
        dialog_width = ctk.CTkInputDialog(text="Enter the new width:", title="Resize Image")
        width_input = dialog_width.get_input()
        
        if not width_input:  # User cancelled
            return
            
        dialog_height = ctk.CTkInputDialog(text="Enter the new height:", title="Resize Image")
        height_input = dialog_height.get_input()
        
        if not height_input:  # User cancelled
            return

        new_width = int(width_input)
        new_height = int(height_input)

        if new_width > 0 and new_height > 0:
            # Save current state to undo stack
            undo_stack.append((enhanced_image.copy(), contrast_slider.get(), brightness_slider.get(), blur_slider.get()))
            
            # Resize the enhanced image
            resized_image = enhanced_image.resize((new_width, new_height))
            enhanced_image = resized_image.copy()
            update_image()
        else:
            tkinter.messagebox.showerror("Error", "Width and height must be positive numbers.")

    except ValueError:
        tkinter.messagebox.showerror("Error", "Please enter valid numeric values for width and height.")
    except Exception as e:
        tkinter.messagebox.showerror("Error", f"Error resizing image: {str(e)}")



def grayscale_image():
    global enhanced_image, display_image, undo_stack
    if enhanced_image:
        try:
            # Save current state to undo stack
            undo_stack.append((enhanced_image.copy(), contrast_slider.get(), brightness_slider.get(), blur_slider.get()))
            
            # Convert to grayscale - need to convert back to RGB mode for further editing
            enhanced_image = ImageOps.grayscale(enhanced_image).convert('RGB')
            update_image()
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Error converting to grayscale: {str(e)}")
    else:
        tkinter.messagebox.showwarning("Warning", "No image to convert. Please open an image first.")

def reset_image():
    global original_image, display_image, enhanced_image, undo_stack
    if original_image:
        try:
            enhanced_image = original_image.copy()
            undo_stack = [(enhanced_image.copy(), 1.0, 1.0, 0.0)]  
            contrast_slider.set(1.0)
            brightness_slider.set(1.0)
            blur_slider.set(0.0)
            update_image()
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Error resetting image: {str(e)}")
    else:
        tkinter.messagebox.showwarning("Warning", "No image to reset. Please open an image first.")
    

root = ctk.CTk()
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
root.title("Image Editor")
window_size = w+'x'+h
root.geometry(window_size)
root.resizable(True, True)


picframe = ctk.CTkFrame(master=root,width=1500,height=860,corner_radius=10)
picframe.place(relx=0.01, rely=0.02)

toolsframe = ctk.CTkFrame(master=root,width=350,height=860,corner_radius=10)
toolsframe.place(relx=0.99, rely=0.02, anchor="ne")

original_image = None
display_image = None
enhanced_image = None
undo_stack = [] 

open_button = ctk.CTkButton(root, text="Open Image", command=open_image)
open_button.place(relx=0.935, rely=0.09, anchor="ne")

contrast_label = ctk.CTkLabel(root, text="Adjust Contrast:")
contrast_label.place(relx=0.923, rely=0.15, anchor="ne")

contrast_slider = ctk.CTkSlider(root, from_=0.1, to=2, number_of_steps=19, orientation="horizontal")
contrast_slider.set(1.0)
contrast_slider.bind("<ButtonRelease-1>", slider_released)
contrast_slider.place(relx=0.951, rely=0.20, anchor="ne")

brightness_label = ctk.CTkLabel(root, text="Adjust Brightness:")
brightness_label.place(relx=0.927, rely=0.25, anchor="ne")

brightness_slider = ctk.CTkSlider(root, from_=0.1, to=2, number_of_steps=19, orientation="horizontal")
brightness_slider.set(1.0)
brightness_slider.bind("<ButtonRelease-1>", slider_released)
brightness_slider.place(relx=0.951, rely=0.30, anchor="ne")

blur_label = ctk.CTkLabel(root, text="Adjust Blur:")
blur_label.place(relx=0.918, rely=0.35, anchor="ne")

blur_slider = ctk.CTkSlider(root, from_=0.0, to=5.0, number_of_steps=50, orientation="horizontal")
blur_slider.set(0.0)
blur_slider.bind("<ButtonRelease-1>", slider_released)
blur_slider.place(relx=0.951, rely=0.40, anchor="ne")

grayscale_button = ctk.CTkButton(root, text="Grayscale", command=grayscale_image)
grayscale_button.place(relx=0.935, rely=0.45, anchor="ne")

resize_button = ctk.CTkButton(root, text="Resize Image", command=resize_image)
resize_button.place(relx=0.935, rely=0.50, anchor="ne")

save_button = ctk.CTkButton(root, text="Save Image", command=save_image)
save_button.place(relx=0.980, rely=0.55, anchor="ne")

undo_button = ctk.CTkButton(root, text="Undo", command=undo_changes)
undo_button.place(relx=0.890, rely=0.55, anchor="ne")

reset_button = ctk.CTkButton(root, text="Reset Image", command=reset_image)
reset_button.place(relx=0.935, rely=0.60, anchor="ne")

img_label_edited = ctk.CTkLabel(picframe, text="‎")
img_label_edited.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()