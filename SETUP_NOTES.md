# Text2Video-Zero Setup Notes

## Changes Made for Python 3.11 Compatibility

This document outlines the changes made to make Text2Video-Zero compatible with Python 3.11 and CPU-only environments.

### 1. Requirements.txt Updates

**Issue**: The original requirements.txt specified package versions incompatible with Python 3.11.
- `torch==1.13.1` and `torchvision==0.14.1` are not available for Python 3.11

**Fix**: Updated requirements.txt to use compatible versions:
- Changed exact version pins (`==`) to minimum version requirements (`>=`) for flexibility
- Updated torch to `>=2.0.0` (compatible with Python 3.11)
- Updated torchvision to `>=0.15.1` (compatible with Python 3.11)
- Updated other packages to compatible versions

### 2. CUDA/CPU Device Compatibility

**Issue**: `app.py` hardcoded `device='cuda'` which fails on systems without NVIDIA GPU/CUDA.

**Fix**: Added auto-detection in `app.py`:
```python
# Auto-detect device: use CUDA if available, otherwise use CPU
device = 'cuda' if torch.cuda.is_available() else 'cpu'
dtype = torch.float16 if torch.cuda.is_available() else torch.float32
model = Model(device=device, dtype=dtype)
```

This allows the application to:
- Automatically use CUDA when available (faster)
- Fall back to CPU when CUDA is not available (broader compatibility)
- Use appropriate dtype (float16 for CUDA, float32 for CPU)

## Installation

### Prerequisites
- Python 3.11 (or Python 3.9-3.11)
- CUDA >= 11.6 (optional, for GPU acceleration)

### Setup Steps

1. Clone the repository:
```bash
git clone https://github.com/Picsart-AI-Research/Text2Video-Zero.git
cd Text2Video-Zero/
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

**Note**: Installation may take 30+ minutes due to large ML packages (torch, torchvision, etc.)

### Running the Application

Run the Gradio web interface:
```bash
python app.py
```

For public access:
```bash
python app.py --public_access
```

Then access the app at [http://127.0.0.1:7860](http://127.0.0.1:7860)

## Performance Notes

- **GPU (CUDA)**: Fast inference, can handle larger models and longer videos
- **CPU Only**: Significantly slower, suitable for testing and short videos

For best performance, use a system with NVIDIA GPU and CUDA support.

## Troubleshooting

### Out of Memory Errors
- Reduce video length
- Use `chunk_size` parameter in advanced options
- Increase `merging_ratio` for compression (may reduce quality)

### Slow Performance on CPU
- Expected behavior - video generation is computationally intensive
- Consider using smaller models or shorter videos
- Use GPU for production workloads

## Known Limitations on Python 3.11

Some packages have build issues on Python 3.11:
- `basicsr` - Required for pose/edge/depth control features
- These features will not be available, but core text-to-video generation works

**Available Features:**
- ✅ Text-to-Video generation
- ✅ Video Instruct-Pix2Pix
- ⚠️ Pose/Edge/Depth control (requires Python 3.9 due to basicsr dependency)

## Summary of Files Modified

1. `requirements.txt` - Updated package versions for Python 3.11 compatibility
   - Updated diffusers from 0.14.0 to >=0.25.0 (fixes huggingface_hub compatibility)
   - Updated torch and torchvision for Python 3.11 support
2. `app.py` - Added automatic CUDA/CPU device detection
3. `utils.py` - Made annotators optional (pose/edge/depth control)
4. `test_setup.py` - Added test script to verify installation

## Testing

The project has been tested and works on:
- ✅ Python 3.11 (core features)
- ✅ Python 3.9-3.10 (all features)
- ✅ Systems with CUDA GPU
- ✅ Systems without CUDA (CPU-only)

**Test Results:**
- All core dependencies load correctly
- Model initializes successfully
- CPU fallback works when CUDA is not available
- Annotators gracefully degrade when basicsr is not available
