import customtkinter as ctk
import tkinter.messagebox
from models.image_model import ImageModel
from services.image_processor import ImageProcessor
import config

class ImageEditorGUI:
    """GUI components and handlers for the image editor"""
    
    def __init__(self, root: ctk.CTk, picframe: ctk.CTkFrame, toolsframe: ctk.CTkFrame):
        self.root = root
        self.picframe = picframe
        self.toolsframe = toolsframe
        self.image_model = ImageModel()
        self.image_processor = ImageProcessor()
        
        self._create_widgets()
    
    def _create_widgets(self):
        """Create all GUI widgets"""
        # Image display label
        self.img_label_edited = ctk.CTkLabel(self.picframe, text="‎")
        self.img_label_edited.place(relx=0.5, rely=0.5, anchor="center")
        
        # Buttons
        positions = config.BUTTON_POSITIONS
        self.open_button = ctk.CTkButton(self.root, text="Open Image", command=self.open_image)
        self.open_button.place(relx=positions['open'][0], rely=positions['open'][1], anchor="ne")
        
        self.grayscale_button = ctk.CTkButton(self.root, text="Grayscale", command=self.grayscale_image)
        self.grayscale_button.place(relx=positions['grayscale'][0], rely=positions['grayscale'][1], anchor="ne")
        
        self.resize_button = ctk.CTkButton(self.root, text="Resize Image", command=self.resize_image)
        self.resize_button.place(relx=positions['resize'][0], rely=positions['resize'][1], anchor="ne")
        
        self.save_button = ctk.CTkButton(self.root, text="Save Image", command=self.save_image)
        self.save_button.place(relx=positions['save'][0], rely=positions['save'][1], anchor="ne")
        
        self.undo_button = ctk.CTkButton(self.root, text="Undo", command=self.undo_changes)
        self.undo_button.place(relx=positions['undo'][0], rely=positions['undo'][1], anchor="ne")
        
        self.reset_button = ctk.CTkButton(self.root, text="Reset Image", command=self.reset_image)
        self.reset_button.place(relx=positions['reset'][0], rely=positions['reset'][1], anchor="ne")
        
        # Sliders and labels
        slider_pos = config.SLIDER_POSITIONS
        slider_ranges = config.SLIDER_RANGES
        defaults = config.DEFAULT_SLIDER_VALUES
        
        self.contrast_label = ctk.CTkLabel(self.root, text="Adjust Contrast:")
        self.contrast_label.place(relx=slider_pos['contrast_label'][0], rely=slider_pos['contrast_label'][1], anchor="ne")
        
        self.contrast_slider = ctk.CTkSlider(
            self.root, 
            from_=slider_ranges['contrast']['from'], 
            to=slider_ranges['contrast']['to'], 
            number_of_steps=slider_ranges['contrast']['steps'], 
            orientation="horizontal"
        )
        self.contrast_slider.set(defaults['contrast'])
        self.contrast_slider.bind("<ButtonRelease-1>", self.slider_released)
        self.contrast_slider.place(relx=slider_pos['contrast_slider'][0], rely=slider_pos['contrast_slider'][1], anchor="ne")
        
        self.brightness_label = ctk.CTkLabel(self.root, text="Adjust Brightness:")
        self.brightness_label.place(relx=slider_pos['brightness_label'][0], rely=slider_pos['brightness_label'][1], anchor="ne")
        
        self.brightness_slider = ctk.CTkSlider(
            self.root, 
            from_=slider_ranges['brightness']['from'], 
            to=slider_ranges['brightness']['to'], 
            number_of_steps=slider_ranges['brightness']['steps'], 
            orientation="horizontal"
        )
        self.brightness_slider.set(defaults['brightness'])
        self.brightness_slider.bind("<ButtonRelease-1>", self.slider_released)
        self.brightness_slider.place(relx=slider_pos['brightness_slider'][0], rely=slider_pos['brightness_slider'][1], anchor="ne")
        
        self.blur_label = ctk.CTkLabel(self.root, text="Adjust Blur:")
        self.blur_label.place(relx=slider_pos['blur_label'][0], rely=slider_pos['blur_label'][1], anchor="ne")
        
        self.blur_slider = ctk.CTkSlider(
            self.root, 
            from_=slider_ranges['blur']['from'], 
            to=slider_ranges['blur']['to'], 
            number_of_steps=slider_ranges['blur']['steps'], 
            orientation="horizontal"
        )
        self.blur_slider.set(defaults['blur'])
        self.blur_slider.bind("<ButtonRelease-1>", self.slider_released)
        self.blur_slider.place(relx=slider_pos['blur_slider'][0], rely=slider_pos['blur_slider'][1], anchor="ne")
    
    def _reset_sliders_to_defaults(self):
        """Reset all sliders to their default values"""
        defaults = config.DEFAULT_SLIDER_VALUES
        self.contrast_slider.set(defaults['contrast'])
        self.brightness_slider.set(defaults['brightness'])
        self.blur_slider.set(defaults['blur'])
    
    def _get_current_slider_values(self):
        """Get current values from all sliders"""
        return (
            self.contrast_slider.get(),
            self.brightness_slider.get(),
            self.blur_slider.get()
        )
    
    def open_image(self):
        file_path = self.image_processor.open_image_dialog()
        if file_path:
            image = self.image_processor.load_image(file_path)
            if image:
                self.image_model.set_original_image(image)
                self._reset_sliders_to_defaults()
                self.update_image()

    def update_image(self):
        if self.image_model.has_image():
            try:
                contrast_value, brightness_value, blur_value = self._get_current_slider_values()
                
                # Always start from the original image to avoid cumulative effects
                temp_image = self.image_model.enhanced_image.copy()
                temp_image = self.image_processor.apply_enhancements(temp_image, contrast_value, brightness_value, blur_value)
                
                # Create a copy for display
                display_image = self.image_processor.create_display_image(temp_image)
                if display_image:
                    self.image_model.set_display_image(display_image)
                    self.img_label_edited.configure(image=display_image)
                    self.img_label_edited.image = display_image
            except Exception as e:
                tkinter.messagebox.showerror("Error", f"Error updating image: {str(e)}")
 
    def slider_released(self, event):
        try:
            # Apply the current slider values to create the new enhanced image
            contrast_value, brightness_value, blur_value = self._get_current_slider_values()
            
            # Start from original and apply all effects
            temp_image = self.image_processor.apply_enhancements(
                self.image_model.original_image, 
                contrast_value, 
                brightness_value, 
                blur_value
            )
            
            self.image_model.set_enhanced_image(temp_image)
            self.update_image()
            self.image_model.add_to_undo_stack(temp_image, contrast_value, brightness_value, blur_value)
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Error applying changes: {str(e)}")

    def adjust_contrast(self, value=None):
        if self.image_model.has_image():
            self.update_image()

    def adjust_brightness(self, value=None):
        if self.image_model.has_image():
            self.update_image()

    def adjust_blur(self, value=None):
        if self.image_model.has_image():
            self.update_image()

    def undo_changes(self):
        try:
            previous_state = self.image_model.undo_last_change()
            if previous_state:
                enhanced_image, contrast_value, brightness_value, blur_value = previous_state
                self.image_model.set_enhanced_image(enhanced_image)
                
                # Update sliders to match the previous state
                self.contrast_slider.set(contrast_value)
                self.brightness_slider.set(brightness_value)
                self.blur_slider.set(blur_value)
                
                # Update the display
                self.update_image()
            elif self.image_model.has_image():
                # Reset to original image
                self.image_model.reset_to_original()
                self._reset_sliders_to_defaults()
                self.update_image()
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Error undoing changes: {str(e)}")

    def save_image(self):
        if self.image_model.has_enhanced_image():
            file_path = self.image_processor.save_image_dialog()
            if file_path:
                # Apply current slider settings to get the final image
                contrast_value, brightness_value, blur_value = self._get_current_slider_values()
                
                # Create final image with all effects
                final_image = self.image_processor.apply_enhancements(
                    self.image_model.enhanced_image,
                    contrast_value,
                    brightness_value,
                    blur_value
                )
                
                self.image_processor.save_image(final_image, file_path)
        else:
            tkinter.messagebox.showwarning("Warning", "No image to save. Please open an image first.")

    def resize_image(self):
        if not self.image_model.has_enhanced_image():
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

            resized_image = self.image_processor.resize_image(self.image_model.enhanced_image, new_width, new_height)
            if resized_image:
                # Save current state to undo stack
                contrast_value, brightness_value, blur_value = self._get_current_slider_values()
                self.image_model.add_to_undo_stack(
                    self.image_model.enhanced_image, 
                    contrast_value, 
                    brightness_value, 
                    blur_value
                )
                
                self.image_model.set_enhanced_image(resized_image)
                self.update_image()

        except ValueError:
            tkinter.messagebox.showerror("Error", "Please enter valid numeric values for width and height.")
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Error resizing image: {str(e)}")

    def grayscale_image(self):
        if self.image_model.has_enhanced_image():
            grayscale_img = self.image_processor.convert_to_grayscale(self.image_model.enhanced_image)
            if grayscale_img:
                # Save current state to undo stack
                contrast_value, brightness_value, blur_value = self._get_current_slider_values()
                self.image_model.add_to_undo_stack(
                    self.image_model.enhanced_image, 
                    contrast_value, 
                    brightness_value, 
                    blur_value
                )
                
                self.image_model.set_enhanced_image(grayscale_img)
                self.update_image()
        else:
            tkinter.messagebox.showwarning("Warning", "No image to convert. Please open an image first.")

    def reset_image(self):
        if self.image_model.has_image():
            try:
                self.image_model.reset_to_original()
                self._reset_sliders_to_defaults()
                self.update_image()
            except Exception as e:
                tkinter.messagebox.showerror("Error", f"Error resetting image: {str(e)}")
        else:
            tkinter.messagebox.showwarning("Warning", "No image to reset. Please open an image first.")
