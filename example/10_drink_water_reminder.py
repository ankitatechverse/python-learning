"""
Drink Water Reminder" that:
Shows a reminder every hour on your desktop.
Plays a ringtone when reminding.
Starts automatically when your PC boots.
"""

import time
import winsound
import os
from datetime import datetime

current_dir = os.getcwd() 
print(current_dir)

def water_reminder():
  
    reminder_interval = 3600  # 1 hour in seconds
    ringtone = f"{current_dir}\\loud_beep.wav"  # Change to your preferred sound file
    print(ringtone)
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"Reminder: It's {current_time}. Time to drink water!")
        winsound.PlaySound(ringtone, winsound.SND_FILENAME)
        time.sleep(reminder_interval)

if __name__ == "__main__":
    water_reminder()