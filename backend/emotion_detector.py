import cv2
from deepface import DeepFace

def detect_emotion():
    cap = cv2.VideoCapture(0)

    emotion = "Detecting..."

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        try:
            # Analyze emotion on current frame
            result = DeepFace.analyze(
                frame,
                actions=["emotion"],
                enforce_detection=False
            )

            emotion = result[0]["dominant_emotion"]

        except Exception as e:
            emotion = "No face"

        # 🔴 DRAW EMOTION ON WEBCAM (THIS IS THE KEY PART)
        cv2.putText(
            frame,
            f"Emotion: {emotion}",
            (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.imshow("Emotion Detection - Press Q to stop", frame)

        # Press Q to stop
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

    return emotion
