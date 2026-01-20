import cv2
import mediapipe
import pyautogui

capture_hands = mediapipe.solutions.hands.Hands()
drawing_option = mediapipe.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
camera = cv2.VideoCapture(0)
x1 = y1 = x2 = y2 = 0

while True:
    ret, image = camera.read()
    image_height, image_width, _ = image.shape
    if not ret:
        break

    image = cv2.flip(image,1)
    rgp_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    output_hand = capture_hands.process(rgp_image)
    all_hands = output_hand.multi_hand_landmarks
    if all_hands:
        for hand in all_hands:
            drawing_option.draw_landmarks(image, hand)
            one_hand_landmarks = hand.landmark
            for id, lm in enumerate(one_hand_landmarks):
                x = int(lm.x * image_width)
                y = int(lm.y * image_height)
                # print(x, y)
                if id == 8:
                    mous_x = (screen_width / image_width * x)
                    mous_y = (screen_height / image_height * y)
                    cv2.circle(image,(x,y),10,(0,255,255))
                    pyautogui.moveTo(mous_x, mous_y)
                    x1 = x
                    y1 = y
                if id == 4:
                    x2 = x
                    y2 = y
                    cv2.circle(image,(x,y),10,(0,255,255))    
        dist = y2 - y1
        print(dist)
        if(dist<40):
            pyautogui.click()
            print("Clicked")

    cv2.imshow("Hand movement video capture", image)
    key = cv2.waitKey(1)
    if key == 27:  
        break

camera.release()
cv2.destroyAllWindows()

