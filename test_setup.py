#!/usr/bin/env python
"""
Simple test script to verify Text2Video-Zero setup.
This checks that all core dependencies are importable and the basic setup is correct.
"""

import sys

def test_imports():
    """Test that all core dependencies can be imported."""
    print("Testing core dependencies...")
    errors = []

    # Test core ML libraries
    try:
        import torch
        print(f"✓ PyTorch {torch.__version__} imported successfully")
        print(f"  CUDA available: {torch.cuda.is_available()}")
        if torch.cuda.is_available():
            print(f"  CUDA version: {torch.version.cuda}")
            print(f"  GPU: {torch.cuda.get_device_name(0)}")
        else:
            print("  Running on CPU")
    except ImportError as e:
        errors.append(f"✗ PyTorch import failed: {e}")

    try:
        import torchvision
        print(f"✓ Torchvision {torchvision.__version__} imported successfully")
    except ImportError as e:
        errors.append(f"✗ Torchvision import failed: {e}")

    try:
        import diffusers
        print(f"✓ Diffusers {diffusers.__version__} imported successfully")
    except ImportError as e:
        errors.append(f"✗ Diffusers import failed: {e}")

    try:
        import transformers
        print(f"✓ Transformers {transformers.__version__} imported successfully")
    except ImportError as e:
        errors.append(f"✗ Transformers import failed: {e}")

    try:
        import gradio
        print(f"✓ Gradio {gradio.__version__} imported successfully")
    except ImportError as e:
        errors.append(f"✗ Gradio import failed: {e}")

    try:
        import numpy
        print(f"✓ NumPy {numpy.__version__} imported successfully")
    except ImportError as e:
        errors.append(f"✗ NumPy import failed: {e}")

    return errors

def test_model_init():
    """Test that the Model class can be initialized."""
    print("\nTesting Model initialization...")
    try:
        import torch
        from model import Model

        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        dtype = torch.float16 if torch.cuda.is_available() else torch.float32

        print(f"  Initializing model on {device} with {dtype}...")
        model = Model(device=device, dtype=dtype)
        print("✓ Model initialized successfully")
        return []
    except Exception as e:
        return [f"✗ Model initialization failed: {e}"]

def main():
    """Run all tests."""
    print("=" * 60)
    print("Text2Video-Zero Setup Test")
    print("=" * 60)
    print()

    # Test imports
    import_errors = test_imports()

    # Test model initialization (only if imports succeeded)
    model_errors = []
    if not import_errors:
        model_errors = test_model_init()
    else:
        print("\nSkipping model test due to import errors")

    # Print summary
    print()
    print("=" * 60)
    all_errors = import_errors + model_errors
    if all_errors:
        print("FAILED - Errors found:")
        for error in all_errors:
            print(f"  {error}")
        print()
        print("Please install missing dependencies:")
        print("  pip install -r requirements.txt")
        sys.exit(1)
    else:
        print("SUCCESS - All tests passed!")
        print()
        print("You can now run the application:")
        print("  python app.py")
        sys.exit(0)

if __name__ == "__main__":
    main()
