from model import detect, model
from control import move_to
import cv2
import os
import sys

# Paths:
os.makedirs('../data/input', exist_ok=True)
os.makedirs('../data/output', exist_ok=True)
input_path = 'data/input/predict_test.jpg'
output_path = 'data/output/predict_test.jpg'


def main():
    # Open USB webcam
    cap = cv2.VideoCapture(0)

    # Set resolution
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    # Warm up the camera
    for _ in range(10):
        ret, frame = cap.read()

    # Final capture
    ret, frame = cap.read()
    cap.release()

    if not ret:
        raise RuntimeError("Could not read the frame from the camera")

    # Save input picture
    cv2.imwrite(input_path, frame)

    # Predict image
    label = detect(frame)
    print("\n?? Predicted:", label)

    # Move servo according to label
    move_to(label)

    # Save predicted picture
    annotated = model(frame[..., ::-1]).render()[0]
    cv2.imwrite(output_path, annotated)


if __name__ == "__main__":
    main()
