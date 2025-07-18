import cv2
import numpy as np

def get_color_name(h, s, v):
    if s < 30 and v > 200:
        return "White"
    elif s < 50 and v < 50:
        return "Black"
    elif h < 10 or h > 160:
        return "Red"
    elif 10 < h <= 25:
        return "Orange"
    elif 25 < h <= 34:
        return "Yellow"
    elif 35 < h <= 85:
        return "Green"
    elif 85 < h <= 100:
        return "Cyan"
    elif 100 < h <= 125:
        return "Blue"
    elif 125 < h <= 160:
        return "Purple"
    else:
        return "Unknown"

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h_frame, w_frame, _ = frame.shape
    cx, cy = w_frame // 2, h_frame // 2

    bgr_pixel = frame[cy, cx]
    hsv_pixel = cv2.cvtColor(np.uint8([[bgr_pixel]]), cv2.COLOR_BGR2HSV)
    h, s, v = hsv_pixel[0][0]

    color_name = get_color_name(h, s, v)

    cv2.circle(frame, (cx, cy), 5, (255, 255, 255), -1)
    cv2.rectangle(frame, (5, 5), (280, 50), (255, 255, 255), -1)
    cv2.putText(frame, f"Color: {color_name}", (10, 35), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 0), 2)

    cv2.imshow("Color Recognition", frame)

    key = cv2.waitKey(1) & 0xFF
    if chr(key).lower() == 'q':
        break

cap.release()
cv2.destroyAllWindows()
