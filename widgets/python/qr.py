# pip install opencv-python opencv-python-headless pyzbar
import cv2
from pyzbar.pyzbar import decode

def main():
    # Open the default camera
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open video capture device.")
        return

    try:
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()

            if not ret:
                print("Error: Could not read frame.")
                break

            # Decode QR codes in the frame
            decoded_objects = decode(frame)

            for obj in decoded_objects:
                # Draw a rectangle around the detected QR code
                points = obj.polygon
                if len(points) > 4:
                    hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                    points = hull

                n = len(points)
                for j in range(0, n):
                    cv2.line(frame, tuple(points[j]), tuple(points[(j + 1) % n]), (0, 255, 0), 3)

                # Put the decoded text above the rectangle
                x = obj.rect.left
                y = obj.rect.top
                cv2.putText(frame, obj.data.decode("utf-8"), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Display the resulting frame
            cv2.imshow('QR Code Scanner', frame)

            # Press 'q' to exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        # When everything is done, release the capture
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
