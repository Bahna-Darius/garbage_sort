# Import Libraries:
import cv2
import os


# Open Camera:
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
ret, frame = cap.read()
cap.release()
frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

# Save Picture:
filename = 'frame_test.jpg'
folder = '../data/input'

os.makedirs(folder, exist_ok=True)
path = os.path.join(folder, filename)
ok = cv2.imwrite(path, frame)

if ok:
        print(f"✅ Imagine salvată în {path}")
else:
    print("❌ Eroare la salvarea imaginii")
