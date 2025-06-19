# 🎯 VisionSynth
**Real-Time Moving Object Tracker in Video with Audio Retention using YOLOv8 + OpenCV + MoviePy**

```
This is a Fun Side Project that inputs videos and add detection boxes around moving objects. It is often percieved as a cool filter for videos by GenZ.
```

---

## 📽️ Overview

TrackVision-YOLOv8 is a Python-based video processing tool that:
- Detects and tracks objects using **YOLOv8**
- Automatically draws bounding boxes + confidence scores
- **Preserves original audio** using `moviepy`
- Exports final video into a fixed output directory

---

## ✨ Features

✅ Select any `.mp4` file via file dialog  
✅ Frame-by-frame detection using YOLOv8 (`yolov8n.pt`)  
✅ Draws real-time bounding boxes with class labels  
✅ Original audio retained post-processing  
✅ Output saved to:  
`C:\Users\User\Desktop\Live Detection System\Output_Vid`

---

## 📁 Folder Structure

```plaintext
📂 Live Detection System/
├─ 📂 Output_Vid/          ← Final videos saved here
├─ 📄 Main_Code.py         ← Your main script
├─ 📄 requirements.txt     ← Dependencies
├─ 📄 README.md            ← This file

```

---

## ⚙️ Requirements
Install dependencies with:

~~~
pip install -r requirements.txt
~~~

---

## 🧰 Required Packages

```plaintext
-opencv-python
-ultralytics
-moviepy
-tk

```

Note: You must also have ffmpeg installed and available in your system's PATH for audio processing.

---

## 🚀 How to Run

1. Run the Program
2. A file picker will open → choose an .mp4 video
3. Script runs object detection and draws boxes
4. Output video with audio will be saved to:

~~~
C:\Users\Om\Desktop\Live Detection System\Output_Vid\output_<filename>_with_audio.mp4
~~~

---

## 🥸Things to keep in mind
- Create a Folder for the Output video named as **Output_Vid**
- The video should be of supported format.
  
---

## 🔒 License
This project is licensed under the MIT License – use freely, just credit the original author.

---

## 📦 YOLOv8 Model

This project uses Ultralytics YOLOv8 Nano (yolov8n.pt) for faster detection with good accuracy.

```plaintext
You can replace it with larger models (yolov8s.pt, yolov8m.pt, etc.) for improved accuracy (but slower performance).
```

---

## 🧠 Credits

```plaintext
-Ultralytics – YOLOv8
-OpenCV – Computer vision tools
-MoviePy – Audio-video editing
-Python – Core programming language
```

