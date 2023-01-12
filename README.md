# Audio to Text Converter
This is a simple GUI application that allows you to convert an audio file (in .wav format) to text. The application is built using Python and the Tkinter library.

## Features
* The application accepts audio files in .wav format.
* The user can select the language of the audio file to improve the accuracy of the transcription.
* The transcription is done using the SpeechRecognition library, which uses Google's Speech-to-Text API.
* The transcription results are displayed in a text field that can be copied.
* The application has a minimum size of 400x300 pixels and the elements of the interface are resized proportionately to the window size.
* The interface has a language dropdown that allows you to choose the language of the audio file.
## Requirements
This application requires the following Python libraries:

* SpeechRecognition

You can install these libraries by running the following command:

```pip install -r requirements.txt ```
## Usage
1. To use the application, run the script audio_to_text_converter.py
2. Select the language of the audio file from the dropdown
3. Choose the .wav file to convert into text
4. Press the "Audio to Text" button
5. The transcription results will be displayed in the text field
6. You can copy the results by selecting the text and pressing "Ctrl+C" or "Cmd+C"
## Limitations
* The application only accepts audio files in .wav format and the file size should be less than 10MB.
* The application is using Google's Speech-to-Text API and it has a limit of 50 requests per day for a free API key.
## Note
This application is for demonstration purposes only and is not intended for production use. The accuracy of the transcription results depends on various factors, including the quality of the audio file and the selected language.

This application is a good starting point to understand the basics of how to convert audio to text using Python and the SpeechRecognition library. You can improve its functionality and use it as a base for more complex projects.
