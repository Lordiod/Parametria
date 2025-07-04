"""
Configuration settings for the Image Editor application
"""

# Application settings
APP_TITLE = "Image Editor"
DEFAULT_WINDOW_SIZE = (1200, 800)

# Image settings
MAX_IMAGE_SIZE = (1460, 860)
DEFAULT_SLIDER_VALUES = {
    'contrast': 1.0,
    'brightness': 1.0,
    'blur': 0.0
}

# Slider ranges
SLIDER_RANGES = {
    'contrast': {'from': 0.1, 'to': 2.0, 'steps': 19},
    'brightness': {'from': 0.1, 'to': 2.0, 'steps': 19},
    'blur': {'from': 0.0, 'to': 5.0, 'steps': 50}
}

# File dialog settings
IMAGE_FILE_TYPES = [
    ("Image files", "*.jpg *.jpeg *.png *.gif *.bmp *.tiff"),
    ("All files", "*.*")
]

SAVE_FILE_TYPES = [
    ("JPEG files", "*.jpg"),
    ("PNG files", "*.png"),
    ("BMP files", "*.bmp"),
    ("All files", "*.*")
]

# UI Layout settings
FRAME_SETTINGS = {
    'picframe': {'width': 1500, 'height': 860, 'corner_radius': 10},
    'toolsframe': {'width': 350, 'height': 860, 'corner_radius': 10}
}

# UI positioning (relative positions)
BUTTON_POSITIONS = {
    'open': (0.935, 0.09),
    'grayscale': (0.935, 0.45),
    'resize': (0.935, 0.50),
    'save': (0.980, 0.55),
    'undo': (0.890, 0.55),
    'reset': (0.935, 0.60)
}

SLIDER_POSITIONS = {
    'contrast_label': (0.923, 0.15),
    'contrast_slider': (0.951, 0.20),
    'brightness_label': (0.927, 0.25),
    'brightness_slider': (0.951, 0.30),
    'blur_label': (0.918, 0.35),
    'blur_slider': (0.951, 0.40)
}

# Theme settings
THEME = {
    'appearance_mode': "dark",
    'color_theme': "blue"
}
