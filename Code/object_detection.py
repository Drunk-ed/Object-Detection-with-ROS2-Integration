from ultralytics import YOLO
import cv2
import cvzone
import math
import time
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


cap = cv2.VideoCapture(0)  # For Webcam
cap.set(3, 1280)
cap.set(4, 720)

model = YOLO("../Yolo-Weights/yolov8n.pt")

classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]


class MyPublisher(Node):
    def __init__(self):
        super().__init__('my_publisher')
        self.publisher_ = self.create_publisher(String, 'chatter', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        success, img = cap.read()
        if not success:
            return

        results = model(img, stream=True)
        msg_out = ""

        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                w, h = x2 - x1, y2 - y1
                cvzone.cornerRect(img, (x1, y1, w, h))
                conf = math.ceil((box.conf[0] * 100)) / 100
                cls = int(box.cls[0])
                label = classNames[cls]
                cvzone.putTextRect(img, f'{label} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1)
                msg_out += f'{label} ({x1},{y1})-({x2},{y2})\n'

        if msg_out:
            msg = String()
            msg.data = msg_out.strip()
            self.publisher_.publish(msg)
            self.get_logger().info(f'Publishing:\n{msg.data}')

        cv2.imshow("output", img)
        cv2.waitKey(1)


def main(args=None):
    rclpy.init(args=args)
    node = MyPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
