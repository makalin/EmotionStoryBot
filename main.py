import time
from emotion_detector import detect_emotion
from story_engine import StoryEngine
from robot_control import RobotController
import pyttsx3

def main():
    # Initialize components
    print("Starting EmotionStoryBot...")
    print("Webcam active. Say hello!")
    
    engine = pyttsx3.init()  # Text-to-speech engine
    story = StoryEngine("stories/happy_story.json")  # Load a story template
    robot = RobotController()  # Optional robotic control (set port if using hardware)

    try:
        while True:
            # Detect emotion from webcam
            emotion = detect_emotion()
            if emotion:
                print(f"[Emotion Detected: {emotion}]")
                
                # Get story segment based on emotion
                story_text = story.get_story_segment(emotion)
                print(f"Story: {story_text}")
                
                # Narrate the story
                engine.say(story_text)
                engine.runAndWait()
                
                # Trigger robotic action (optional)
                robot.perform_action(emotion)
                
            time.sleep(2)  # Pause between iterations
    except KeyboardInterrupt:
        print("\nStopping EmotionStoryBot...")
        robot.close()

if __name__ == "__main__":
    main()