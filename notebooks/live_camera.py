import torch
import cv2

# Încarcă modelul YOLOv5 antrenat
model = torch.hub.load(
    r'../yolov5',
    'custom',
    path='../weights/best.pt',
    source='local',
    force_reload=False
)

# Deschide camera laptopului
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("❌ Nu pot deschide camera.")
    exit()

print("✅ Camera funcționează. Apasă 'q' pentru a opri.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Nu pot citi frame-ul.")
        break

    # Trimite frame-ul la model pentru predicții
    results = model(frame)

    # Obține imaginea cu bounding box-uri desenate
    img = results.render()[0]  # imaginea este modificată în place

    # Afișează rezultatul într-o fereastră
    cv2.imshow("YOLOv5 - Detectare Gunoi", img)

    # Dacă se apasă 'q', ieșim din buclă
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Eliberăm resursele
cap.release()
cv2.destroyAllWindows()
