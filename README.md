# Real-Time Object Detection with YOLOv8 and Integration with ROS2

## Description

This project integrates **YOLOv8 object detection** with **ROS2** (`rclpy`) communication.  
It consists of:
- `object_detection.py`: **Publisher** node — captures webcam feed, performs object detection, and publishes detected object data.
- `detection_subscriber.py`: **Subscriber** node — listens to the published messages and displays the received object information.

---

## Features
- Real-time object detection using **YOLOv8**.
- **ROS2 Publisher** (`object_detection.py`) sending detection information.
- **ROS2 Subscriber** (`detection_subscriber.py`) receiving and logging detected objects.
- Live webcam video with bounding boxes and labels.

---

## Requirements

Install these Python packages:

```bash
pip install cvzone==1.6.1
pip install opencv-python==4.10.0.84
pip install rclpy==3.3.14
pip install std_msgs==4.2.4
pip install ultralytics==8.3.61
```

Additional Requirements:
- **ROS2** installed and sourced (e.g., Humble, Iron).
- YOLO model weights `yolov8n.pt` stored at `../Yolo-Weights/yolov8n.pt`.

---

## Project Structure

```
├── detection_subscriber.py     # Subscriber Node
├── object_detection.py         # Publisher Node
├── README.md
├── Yolo-Weights/
│   └── yolov8n.pt
```

---

## How to Run

1. **Source your ROS2 environment:**
   ```bash
   source /opt/ros/humble/setup.bash
   ```

2. **Open two terminals:**

### Terminal 1 — Run the Publisher (`object_detection.py`)

```bash
python object_detection.py
```

This will:
- Open the webcam.
- Detect objects.
- Publish object details to the `/chatter` topic.

---

### Terminal 2 — Run the Subscriber (`detection_subscriber.py`)

```bash
python detection_subscriber.py
```

This will:
- Subscribe to `/chatter`.
- Display detected object data in the terminal.

---

## Example Output

**Terminal (Subscriber):**
```
Received:
person (100,120)-(300,450)
dog (400,500)-(650,700)
```

**Publisher (Webcam feed window):**
- Bounding boxes with object labels displayed live.

---

## Notes
- Ensure that the YOLO model path (`../Yolo-Weights/yolov8n.pt`) is correct.
- Ensure no other application is using your webcam.
- If needed, adjust camera resolution settings inside `object_detection.py`.

---

## Future Improvements
- Use custom ROS2 message types instead of `std_msgs/String`.
- Add support for multiple object detection streams.
- Incorporate object tracking (e.g., DeepSORT) for better multi-frame consistency.

---
