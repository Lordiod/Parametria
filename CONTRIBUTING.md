# Contributing to Image Editor

Thank you for your interest in contributing to the Image Editor project! We welcome contributions from everyone.

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- Git
- Basic knowledge of Python and GUI development

### Development Setup

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
```bash
git clone https://github.com/yourusername/Image-processing-project.git
cd Image-processing-project
```

3. **Install dependencies**:
```bash
python setup.py
# or manually: pip install -r requirements.txt
```

4. **Create a branch** for your feature:
```bash
git checkout -b feature/your-feature-name
```

## 📋 How to Contribute

### 🐛 Reporting Bugs

Before creating bug reports, please check the issue list as you might find that the bug has already been reported. When creating a bug report, include:

- **Clear title** and description
- **Steps to reproduce** the behavior
- **Expected behavior**
- **Screenshots** if applicable
- **Environment details** (OS, Python version, etc.)

### 💡 Suggesting Features

Feature suggestions are welcome! Please:

- **Check existing issues** first
- **Describe the feature** clearly
- **Explain why it would be useful**
- **Consider implementation complexity**

### 🔧 Code Contributions

#### Code Style Guidelines

- Follow **PEP 8** Python style conventions
- Use **type hints** for function parameters and return values
- Write **docstrings** for all classes and methods
- Keep line length under **88 characters**
- Use **meaningful variable names**

#### Example Code Style
```python
def process_image(image: Image.Image, brightness: float) -> Image.Image:
    """
    Apply brightness adjustment to an image.
    
    Args:
        image: The PIL Image to process
        brightness: Brightness factor (1.0 = no change)
        
    Returns:
        Processed PIL Image
        
    Raises:
        ValueError: If brightness is negative
    """
    if brightness < 0:
        raise ValueError("Brightness must be non-negative")
    
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(brightness)
```

#### Project Structure

When adding new features, follow the modular architecture:

- **`models/`**: Data and state management
- **`services/`**: Business logic and processing
- **`gui/`**: User interface components
- **`utils/`**: Utility functions
- **`config.py`**: Configuration settings

#### Adding New Image Filters

1. **Add processing logic** to `services/image_processor.py`:
```python
@staticmethod
def apply_vintage_filter(image: Image.Image) -> Image.Image:
    """Apply vintage effect to image"""
    # Implementation here
    pass
```

2. **Update GUI** in `gui/image_editor_gui.py`:
```python
def vintage_image(self):
    """Apply vintage filter to current image"""
    if self.image_model.has_enhanced_image():
        filtered_img = self.image_processor.apply_vintage_filter(
            self.image_model.enhanced_image
        )
        if filtered_img:
            # Save state and update display
            pass
```

3. **Add button/control** in the GUI widget creation method
4. **Update configuration** in `config.py` if needed

### 🧪 Testing

Before submitting your changes:

1. **Test the application** manually:
```bash
python main.py
```

2. **Test your specific feature** thoroughly
3. **Check for regressions** in existing functionality
4. **Verify error handling** works correctly

### 📝 Commit Guidelines

Write clear, descriptive commit messages:

```bash
# Good examples
git commit -m "Add sepia filter functionality"
git commit -m "Fix brightness slider not updating display"
git commit -m "Improve error handling in image loading"

# Avoid
git commit -m "Fix bug"
git commit -m "Update stuff"
git commit -m "WIP"
```

### 📤 Submitting Changes

1. **Push your branch** to your fork:
```bash
git push origin feature/your-feature-name
```

2. **Create a Pull Request** on GitHub:
   - Use a clear, descriptive title
   - Describe what your changes do
   - Reference any related issues
   - Include screenshots for UI changes

3. **Respond to feedback** and make requested changes

## 🎯 Priority Areas

We're particularly interested in contributions in these areas:

### High Priority
- **New image filters** (sepia, vintage, etc.)
- **Performance optimizations**
- **Better error handling**
- **Unit tests**

### Medium Priority
- **Keyboard shortcuts**
- **Batch processing**
- **Plugin system**
- **Additional file formats**

### Low Priority
- **UI themes**
- **Advanced undo/redo**
- **Image metadata editing**

## 🆘 Getting Help

If you need help:

- **Check the documentation** in the README
- **Browse existing issues** for similar problems
- **Ask questions** in GitHub Discussions
- **Review the code** - it's well-documented!

## 📜 Code of Conduct

### Be Respectful
- Use welcoming and inclusive language
- Respect differing viewpoints and experiences
- Accept constructive criticism gracefully
- Focus on what's best for the community

### Be Collaborative
- Help others learn and grow
- Share knowledge and resources
- Encourage new contributors
- Be patient with beginners

## 🏆 Recognition

Contributors will be:
- **Listed** in the project contributors
- **Mentioned** in release notes for significant contributions
- **Invited** to join the project team for ongoing contributors

## 📞 Contact

- **GitHub Issues**: For bugs and feature requests
- **GitHub Discussions**: For questions and general discussion
- **Pull Requests**: For code contributions

Thank you for contributing to make Image Editor better! 🎉
