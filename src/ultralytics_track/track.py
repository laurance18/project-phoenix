from ultralytics import YOLO
import os
import argparse

def main():
  parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument(
      '--source', 
      help='Path of the video or camera id.', 
      required=False, 
      default=os.path.join(os.path.dirname(__file__), "testing", "red_v1.mp4")
    )
  parser.add_argument(
      '--model', 
      help='Path of the object detection model.', 
      required=False, 
      default=os.path.join(os.path.dirname(__file__), "models", "anka_v1.0.pt")
    )
  parser.add_argument(
      '--conf', 
      help='Path of the object detection model.', 
      required=False, 
      default=0.30
    )
  args = parser.parse_args()

  source_path = os.path.join(os.path.dirname(__file__), "testing", args.source)
  model_path = os.path.join(os.path.dirname(__file__), "models", args.model)
  conf_threshold = float(args.conf)
  
  run(source_path, model_path, conf_threshold)
    
def run(source_path, model_path, conf_threshold):
  # Show and save results to project folder
  model = YOLO(model_path)
  for r in model.track(source=source_path, tracker="bytetrack.yaml", show=True, stream=True, persist=True, save=True, conf=conf_threshold, project=os.path.join(os.path.dirname(__file__), "demo")):
      pass
  # DEPRECATED: results = model.track(source=source_path, show=True, persist=True, save=True, project=os.path.join(os.path.dirname(__file__), "val"))

  # TODO: Put points on the center of the bounding boxes
  # TODO: Apply HSV color detection to the balloons

if __name__ == "__main__":
  main()