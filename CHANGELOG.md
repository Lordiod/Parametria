# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2025-07-04

### 🎉 Major Refactoring Release

#### Added
- **Modular Architecture**: Complete restructuring into models, services, utils, and GUI modules
- **Configuration Management**: Centralized settings in `config.py`
- **Type Hints**: Full type annotation support throughout codebase
- **Error Handling**: Comprehensive exception handling with user-friendly messages
- **Documentation**: Extensive docstrings and project documentation
- **Setup Script**: Automated installation script (`setup.py`)
- **GitHub Ready**: License, gitignore, and proper project structure

#### Changed
- **Code Organization**: Separated concerns into logical modules
  - `models/`: Data and state management
  - `services/`: Business logic and image processing
  - `gui/`: User interface components
  - `utils/`: Utility functions
- **Improved Maintainability**: Clean, readable code structure
- **Enhanced Extensibility**: Easy to add new features and filters
- **Better Testing**: Modular design enables unit testing

#### Technical Improvements
- **Separation of Concerns**: Clear boundaries between UI, business logic, and data
- **Single Responsibility**: Each class and module has one clear purpose
- **Dependency Injection**: Loose coupling between components
- **Configuration-Driven**: UI layout and settings externalized

#### Preserved Features
- ✅ All original functionality maintained
- ✅ Image loading and saving (JPG, PNG, GIF, BMP, TIFF)
- ✅ Real-time adjustments (contrast, brightness, blur)
- ✅ Grayscale conversion
- ✅ Image resizing with custom dimensions
- ✅ Undo/redo functionality with full history
- ✅ Reset to original image
- ✅ Modern dark theme UI
- ✅ Auto-scaling based on screen resolution

## [1.0.0] - 2025-07-03

### Initial Release
- Basic image editing functionality in single file (`finalimage.py`)
- Image loading and saving
- Contrast, brightness, and blur adjustments
- Grayscale conversion
- Resize functionality
- Undo/redo support
- CustomTkinter dark theme UI
