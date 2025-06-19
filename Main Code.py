#Basic Imports necessary for the code to execute
import cv2
from ultralytics import YOLO
from tkinter import Tk, filedialog
import os
from moviepy.editor import VideoFileClip

# Popup Window for file selection
Tk().withdraw()
input_path = filedialog.askopenfilename(
    title="Select input video file",
    filetypes=[("MP4 files", "*.mp4"), ("All files", "*.*")]
)

if not input_path:
    print("No file selected. Exiting.")
    exit()

# Load Yolo model
model = YOLO("yolov8n.pt")

# Setup video
cap = cv2.VideoCapture(input_path)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Output
output_path = "output_" + os.path.basename(input_path)
out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)[0]

    for box in results.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = box.conf[0].item()
        cls = int(box.cls[0])
        label = f"{model.names[cls]} {conf:.2f}"
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (255, 255, 255), 1)

    out.write(frame)

cap.release()
out.release()

# Will add audio from the original video to the processed video
try:
    original_clip = VideoFileClip(input_path)
    processed_clip = VideoFileClip(output_path)

    final = processed_clip.set_audio(original_clip.audio)
    final_output_path = output_path.replace(".mp4", "_with_audio.mp4")
    final.write_videofile(final_output_path, codec="libx264", audio_codec="aac")

    print(f"Audio added! Final video saved at: {final_output_path}")
except Exception as e:
    print(f"⚠️ Failed to add audio: {e}")

print(f"Done! Saved as: {output_path}")
