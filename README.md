# speech_recognition

 **Packages:**
 <br>Install **'Python'** and create a virtual environment.
 <br>Install **'SpeechRecognition'** for processing speech.
 <br>Install **'PyAudio'** for accessing microphone input.

**Implementation:**
<br>Setup: Import the speech_recognition library and initialize the recognizer and microphone objects.
<br>Noise Adjustment: Use the microphone to capture a moment of ambient noise and adjust the recognizer's energy threshold for better accuracy.
<br>Continuous Listening: Implement a loop that continuously listens for audio input using the microphone.
<br>Speech-to-Text Conversion: Utilize Google's speech recognition API to convert the captured audio into text.
<br>User Interaction: Print the recognized text and terminate the program if the user says the keyword "close".
