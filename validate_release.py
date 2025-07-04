#!/usr/bin/env python3
"""
Quick validation script to ensure the Image Editor is ready for GitHub publishing.
Run this before pushing to GitHub to verify everything works correctly.
"""

import sys
import os
from pathlib import Path

def check_file_structure():
    """Verify all required files are present"""
    print("📁 Checking file structure...")
    
    required_files = [
        "main.py",
        "config.py", 
        "requirements.txt",
        "README.md",
        "LICENSE",
        "CONTRIBUTING.md",
        "CHANGELOG.md",
        "SECURITY.md",
        ".gitignore",
        "setup.py"
    ]
    
    required_dirs = [
        "models",
        "services", 
        "gui",
        "utils",
        ".github"
    ]
    
    missing_files = []
    missing_dirs = []
    
    for file in required_files:
        if not Path(file).exists():
            missing_files.append(file)
    
    for dir in required_dirs:
        if not Path(dir).is_dir():
            missing_dirs.append(dir)
    
    if missing_files:
        print(f"❌ Missing files: {', '.join(missing_files)}")
        return False
    
    if missing_dirs:
        print(f"❌ Missing directories: {', '.join(missing_dirs)}")
        return False
    
    print("✅ All required files and directories present")
    return True

def check_imports():
    """Test that all modules can be imported"""
    print("\n📦 Testing imports...")
    
    try:
        import config
        print("✅ config.py imported successfully")
        
        from models.image_model import ImageModel
        print("✅ ImageModel imported successfully")
        
        from services.image_processor import ImageProcessor  
        print("✅ ImageProcessor imported successfully")
        
        from utils.screen_utils import ScreenUtils
        print("✅ ScreenUtils imported successfully")
        
        from gui.main_window import MainWindow
        print("✅ MainWindow imported successfully")
        
        from gui.image_editor_gui import ImageEditorGUI
        print("✅ ImageEditorGUI imported successfully")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def check_configuration():
    """Verify configuration is valid"""
    print("\n⚙️ Checking configuration...")
    
    try:
        import config
        
        # Check required config attributes
        required_attrs = [
            'APP_TITLE',
            'DEFAULT_WINDOW_SIZE', 
            'MAX_IMAGE_SIZE',
            'DEFAULT_SLIDER_VALUES',
            'SLIDER_RANGES',
            'IMAGE_FILE_TYPES',
            'SAVE_FILE_TYPES'
        ]
        
        for attr in required_attrs:
            if not hasattr(config, attr):
                print(f"❌ Missing config attribute: {attr}")
                return False
        
        print("✅ Configuration is valid")
        return True
        
    except Exception as e:
        print(f"❌ Configuration error: {e}")
        return False

def check_dependencies():
    """Check if all dependencies are installable"""
    print("\n📋 Checking dependencies...")
    
    try:
        with open('requirements.txt', 'r') as f:
            deps = f.read().strip().split('\n')
        
        print(f"✅ Found {len(deps)} dependencies:")
        for dep in deps:
            print(f"   • {dep}")
        
        return True
        
    except FileNotFoundError:
        print("❌ requirements.txt not found")
        return False
    except Exception as e:
        print(f"❌ Error reading dependencies: {e}")
        return False

def check_github_files():
    """Verify GitHub-specific files are present"""
    print("\n🐙 Checking GitHub files...")
    
    github_files = [
        ".github/ISSUE_TEMPLATE/bug_report.yml",
        ".github/ISSUE_TEMPLATE/feature_request.yml", 
        ".github/ISSUE_TEMPLATE/question.yml",
        ".github/workflows/ci.yml"
    ]
    
    missing = []
    for file in github_files:
        if not Path(file).exists():
            missing.append(file)
    
    if missing:
        print(f"❌ Missing GitHub files: {', '.join(missing)}")
        return False
    
    print("✅ All GitHub files present")
    return True

def main():
    """Run all validation checks"""
    print("🚀 Image Editor - GitHub Publishing Validation")
    print("=" * 50)
    
    checks = [
        ("File Structure", check_file_structure),
        ("Module Imports", check_imports), 
        ("Configuration", check_configuration),
        ("Dependencies", check_dependencies),
        ("GitHub Files", check_github_files)
    ]
    
    all_passed = True
    
    for check_name, check_func in checks:
        result = check_func()
        if not result:
            all_passed = False
    
    print("\n" + "=" * 50)
    
    if all_passed:
        print("🎉 All checks passed! The project is ready for GitHub publishing.")
        print("\n📝 Next steps:")
        print("1. Create a new repository on GitHub")
        print("2. Add remote: git remote add origin <repository-url>")
        print("3. Add all files: git add .")
        print("4. Commit: git commit -m 'Initial release - Modular Image Editor v2.0.0'")
        print("5. Push: git push -u origin main")
        print("\n🎯 Repository should include:")
        print("• Clear README with screenshots")
        print("• Proper licensing (MIT)")
        print("• Contributing guidelines")
        print("• Issue templates")
        print("• CI/CD pipeline")
        print("• Security policy")
        
        return True
    else:
        print("❌ Some checks failed. Please fix the issues above before publishing.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
