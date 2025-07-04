from PIL import Image, ImageEnhance, ImageFilter, ImageOps, ImageTk
from tkinter import filedialog
import tkinter.messagebox
from typing import Optional, Tuple
import config

class ImageProcessor:
    """Service class for image processing operations"""
    
    @staticmethod
    def load_image(file_path: str) -> Optional[Image.Image]:
        """Load an image from file path"""
        try:
            image = Image.open(file_path)
            image.thumbnail(config.MAX_IMAGE_SIZE)
            return image
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Error opening image: {str(e)}")
            return None
    
    @staticmethod
    def open_image_dialog() -> Optional[str]:
        """Open file dialog to select image"""
        return filedialog.askopenfilename(
            title="Select an Image",
            filetypes=config.IMAGE_FILE_TYPES
        )
    
    @staticmethod
    def save_image_dialog() -> Optional[str]:
        """Open save dialog for image"""
        return filedialog.asksaveasfilename(
            defaultextension=".jpg",
            filetypes=config.SAVE_FILE_TYPES
        )
    
    @staticmethod
    def apply_enhancements(image: Image.Image, contrast: float, brightness: float, blur: float) -> Image.Image:
        """Apply contrast, brightness and blur enhancements to image"""
        try:
            temp_image = image.copy()
            temp_image = ImageEnhance.Contrast(temp_image).enhance(contrast)
            temp_image = ImageEnhance.Brightness(temp_image).enhance(brightness)
            if blur > 0:
                temp_image = temp_image.filter(ImageFilter.GaussianBlur(blur))
            return temp_image
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Error applying enhancements: {str(e)}")
            return image
    
    @staticmethod
    def create_display_image(image: Image.Image) -> ImageTk.PhotoImage:
        """Create a PhotoImage for display"""
        try:
            display_temp = image.copy()
            display_temp.thumbnail(config.MAX_IMAGE_SIZE)
            return ImageTk.PhotoImage(display_temp)
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Error creating display image: {str(e)}")
            return None
    
    @staticmethod
    def save_image(image: Image.Image, file_path: str) -> bool:
        """Save image to file"""
        try:
            image.save(file_path)
            tkinter.messagebox.showinfo("Success", "Image saved successfully!")
            return True
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Error saving image: {str(e)}")
            return False
    
    @staticmethod
    def resize_image(image: Image.Image, width: int, height: int) -> Optional[Image.Image]:
        """Resize image to specified dimensions"""
        try:
            if width > 0 and height > 0:
                return image.resize((width, height))
            else:
                tkinter.messagebox.showerror("Error", "Width and height must be positive numbers.")
                return None
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Error resizing image: {str(e)}")
            return None
    
    @staticmethod
    def convert_to_grayscale(image: Image.Image) -> Optional[Image.Image]:
        """Convert image to grayscale"""
        try:
            # Convert to grayscale - need to convert back to RGB mode for further editing
            return ImageOps.grayscale(image).convert('RGB')
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Error converting to grayscale: {str(e)}")
            return None
