import speech_recognition as sr
import tkinter as tk
from tkinter import filedialog
import os

def transcribe_audio():
    
    # clean fields
    text_label.config(text="")
    text_field.config(state="normal")
    # Get file path for audio file
    file_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
    if not file_path:
        text_field.config(state="disabled")
        return
    
    # check the size of the file
    file_size = os.path.getsize(file_path)
    max_file_size = 10*1024*1024
    if file_size > max_file_size:
        text_label.config(text="Error: File size exceeded 10MB.")
        text_field.delete(1.0, tk.END)
        text_field.insert(tk.END, "Please select a language and then choose a .wav file to convert into text...")
        text_field.config(state="disabled")
        return

    # Initialize speech recognizer
    r = sr.Recognizer()

    try:
    # Open audio file
        with sr.AudioFile(file_path) as source:

            # Read audio file
            audio = r.record(source)
    except:
        text_label.config(text="Error: Could not understand audio")
        text_field.delete(1.0, tk.END)
        text_field.insert(tk.END, "Please select a language and then choose a .wav file to convert into text...")
        text_field.config(state="disabled")
        return

    # Get language from input
    language = language_var.get()

    # Recognize text from audio file
    try:
        text = r.recognize_google(audio, language=language)

        # Write text in text field
        text_field.delete(1.0, tk.END)
        text_field.insert(tk.END, text)
        text_field.config(state="disabled")
    except sr.RequestError:
        text_label.config(text="Error: Could not connect to Google Speech Recognition API")
        text_field.delete(1.0, tk.END)
        text_field.insert(tk.END, "Please select a language and then choose a .wav file to convert into text...")
        text_field.config(state="disabled")
    except sr.UnknownValueError:
        text_label.config(text="Error: Could not understand audio")
        text_field.delete(1.0, tk.END)
        text_field.insert(tk.END, "Please select a language and then choose a .wav file to convert into text...")
        text_field.config(state="disabled")


# Create the main window
root = tk.Tk()
root.geometry("800x600")
root.title("Audio to Text")
root.minsize(width=600, height=300)
root.columnconfigure(1,minsize=250)

# Create a button to select and transcribe audio file
audio_to_text_button = tk.Button(root, text="Choose file", command=transcribe_audio)
audio_to_text_button.grid(row=0, column=0, padx=5, pady=5)

# Choose language
language_var = tk.StringVar(value="en-US")
language_options = ["en-US", "it-IT", "fr-FR", "es-ES", "de-DE"]
language_dropdown = tk.OptionMenu(root, language_var, *language_options)
language_dropdown.grid(row=0, column=1, padx=5, pady=5)
language_dropdown.config(width=8)

# Create a label to display error messages
text_label = tk.Label(root, text="", justify="left")
text_label.grid(row=1, column=0, padx=5, pady=5)
text_label.config(width=60,fg='red')

# Create a text field to display transcribed text
text_field = tk.Text(root, background="white")
text_field.grid(row=2, column=0, columnspan=2, padx=5, pady=5,sticky="nsew")
text_field.insert(tk.END, "Please select a language and then choose a .wav file to convert into text...")
text_field.config(state="disabled")

# Set rezising proportions for columns and rows
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

# Run the main loop to display the window
root.mainloop()
