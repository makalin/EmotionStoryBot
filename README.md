# EmotionStoryBot
A creative robotic application that tells dynamic, emotion-adaptive stories based on your facial expressions! Using a webcam for real-time emotion detection and an optional robotic component (e.g., arm or LEDs), this project brings storytelling to life in a unique, interactive way.

## Features
- **Emotion Detection:** Analyzes your facial expressions (happy, sad, surprised, etc.) using a webcam.
- **Dynamic Storytelling:** Adjusts the story’s tone, events, or pacing based on your emotions.
- **Robotic Interaction:** Optionally controls a small robotic arm or LEDs to "act out" story moments.
- **Voice Narration:** Narrates the story aloud with text-to-speech.
- **Customizable:** Add your own story templates in simple JSON or text format.

## How It Works
1. Start the program, and your webcam activates to detect your emotions.
2. The bot begins narrating a story (e.g., *"Once, there was a brave explorer..."*).
3. Your expressions shape the tale:
   - Frowning? The story adds a comforting twist.
   - Smiling? It ramps up the excitement!
4. A robotic arm waves or LEDs blink to enhance key moments (optional).
5. The story concludes based on your final mood.

## Prerequisites
- **Python 3.8+**
- A webcam (for emotion detection)
- Optional: Arduino or Raspberry Pi with servo motors/LEDs for robotic features

## Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/sosyalrobot/EmotionStoryBot.git
   cd EmotionStoryBot
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   Required libraries: `opencv-python`, `deepface`, `pyttsx3`, `pyserial` (optional for hardware).

3. **Hardware Setup (Optional):**
   - Connect an Arduino or Raspberry Pi with a servo motor or LEDs.
   - Upload the provided `robot_control.ino` sketch to your Arduino (if using).

4. **Run the Program:**
   ```bash
   python main.py
   ```

## Usage
- Launch the script and look into your webcam.
- Listen as the story unfolds, adapting to your reactions.
- Customize stories by editing files in the `stories/` folder (see [Story Templates](#story-templates)).

## Project Structure
```
EmotionStoryBot/
├── main.py              # Main script to run the application
├── emotion_detector.py  # Module for facial emotion detection
├── story_engine.py      # Logic to adapt and generate stories
├── robot_control.py     # Controls robotic hardware (optional)
├── stories/             # Folder for sample story templates
│   ├── happy_story.json
│   └── adventure_story.json
├── requirements.txt     # Dependencies
└── README.md            # You’re reading it!
```

## Story Templates
Stories are stored in the `stories/` folder as JSON files. Example format:
```json
{
  "title": "The Brave Explorer",
  "base_story": "Once, there was a brave explorer named Alex.",
  "happy": "Alex found a treasure chest full of gold!",
  "sad": "Alex met a lost puppy and decided to help it home.",
  "surprised": "Suddenly, a dragon flew overhead!"
}
```
Edit or add your own to personalize the experience!

## Example Output
```
Starting EmotionStoryBot...
Webcam active. Say hello!
[Emotion Detected: Happy] "Alex found a treasure chest full of gold!"
[Robotic Arm Waves] "Hooray!"
```

## Contributing
Feel free to fork this repo, submit issues, or send pull requests. Ideas for new features (e.g., multilingual support, GUI) are welcome!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- Built with ❤️ by [sosyalrobot](https://github.com/sosyalrobot).
- Powered by OpenCV, DeepFace, and pyttsx3.

## Roadmap
- Add multilingual story support (e.g., Turkish).
- Create a simple GUI for story creation.
- Export story sessions as replay videos.
