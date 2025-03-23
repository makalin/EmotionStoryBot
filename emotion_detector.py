from deepface import DeepFace
import cv2

def detect_emotion():
    try:
        # Capture frame from webcam
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not access webcam.")
            return None
        
        # Analyze emotion
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        dominant_emotion = result[0]['dominant_emotion']
        
        # Release the capture
        cap.release()
        cv2.destroyAllWindows()
        
        return dominant_emotion  # e.g., "happy", "sad", "surprised"
    except Exception as e:
        print(f"Emotion detection failed: {e}")
        return None

# Test the module standalone
if __name__ == "__main__":
    emotion = detect_emotion()
    print(f"Detected emotion: {emotion}")