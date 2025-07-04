#!/usr/bin/env python3
"""
Image Editor Application

A modern image editing application built with CustomTkinter and PIL.
Provides basic image editing features including contrast, brightness, blur adjustments,
grayscale conversion, resizing, and undo/redo functionality.
"""

from utils.screen_utils import ScreenUtils
from gui.main_window import MainWindow
from gui.image_editor_gui import ImageEditorGUI

def main():
    """Main entry point for the image editor application"""
    # Get optimal window size
    window_size = ScreenUtils.get_optimal_window_size()
    
    # Create main window
    main_window = MainWindow(window_size)
    
    # Create image editor GUI
    image_editor = ImageEditorGUI(
        main_window.get_root(),
        main_window.get_picframe(),
        main_window.get_toolsframe()
    )
    
    # Start the application
    main_window.run()

if __name__ == "__main__":
    main()
