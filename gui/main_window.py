import customtkinter as ctk
from typing import Tuple
import config

class MainWindow:
    """Main window setup and configuration"""
    
    def __init__(self, window_size: Tuple[str, str]):
        self.root = ctk.CTk()
        self.window_size = window_size
        self._setup_window()
        self._create_frames()
    
    def _setup_window(self):
        """Setup main window properties"""
        ctk.set_appearance_mode(config.THEME['appearance_mode'])
        ctk.set_default_color_theme(config.THEME['color_theme'])
        self.root.title(config.APP_TITLE)
        window_size_str = f"{self.window_size[0]}x{self.window_size[1]}"
        self.root.geometry(window_size_str)
        self.root.resizable(True, True)
    
    def _create_frames(self):
        """Create main frames for the application"""
        frame_config = config.FRAME_SETTINGS
        
        self.picframe = ctk.CTkFrame(
            master=self.root, 
            width=frame_config['picframe']['width'], 
            height=frame_config['picframe']['height'], 
            corner_radius=frame_config['picframe']['corner_radius']
        )
        self.picframe.place(relx=0.01, rely=0.02)
        
        self.toolsframe = ctk.CTkFrame(
            master=self.root, 
            width=frame_config['toolsframe']['width'], 
            height=frame_config['toolsframe']['height'], 
            corner_radius=frame_config['toolsframe']['corner_radius']
        )
        self.toolsframe.place(relx=0.99, rely=0.02, anchor="ne")
    
    def get_root(self) -> ctk.CTk:
        """Get the root window"""
        return self.root
    
    def get_picframe(self) -> ctk.CTkFrame:
        """Get the picture frame"""
        return self.picframe
    
    def get_toolsframe(self) -> ctk.CTkFrame:
        """Get the tools frame"""
        return self.toolsframe
    
    def run(self):
        """Start the main event loop"""
        self.root.mainloop()
