# 🎨 Image Editor

<div align="center">

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)
![Status](https://img.shields.io/badge/status-stable-brightgreen.svg)

A modern, modular image editing application built with Python, CustomTkinter, and PIL. Features a clean dark theme interface with real-time image editing capabilities.

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [Architecture](#architecture) • [Contributing](#contributing)

</div>

## ✨ Features

### 🖼️ **Image Operations**
- **Multi-format Support**: JPG, PNG, GIF, BMP, TIFF
- **Real-time Editing**: Live preview of all adjustments
- **Batch Operations**: Apply multiple effects simultaneously

### 🎛️ **Editing Tools**
- **🔆 Brightness**: Adjust image luminosity (0.1x - 2.0x)
- **🌈 Contrast**: Enhance or reduce image contrast (0.1x - 2.0x)  
- **🌀 Blur**: Apply Gaussian blur effect (0 - 5.0 radius)
- **⚫ Grayscale**: Convert to black and white
- **📏 Resize**: Custom width and height dimensions

### 💾 **File Management**
- **Open**: Load images with file browser
- **Save**: Export in multiple formats
- **Auto-scaling**: Automatically fits large images to display

### 🔄 **History & Controls**
- **Undo/Redo**: Full operation history
- **Reset**: Return to original image
- **Real-time Preview**: See changes instantly

### 🎨 **User Interface**
- **Modern Design**: Clean dark theme
- **Responsive Layout**: Auto-adapts to screen size
- **Intuitive Controls**: Slider-based adjustments
- **Cross-platform**: Works on Windows, macOS, Linux

## Project Structure

```
Image-processing-project/
├── main.py                     # Application entry point
├── requirements.txt            # Python dependencies
├── models/
│   ├── __init__.py
│   └── image_model.py         # Image data model and state management
├── services/
│   ├── __init__.py
│   └── image_processor.py     # Image processing operations
├── utils/
│   ├── __init__.py
│   └── screen_utils.py        # Screen and window utilities
├── gui/
│   ├── __init__.py
│   ├── main_window.py         # Main window setup
│   └── image_editor_gui.py    # Image editor GUI components
└── finalimage.py              # Original monolithic version (legacy)
```

## 🚀 Installation

### Prerequisites
- **Python 3.7+** (Check with `python --version`)
- **pip** package manager

### Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/Image-processing-project.git
cd Image-processing-project
```

2. **Run setup script** (Recommended)
```bash
python setup.py
```

3. **Manual installation** (Alternative)
```bash
pip install -r requirements.txt
```

4. **Launch the application**
```bash
python main.py
```

### Dependencies
- `customtkinter>=5.0.0` - Modern UI framework
- `Pillow>=9.0.0` - Image processing library  
- `screeninfo>=0.8.1` - Screen resolution detection

## 🎯 Usage

### Basic Workflow
1. **Open Image**: Click "Open Image" to load a file
2. **Edit**: Use sliders to adjust brightness, contrast, blur
3. **Transform**: Apply grayscale or resize operations
4. **Save**: Export your edited image

### Keyboard Shortcuts
- `Ctrl+O`: Open image
- `Ctrl+S`: Save image  
- `Ctrl+Z`: Undo last action
- `Ctrl+R`: Reset to original

### Tips
- **Real-time Preview**: All changes show instantly
- **Undo Anytime**: Full history of all operations
- **Multiple Formats**: Save as JPG, PNG, BMP
- **Auto-scaling**: Large images automatically fit display

## 🏗️ Architecture

The application follows a **modular architecture** with clear separation of concerns:

```
📁 Image-processing-project/
├── 🚀 main.py                    # Application entry point
├── ⚙️ config.py                  # Configuration settings
├── 📋 requirements.txt           # Python dependencies
├── 📁 models/                    # Data layer
│   └── 🗃️ image_model.py        # Image state management
├── 📁 services/                  # Business logic
│   └── 🔧 image_processor.py    # Image processing operations
├── 📁 utils/                     # Utilities
│   └── 🖥️ screen_utils.py       # Screen/window utilities
└── 📁 gui/                       # User interface
    ├── 🏠 main_window.py         # Main window setup
    └── 🎨 image_editor_gui.py    # GUI components & handlers
```

### Design Principles
- **🎯 Single Responsibility**: Each module has one clear purpose
- **🔄 Separation of Concerns**: UI, business logic, and data are separated
- **🧩 Modularity**: Easy to test, maintain, and extend
- **⚙️ Configuration-Driven**: Settings externalized for easy customization

### Key Components

#### **Models** (`models/`)
- `ImageModel`: Manages image state, undo history, and data operations

#### **Services** (`services/`)  
- `ImageProcessor`: Handles all image processing logic and file operations

#### **GUI** (`gui/`)
- `MainWindow`: Window setup and layout management
- `ImageEditorGUI`: UI components and event handling

#### **Utils** (`utils/`)
- `ScreenUtils`: Screen resolution and window sizing utilities

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Getting Started
1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Setup
```bash
# Clone your fork
git clone https://github.com/yourusername/Image-processing-project.git
cd Image-processing-project

# Install development dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

### Code Style
- Follow **PEP 8** Python style guide
- Add **type hints** for function parameters and returns
- Include **docstrings** for all classes and methods
- Write **meaningful commit messages**

### Adding New Features

#### Adding a New Image Filter
1. Add the processing logic to `services/image_processor.py`
2. Update the GUI in `gui/image_editor_gui.py`
3. Add configuration options to `config.py`

#### Example: Adding Sepia Filter
```python
# In services/image_processor.py
@staticmethod
def apply_sepia(image: Image.Image) -> Image.Image:
    """Apply sepia tone effect"""
    # Implementation here
    pass

# In gui/image_editor_gui.py  
def sepia_image(self):
    """Apply sepia effect to current image"""
    # GUI handling here
    pass
```

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **[CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)** - Modern UI framework
- **[Pillow](https://python-pillow.org/)** - Python Imaging Library
- **[Screeninfo](https://github.com/rr-/screeninfo)** - Multi-monitor support

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/Image-processing-project/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/Image-processing-project/discussions)
- **Wiki**: [Project Wiki](https://github.com/yourusername/Image-processing-project/wiki)

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

Made with ❤️ by the Image Editor team

</div>
