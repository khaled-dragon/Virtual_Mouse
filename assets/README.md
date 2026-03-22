# AI Virtual Mouse Control 🖱️

An AI-powered virtual mouse system that uses computer vision to control the desktop mouse cursor via hand gestures.

## 🚀 Features
* **Cursor Movement:** Move your hand's index finger to control the mouse pointer across the screen.
* **Click Action:** Pinch your index finger and thumb (reducing the vertical distance) to perform a left-click.
* **Real-time Processing:** Uses MediaPipe for fast and accurate hand landmark detection.

## 🛠️ Built With
* **Python**
* **OpenCV:** For video capturing and image processing.
* **MediaPipe:** For detecting hand landmarks.
* **PyAutoGUI:** For controlling mouse movements and clicks.

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YourUsername/Virtual_Mouse.git](https://github.com/YourUsername/Virtual_Mouse.git)
   Install dependencies:

Bash

pip install opencv-python mediapipe pyautogui
Run the application:

Bash

python mouse_control.py
🎮 How to Use
Once the camera opens, show your hand to the screen.

The yellow circles track your Index Finger (ID 8) and Thumb (ID 4).

Moving your Index Finger moves the cursor.

Bring the Thumb and Index Finger close together (vertically) to trigger a click.
