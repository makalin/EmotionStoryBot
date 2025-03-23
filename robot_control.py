import serial
import time

class RobotController:
    def __init__(self, port='/dev/ttyUSB0', baud_rate=9600):
        # Initialize serial connection to Arduino (adjust port as needed)
        try:
            self.arduino = serial.Serial(port, baud_rate)
            time.sleep(2)  # Wait for connection
            print("Robot connected.")
        except Exception as e:
            print(f"Robot connection failed: {e}. Running without hardware.")
            self.arduino = None
    
    def perform_action(self, emotion):
        if not self.arduino:
            print("[No hardware] Simulating action.")
            return
        
        # Simple actions based on emotion
        if emotion == "happy":
            self.arduino.write(b'W')  # Wave arm
            print("[Robotic Arm] Waving!")
        elif emotion == "sad":
            self.arduino.write(b'S')  # Slow nod
            print("[Robotic Arm] Nodding slowly.")
        elif emotion == "surprised":
            self.arduino.write(b'F')  # Flash LED
            print("[LED] Flashing!")
    
    def close(self):
        if self.arduino:
            self.arduino.close()
            print("Robot disconnected.")

# Test the module standalone
if __name__ == "__main__":
    robot = RobotController()
    robot.perform_action("happy")
    robot.close()