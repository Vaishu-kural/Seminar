import cv2
import os
from datetime import datetime
import time

# === Menu ===
print("Select Face Detection Mode:")
print("1 - Normal Detection (boxes)")
print("2 - Blur Faces (privacy mode)")
print("3 - Save Cropped Faces (dataset builder)")
print("4 - Auto-Save Full Snapshots (attendance style)")
choice = input("Enter choice (1/2/3/4): ").strip()
# === Setup ===
cam = cv2.VideoCapture(0)
if not cam.isOpened():
    raise RuntimeError("Could not open webcam.")
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
if face_cascade.empty():
    raise RuntimeError("Failed to load Haar cascade model.")
# Output folders
if choice == "3":
    os.makedirs("cropped_faces", exist_ok=True)
    count = 0
if choice == "4":
    os.makedirs("snapshots", exist_ok=True)
    last_save_time = 0
    saved_count = 0

    COOLDOWN_SEC = 2.0   # seconds between auto-saves
# === Main Loop ===
while True:
    ret, frame = cam.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        if choice == "1":
            # Normal detection (green box)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        elif choice == "2":
            # Blur faces
            roi = frame[y:y+h, x:x+w]
            roi = cv2.GaussianBlur(roi, (51, 51), 30)
            frame[y:y+h, x:x+w] = roi
        elif choice == "3":
            # Save cropped faces
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            face_crop = frame[y:y+h, x:x+w]
            filename = f"cropped_faces/face_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{count}.jpg"
            cv2.imwrite(filename, face_crop)
            count += 1
    # Attendance-style auto snapshot (mode 4)
    if choice == "4":
        if len(faces) > 0:
            now = time.time()
            if now - last_save_time >= COOLDOWN_SEC:
                filename = f"snapshots/snap_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
                cv2.imwrite(filename, frame)
                saved_count += 1
                last_save_time = now
        hud = f"Faces: {len(faces)} | Saved: {saved_count} | Press 'q' to quit"
        cv2.putText(frame, hud, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 200, 255), 2)
    # Show window
    cv2.imshow("Face Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cam.release()
cv2.destroyAllWindows()
