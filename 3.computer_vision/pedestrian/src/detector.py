from ultralytics import YOLO
from pydantic import BaseModel
from enum import Enum
from src.config import get_settings

SETTINGS = get_settings()

class PredictionType(str, Enum):
    classification = "CLS"
    object_detection = "OD"
    segmentation = "SEG"

class GeneralPrediction(BaseModel):
    pred_type: PredictionType

class Detection(GeneralPrediction):
    n_detections: int
    boxes: list[list[int]]
    label: str
    confidences: list[float]

class PedestrianDetector:
    def __init__(self) -> None:
        self.model = YOLO(SETTINGS.yolo_version)

    def predict_image(self, image_array, threshold):
        results = self.model(image_array, conf=threshold)[0]
        labels = results.boxes.cls.tolist()
        # pedestrian_indexes = [i for i in range(len(label_list)) if label_list[i] == "person"]
        # labels = [results.names[i] for i in results.boxes.cls.tolist()]
        indexes = [i for i in range(len(labels)) if labels[i] == 0]     # 0 = "person"
        boxes = [[int(v) for v in box] for i, box in enumerate(results.boxes.xyxy.tolist()) if i in indexes]
        confidences = [c for i, c in enumerate(results.boxes.conf.tolist()) if i in indexes]
        detection = Detection(
            pred_type=PredictionType.object_detection,
            n_detections=len(boxes),
            boxes=boxes,
            label="person",
            confidences=confidences
        )
        return detection