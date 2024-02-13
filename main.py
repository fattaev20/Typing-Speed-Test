import time  # Import the time module to handle time-related functions
import tkinter  # Import tkinter for GUI
from tkinter import *  # Import everything from tkinter for convenience


# Handler function to process key presses
def handler(event):
    user_text = entry.get()  # Get the text entered by the user from the Entry widget
    text_list = user_text.split(" ")  # Split the entered text into a list of words

    accuracy = len(user_text)  # Initialize accuracy with the length of the entered text

    # Calculate accuracy by comparing each character with the corresponding character in the sample text
    for item in user_text:
        if item != sample_text[user_text.index(item)]:
            accuracy = accuracy - 1

    # Update accuracy label if the length of user text is not zero
    if len(user_text) != 0:
        ac.configure(text=f"Accuracy: {(accuracy / len(user_text)) * 100}%")

    # Check if 10 seconds have passed since the start of the test
    if time.time() - s > 10:
        # Update accuracy and typing speed labels after the time is up
        ac.configure(text=f"Accuracy: {(accuracy / len(user_text)) * 100}%\n"
                          f"Typing Speed: {len(text_list)} words/min")
        text.configure(text="Time is up!", width=45)  # Change text label to indicate time's up
        tk.geometry("480x240")  # Adjust window size


custom_font = ("Helvetica", 12)  # Define a custom font

sample_text = ("Look again at that dot. That's here. That's home. That's us. On it everyone you "
               "love, everyone you know, everyone you ever heard of, every human being who ever "
               "was, lived out their lives. The aggregate of our joy and suffering, thousands of "
               "confident religions, ideologies, and economic doctrines, every hunter and forager, "
               "every hero and coward, every creator and destroyer of civilization, every king and "
               "peasant, every young couple in love, every mother and father, hopeful child, inventor "
               "and explorer, every teacher of morals, every corrupt politician, every superstar, every "
               "supreme leader, every saint and sinner in the history of our species lived there--on "
               "a mote of dust suspended in a sunbeam.")  # Define a sample text

sample_list = sample_text.split(" ")  # Split the sample text into a list of words

s = time.time()  # Record the start time of the test

tk = Tk()  # Create a tkinter window instance
tk.geometry("480x480")  # Set the initial window size
tk.title("Typing speed test")  # Set the window title

# Create a label widget to display the sample text
text = tkinter.Label(tk, text=sample_text, wraplength=400, justify="left", pady=40,
                     padx=40, font=custom_font)
text.grid(row=0, column=0, sticky="w")  # Position the label in the tkinter grid layout

# Create an entry widget for user input
entry = tkinter.Entry(width=64)
entry.configure(justify="left")
entry.grid(row=1, column=0)  # Position the entry widget in the tkinter grid layout

# Create a label widget to display accuracy
ac = tkinter.Label(text="Accuracy: 0%", font=custom_font, pady=40)
ac.grid(row=2, column=0)  # Position the accuracy label in the tkinter grid layout

entry.bind("<KeyPress>", handler)  # Bind key press event to the handler function

tk.mainloop()  # Start the tkinter event loop to display the window and handle events

