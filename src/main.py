from src.model import detect, model
from src.control import move_to
import cv2
import os


# Paths:
os.makedirs('../data/input', exist_ok=True)
os.makedirs('../data/output', exist_ok=True)
input_path = 'data/input/predict_test.jpg'
output_path = 'data/output/predict_test.jpg'


def main():
    capture_picture = cv2.VideoCapture(0)

    for _ in range(10):
        ret, frame = capture_picture.read()
    capture_picture.release()
    if not ret:
        raise RuntimeError("Could not read the frame from the Pi camera")

    cv2.imwrite(input_path, frame)
    # Predict image:
    label = detect(frame)
    print("\n🔖 Predicted:", label)

    # Move servo according to label:
    move_to(label)

    # Save predicted picture:
    annotated = model(frame[..., ::-1]).render()[0]
    cv2.imwrite(output_path, annotated)

if __name__ == "__main__":
    main()
