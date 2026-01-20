# Virtual Mouse Using Hand Gestures 🖱️✨

A real-time hand gesture-controlled virtual mouse that uses computer vision and MediaPipe to control your cursor without touching your mouse!

---

## 📖 About the Project

This project enables you to control your computer's mouse cursor using hand gestures captured through your webcam. Built with Python, OpenCV, and MediaPipe, it tracks your hand movements in real-time and translates them into mouse actions. Move your index finger to control the cursor and perform a pinch gesture to click—no physical mouse required!

**Perfect for:**
- Touchless computer interaction
- Accessibility applications
- Learning computer vision and gesture recognition
- Building interactive presentations

---

## ✨ Key Features

- **Real-time Hand Tracking**: Detects and tracks hand landmarks with high accuracy using MediaPipe
- **Smooth Cursor Control**: Index finger tip controls cursor movement with screen-to-image coordinate mapping
- **Gesture-based Clicking**: Pinch gesture (thumb and index finger together) triggers left mouse click
- **Visual Feedback**: Yellow circles highlight tracked finger positions on the video feed
- **Mirror Effect**: Flipped video display for intuitive, natural hand movements
- **Lightweight & Fast**: Optimized for real-time performance

---

## 🔧 Requirements

### Software
- **Python**: 3.7 or higher
- **Operating System**: Windows, macOS, or Linux

### Hardware
- **Webcam**: Built-in or external USB camera

### Python Libraries
- `opencv-python`: For video capture and image processing
- `mediapipe`: For hand landmark detection
- `pyautogui`: For controlling mouse cursor and clicks

---

## 📦 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/virtual-mouse-hand-gestures.git
cd virtual-mouse-hand-gestures
```

### Step 2: Install Required Libraries

Install all dependencies using pip:

```bash
pip install opencv-python mediapipe pyautogui
```

Or using the `requirements.txt` file (if available):

```bash
pip install -r requirements.txt
```

---

## 🎯 How It Works

### Cursor Movement
The script uses **MediaPipe Hands** to detect 21 hand landmarks in real-time. The **index finger tip (landmark ID 8)** is tracked to control the cursor position:

```python
if id == 8:  # Index finger tip
    mous_x = (screen_width / image_width * x)
    mous_y = (screen_height / image_height * y)
    pyautogui.moveTo(mous_x, mous_y)
```

The coordinates are mapped from the camera frame to your screen resolution for full-screen cursor control.

### Click Detection
A **pinch gesture** is detected by measuring the vertical distance between the **thumb tip (landmark ID 4)** and **index finger tip (landmark ID 8)**:

```python
dist = y2 - y1
if(dist < 40):  # Pinch threshold
    pyautogui.click()
```

When the distance falls below a threshold (40 pixels), a left mouse click is triggered.

### Visual Feedback
Yellow circles are drawn on the tracked finger tips to provide real-time visual feedback:

```python
cv2.circle(image, (x, y), 10, (0, 255, 255))
```

---

## 🚀 How to Run

### Step 1: Run the Script

Execute the main Python script:

```bash
python mouse_control.py
```

### Step 2: Control Your Mouse

```text
1. Position your hand in front of the webcam
2. Move your INDEX FINGER to control the cursor
3. Bring your THUMB and INDEX FINGER together (pinch) to click
4. Press ESC key to exit the application
```

### Step 3: Exit the Program

Press the **ESC** key on your keyboard to close the application:

```text
Key: ESC (key code 27)
```

---

## 📁 Project Structure

```text
virtual-mouse-hand-gestures/
│
├── mouse_control.py       # Main script with hand detection and mouse control logic
├── requirements.txt       # List of Python dependencies
├── README.md             # Project documentation (this file)
└── LICENSE               # License file (optional)
```

---

## 💡 Code Highlights

```python
# Key components of the implementation:

# 1. Initialize hand detection model
capture_hands = mediapipe.solutions.hands.Hands()

# 2. Capture video from webcam
camera = cv2.VideoCapture(0)

# 3. Flip image for mirror effect
image = cv2.flip(image, 1)

# 4. Convert BGR to RGB for MediaPipe processing
rgp_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 5. Process and detect hands
output_hand = capture_hands.process(rgp_image)

# 6. Track index finger (ID 8) for cursor movement
# 7. Track thumb (ID 4) for click detection
# 8. Calculate distance between thumb and index finger
# 9. Trigger click when distance < 40 pixels

# 10. Display video feed with visual feedback
cv2.imshow("Hand movement video capture", image)
```

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve this project:

```text
1. Fork the repository
2. Create a new branch: git checkout -b feature-name
3. Make your changes and commit: git commit -m 'Add feature'
4. Push to the branch: git push origin feature-name
5. Submit a pull request
```

**Ideas for Enhancement:**
- Add right-click functionality with different gestures
- Implement double-click detection
- Add scroll functionality
- Improve click detection accuracy
- Add gesture customization options

---

## 📧 Contact & Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Star ⭐ this repository if you found it helpful!
- or email me at: kwael6774@gmail.com
خ
---

**Happy Gesture Controlling! 👋🖱️**
