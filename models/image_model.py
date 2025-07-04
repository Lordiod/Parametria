from PIL import Image, ImageTk
from typing import List, Tuple, Optional

class ImageModel:
    """Model class to manage image state and data"""
    
    def __init__(self):
        self.original_image: Optional[Image.Image] = None
        self.display_image: Optional[ImageTk.PhotoImage] = None
        self.enhanced_image: Optional[Image.Image] = None
        self.undo_stack: List[Tuple[Image.Image, float, float, float]] = []
    
    def set_original_image(self, image: Image.Image):
        """Set the original image and initialize state"""
        self.original_image = image
        self.enhanced_image = image.copy()
        self.undo_stack = [(image.copy(), 1.0, 1.0, 0.0)]
    
    def set_enhanced_image(self, image: Image.Image):
        """Set the enhanced image"""
        self.enhanced_image = image
    
    def set_display_image(self, image: ImageTk.PhotoImage):
        """Set the display image"""
        self.display_image = image
    
    def add_to_undo_stack(self, image: Image.Image, contrast: float, brightness: float, blur: float):
        """Add state to undo stack"""
        self.undo_stack.append((image.copy(), contrast, brightness, blur))
    
    def undo_last_change(self) -> Optional[Tuple[Image.Image, float, float, float]]:
        """Undo last change and return previous state"""
        if len(self.undo_stack) > 1:
            self.undo_stack.pop()
            return self.undo_stack[-1]
        return None
    
    def reset_to_original(self):
        """Reset to original state"""
        if self.original_image:
            self.enhanced_image = self.original_image.copy()
            self.undo_stack = [(self.enhanced_image.copy(), 1.0, 1.0, 0.0)]
    
    def has_image(self) -> bool:
        """Check if there's an image loaded"""
        return self.original_image is not None
    
    def has_enhanced_image(self) -> bool:
        """Check if there's an enhanced image"""
        return self.enhanced_image is not None
