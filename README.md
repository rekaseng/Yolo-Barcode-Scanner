

# Yolo-Barcode-Scanner

Barcode detection with Deep Learning (YOLO) and decoding barcode using Pyzbar in Python



## Requirements

python version 3.8.10

torch==2.3.1

torchvision==0.18.1 

Refer: https://github.com/pytorch/pytorch/issues/130659


## Installation

Make sure to fulfill above requirements before proceed with this step.

```bash
git clone https://github.com/rekaseng/Yolo-Barcode-Scanner.git
cd Yolo-Barcode-Scanner
pip install -r requirements.txt
```

Note: If you faced warning issues with different torch version, uninstall the current torch versions and run the following commands:

```bash
pip uninstall torch torchvision torchaudio -y
pip install torch==2.3.1 torchvision==0.18.1 torchaudio==2.3.1 --index-url https://download.pytorch.org/whl/cpu
```

⚠ Make sure to use --index-url for specific GPU versions / CPU-only version.

If using a GPU (CUDA), visit the PyTorch installation page to get the correct version.


## Installation of YoloV5
Since this project relies on YOLOv5, install it separately:

```bash
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -r requirements.txt
```



## Requirements

python version 3.8.10

torch==2.3.1

torchvision==0.18.1 

Refer: https://github.com/pytorch/pytorch/issues/130659


## Installation

Make sure to fulfill above requirements before proceed with this step.

```bash
  https://github.com/rekaseng/Yolo-Barcode-Scanner.git
  cd Yolo-Barcode-Scanner
  pip install -r requirements.txt
```

Note: If you faced warning issues with different torch version, uninstall the current torch versions and run the following commands:

```bash
  pip uninstall torch torchvision torchaudio -y
  pip install torch==2.3.1 torchvision==0.18.1 torchaudio==2.3.1 --index-url https://download.pytorch.org/whl/cpu
```

⚠ Make sure to use --index-url for specific GPU versions / CPU-only version.

If using a GPU (CUDA), visit the PyTorch installation page to get the correct version.


## Installation of YoloV5
Since this project relies on YOLOv5, install it separately:

```bash
  git clone https://github.com/ultralytics/yolov5.git
  cd yolov5
  pip install -r requirements.txt
```