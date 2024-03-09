# Task 6

# Part 2:
# Pick an open-source software on GitHub
# Write a script that showcases the basic usage of the software

import cv2
import pytesseract

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error opening video stream or file")

frame_count = 0

cv2.namedWindow("Text Extraction", cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    frame_count += 1

    if frame_count % 100 == 0:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        data = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)
        for i in range(len(data["text"])):
            if int(data["conf"][i]) > 60:
                (x, y, w, h) = (
                    data["left"][i],
                    data["top"][i],
                    data["width"][i],
                    data["height"][i],
                )
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                text = data["text"][i]
                if text and text.strip():
                    print(text)
                    cv2.putText(
                        frame,
                        text,
                        (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.9,
                        (0, 255, 0),
                        2,
                    )
        cv2.imshow("Text Extraction", frame)

    if cv2.getWindowProperty("Text Extraction", cv2.WND_PROP_VISIBLE) < 1:
        break

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
