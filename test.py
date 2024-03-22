from pynput.mouse import Listener
import pyautogui
import threading
import cv2
import numpy as np
import csv
import time

def draw_mouse_cursor(frame):
    # Get the current mouse position
    x, y = pyautogui.position()

    # Draw a red circle to represent the mouse cursor
    cv2.circle(frame, (x, y), 10, (0, 0, 255), -1)

# Function to continuously record the screen
def record_screen():
    # Define the screen resolution
    screen_width, screen_height = pyautogui.size()

    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('screen_recording.avi', fourcc, 20.0, (screen_width, screen_height))

    # Record the screen
    while not exit_flag.is_set():
        # Capture a screenshot
        screenshot = pyautogui.screenshot()

        # Convert the screenshot to an OpenCV image
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        draw_mouse_cursor(frame)
        
        # Write the frame to the output video file
        out.write(frame)

    # Release the VideoWriter object
    out.release()

# Function to continuously get mouse position
def get_mouse_position():
    while True:
        # Get the current mouse position
        x, y = pyautogui.position()
        # print(f'Mouse position: ({x}, {y})')
        csv_writer.writerow([cv2.getTickCount(), x, y, 'None'])
        time.sleep(0.01)



# Function to handle mouse clicks
def on_click(x, y, button, pressed):
    if pressed:
        if button == button.left:
            print(f'Left click at ({x}, {y})')
            csv_writer.writerow([cv2.getTickCount(), x, y, 'Left click'])
        elif button == button.right:
            print(f'Right click at ({x}, {y})')
            csv_writer.writerow([cv2.getTickCount(), x, y, 'Right click'])


# Create a thread to run the function
            # Open the CSV file to save mouse position data

input('Aperte uma tecla para começar')
csvfile = open('mouse_positions.csv', 'w', newline='')
csv_writer = csv.writer(csvfile)
csv_writer.writerow(['Time', 'X', 'Y', 'MOUSE_EVENT'])  # Header row

mouse_position_thread = threading.Thread(target=get_mouse_position)
mouse_position_thread.start()

exit_flag = threading.Event()
recording_thread = threading.Thread(target=record_screen)
recording_thread.start()

# Start listening for mouse clicks
with Listener(on_click=on_click) as listener:
    listener.join()
    


exit_flag.set()

# Wait for the recording thread to finish
recording_thread.join()

# Close OpenCV windows
cv2.destroyAllWindows()

# Close the CSV file
csvfile.close()
# try:
#     while True:
        # x, y = pyautogui.position()
        # positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        # print(positionStr, end='')
        # print('\b' * len(positionStr), end='', flush=True)
# except KeyboardInterrupt:
#     print('\n')