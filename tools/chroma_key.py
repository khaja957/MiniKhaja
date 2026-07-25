from pathlib import Path
import cv2
import numpy as np

INPUT = Path("assets/input/idle.mp4")
OUTPUT = Path("assets/output/idle")

OUTPUT.mkdir(parents=True, exist_ok=True)

cap = cv2.VideoCapture(str(INPUT))

frame = 0

while True:

    ok, img = cap.read()

    if not ok:
        break

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Tuned for bright chroma green
    lower = np.array([35, 60, 40])
    upper = np.array([90, 255, 255])

    mask = cv2.inRange(hsv, lower, upper)

    # Clean mask
    kernel = np.ones((3, 3), np.uint8)

    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    alpha = cv2.bitwise_not(mask)
    alpha = cv2.GaussianBlur(alpha, (5, 5), 0)

    rgba = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)

    rgba[:, :, 3] = alpha

    # Reduce green spill on visible pixels
    visible = alpha > 10

    b = rgba[:, :, 0]
    g = rgba[:, :, 1]
    r = rgba[:, :, 2]

    g[visible] = np.minimum(g[visible], ((r[visible] + b[visible]) / 2).astype(np.uint8))

    rgba[:, :, 1] = g

    cv2.imwrite(str(OUTPUT / f"{frame:04}.png"), rgba)

    frame += 1

cap.release()

print(f"Exported {frame} frames.")