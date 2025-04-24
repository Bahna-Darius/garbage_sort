import sys
import cv2
import torch


sys.path.insert(__index=0, __object='../yolov5')

model = torch.hub.load(
    repo_or_dir='../yolov5',
    model='custom',
    path='../weights/best.pt',
    source='local',
    force_reload=False
)


def detect(frame_bgr):
    """
    Receives a BGR frame (OpenCV), returns the label (string).
    """
    frame_rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)      # BGR -> RGB
    predict_model = model(frame_rgb)
    df = predict_model.pandas().xyxy[0]

    if df.empty:
        return 'unknown'
    else:
        top = df.iloc[df['confidence'].idxmax()]

    return top['name']

