# p5GloveOT

This code is a Python script that records the screen and simultaneously captures P5 Glove events such as thumb bending. Here's a summary of what it does:

Imports necessary libraries including pynput, pyautogui, threading, cv2, numpy, csv, and time.

Defines a function draw_P5_Glove_on_screen(frame) to draw the P5 Glove cursor on an OpenCV frame.

Defines a function record_screen() to continuously record the screen using pyautogui.screenshot(), convert the screenshots to OpenCV frames, draw the P5 Glove cursor on each frame, and write the frames to a video file (screen_recording.avi).

Defines a function P5_Glove_position() to continuously get the P5 Glove position using pyautogui.position() and write the position data to a CSV file (mouse_positions.csv).

Defines a function on_finger_movement(x, y, button, pressed) to handle P5 Glove fingers events. It prints the P5 Glove position and type of finger bending thumb, index or middle) and writes the data to the CSV file.

Opens the CSV file (p5_positions.csv) to save P5 Glove position data with a header row.

Creates and starts a thread (p5_position_thread) to run the get_mouse_position() function.

Creates and starts a thread (recording_thread) to run the record_screen() function.

Starts listening for P5 Glove clicks using pynput.Listener.

Once a key is pressed (as instructed by input('Aperte uma tecla para começar')), it starts capturing P5 Glove finger bending and positions.

When the user presses any key, it sets an exit flag (exit_flag) to signal the threads to stop.

Waits for the recording thread to finish.

Closes OpenCV windows and the CSV file.

This script records the screen while capturing P5 Glove bending events and positions, allowing you to analyze the P5 Glove behavior during the screen recording. If you have any further questions or need clarification, feel free to ask!
