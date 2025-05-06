# Measure-Mather

**Predicting calorie and carbon waste from Harvard dining hall plates using computer vision.**

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Hardware Setup](#hardware-setup)
- [Quick Start](#quick-start)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)

## Overview
Measure-Mather is a research collaboration between the Harvard John A. Paulson School of Engineering and Applied Sciences and Mather House that quantifies edible calories and their associated greenhouse-gas emissions discarded in the undergraduate dining halls. By combining **Ultralytics YOLOv8-Seg** and an automated image-capture pipeline, the project turns anonymous tray images into actionable sustainability metrics for Harvard University Dining Services (HUDS). The long-term vision is to inform menu design, procurement, and behavioral nudges that reduce food waste on campus.

## Features
- **Ultralytics YOLOv8-Seg** model for instance segmentation of tray items.  
- **Edge collection rig**: Raspberry Pi 5 + 12 MP camera + HC-SR04 ultrasonic sensor for hands-free capture at the dish belt.  
- **Secure upload** to Google Drive via the Drive API (OAuth 2.0); HUDS nutritional data ingested from **CSV files** for downstream analysis.  
- **Carbon accounting**: converts predicted portions into calories and CO₂-equivalent using values from Our World in Data.  

## Hardware Setup

| Component | Price (USD) | Buy-link |
| --- | --- | --- |
| Ultrasonic Distance Sensor – 5 V (HC-SR04) | 5.25 | [link](https://gladstonehifi.com/products/piicodev-cable-100mm?pr_prod_strat=e5_desc&pr_rec_id=716b0622d&pr_rec_pid=7509617279153&pr_ref_pid=7509617246385&pr_seq=uniform) |
| Raspberry Pi 5 / 8 GB | 80.00 | [link](https://www.pishop.us/product/raspberry-pi-5-8gb/?src=raspberrypi) |
| Raspberry Pi 5 Case with Fan | 10.95 | [link](https://www.pishop.us/product/raspberry-pi-5-8gb/?src=raspberrypi) |
| Raspberry Pi Active Cooler | 6.60 | [link](https://www.pishop.us/product/raspberry-pi-5-8gb/?src=raspberrypi) |
| Official 32 GB microSD (Raspberry Pi OS 64-bit) | 12.95 | [link](https://www.pishop.us/product/raspberry-pi-5-8gb/?src=raspberrypi) |
| Micro-HDMI → HDMI (1 m) | 6.95 | [link](https://www.pishop.us/product/raspberry-pi-5-8gb/?src=raspberrypi) |
| Raspberry Pi 5 27 W USB-C Power Supply | 13.20 | [link](https://www.pishop.us/product/raspberry-pi-5-8gb/?src=raspberrypi) |
| Raspberry Pi Camera Module 3 Wide | 38.50 | [link](https://www.pishop.us/product/raspberry-pi-camera-module-3-wide/) |
| Camera Cable for Raspberry Pi 5 (500 mm) | 3.95 | [link](https://www.pishop.us/product/camera-cable-for-raspberry-pi-5/) |

**Total cost:** \$178.35 (excluding taxes and shipping)

## Quick Start
```bash
git clone https://github.com/Patarakorn/Measure-Mather.git
cd Measure-Mather
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Training
```bash
yolo segment train data=measuremather.yaml model=yolov8n-seg.pt epochs=100 imgsz=640
```

## Inference
```bash
yolo segment predict model=runs/segment/exp/weights/best.pt source=data/samples
```

## Contributing
Pull requests are welcome! Please open an issue first to discuss major changes.

1. Fork the repo  
2. Create your feature branch (`git checkout -b feat/amazing-feature`)  
3. Commit your changes (`git commit -m 'Add amazing feature'`)  
4. Push to the branch (`git push origin feat/amazing-feature`)  
5. Open a Pull Request  

## Acknowledgements
- Prof. **Lakshminarayanan Mahadevan** for advising  
- Harvard University Dining Services for operational support  
- Ultralytics for YOLOv8  
- Our World in Data for emission factors  
- Everyone at Mather House who let me lurk by the dish belt 🔍

