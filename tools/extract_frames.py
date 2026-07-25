from pathlib import Path
import cv2

VIDEO = Path("assets/input/idle.mp4")
OUTPUT = Path("assets/idle")

OUTPUT.mkdir(parents=True, exist_ok=True)

cap = cv2.VideoCapture(str(VIDEO))

frame = 0

while True:

    ok, img = cap.read()

    if not ok:
        break

    cv2.imwrite(
        str(OUTPUT / f"{frame:04}.png"),
        img
    )

    frame += 1

cap.release()

print(frame)