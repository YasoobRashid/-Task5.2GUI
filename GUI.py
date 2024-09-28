import tkinter as tk
from RPi import GPIO
import time

# Set up GPIO mode and pin
GPIO.setmode(GPIO.BCM)
LED_PIN = 18
GPIO.setup(LED_PIN, GPIO.OUT)

# Set up PWM on the pin (with 1000Hz frequency)
pwm = GPIO.PWM(LED_PIN, 1000)
pwm.start(0)  # Start with LED off

# Function to change LED brightness based on slider value
def change_brightness(val):
    duty_cycle = int(val)  # Convert slider value to integer
    pwm.ChangeDutyCycle(duty_cycle)  # Change PWM duty cycle

# Set up the main window
root = tk.Tk()
root.title("LED Brightness Control")

# Create a label
label = tk.Label(root, text="Adjust LED Brightness")
label.pack(pady=10)

# Create a slider widget
slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=change_brightness)
slider.pack(pady=20)

# Create a quit button
quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.pack(pady=20)

# Main event loop
try:
    root.mainloop()
finally:
    # Clean up GPIO when closing the program
    pwm.stop()
    GPIO.cleanup()
