import json
import random

class StoryEngine:
    def __init__(self, story_file):
        # Load story template from JSON
        with open(story_file, 'r') as f:
            self.story_data = json.load(f)
        self.current_story = self.story_data["base_story"]
    
    def get_story_segment(self, emotion):
        # Append a segment based on the detected emotion
        if emotion in self.story_data:
            segment = self.story_data[emotion]
        else:
            segment = random.choice(list(self.story_data.values())[2:])  # Fallback to random segment
        
        self.current_story += " " + segment
        return self.current_story

# Test the module standalone
if __name__ == "__main__":
    story = StoryEngine("stories/happy_story.json")
    print(story.get_story_segment("happy"))
    print(story.get_story_segment("sad"))