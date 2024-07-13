# speech_recognition

 Packages:
 Install 'Python' and create a virtual environment.
 Install 'SpeechRecognition' for processing speech.	
 Install 'PyAudio' for accessing microphone input.

Implementation :
Setup: Import the speech_recognition library and initialize the recognizer and microphone objects.
Noise Adjustment: Use the microphone to capture a moment of ambient noise and adjust the recognizer's energy threshold for better accuracy.
Continuous Listening: Implement a loop that continuously listens for audio input using the microphone.
Speech-to-Text Conversion: Utilize Google's speech recognition API to convert the captured audio into text.
User Interaction: Print the recognized text and terminate the program if the user says the keyword "close".
