# 🤟 Sign Language Gesture Detection with YOLOv8

This project uses a custom-trained YOLOv8 model to detect and classify hand gestures representing sign language in real time through your webcam.

## 📸 Demo
![demo](docs/demo.gif) <!-- Optional if you add a GIF -->

## 🧠 Project Highlights

- Trained on 3 custom hand gestures like:
  - `loveyou`
  - `yes`
  - `stop`
  

- Real-time gesture detection using OpenCV
- Built with Ultralytics' YOLOv8
- Custom dataset collected and annotated using Roboflow

---

## 📁 Folder Structure

```
sign-language-detection/
├── roboflow/
│   ├── train/
│   ├── valid/
│   └── data.yaml                # Trained YOLOv8 model weights
├── capture.py      # Capture and save labeled hand gesture images
├── train_mode.py         # YOLOv8 model training script
├── detection.py           # Real-time webcam detection
├── requirements.txt
├── LICENCSE
├── README.md
└── .gitignore
```

---

## 🚀 Getting Started

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt

```
Create and Setup Environment
Select Python interpretor as Environment(Press F1)
Activate Environment
```bash
pip install -r requirements.txt

if you want to use GPU then install this pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118



### 2️⃣ Prepare Dataset

You can:
- Collect your own using `capture.py`
- and label using robflow or Download pre Labelled dataset and push it in robflow folder

Make sure your folder structure looks like this:
```
roboflow/
├── train/
├── valid/
└── data.yaml
```

### 3️⃣ Train the Model

```bash
python train_mode.py
```

### 4️⃣ Run Real-Time Detection

```bash
python detection.py
```

---

## 🧠 Training Config (YOLOv8)

- `imgsz`: 1280
- `epochs`: 100
- `batch`: 8
- `model`: yolov8n.pt or yolov8s.pt

---

## 🤝 Contributing

Pull requests and forks are welcome! Add more gestures or improve accuracy.

---

## 📜 License

This project is open source under the MIT License.
