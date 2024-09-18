## Speech Recognition with Python

This project demonstrates how to use Python to process speech using the `SpeechRecognition` library and capture microphone input using `PyAudio`. It listens for spoken words, converts the audio to text using Google's Speech Recognition API, and interacts with the user.

## Requirements

To get started, you'll need the following:

1. Python (3.x recommended)
2. Virtual environment (optional but recommended)
3. The following Python libraries:
 - `SpeechRecognition`: For processing speech.
 - `PyAudio`: For accessing microphone input.

## Installation

### Step 1: Install Python

First, ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Step 2: Create and Activate a Virtual Environment (Optional)

To avoid conflicts with other packages, it's best to use a virtual environment.

# Create a virtual environment
```bash
python -m venv myenv
```
# Activate the virtual environment

# On Windows
```bash
source myenv/Scripts/activate
```

# On macOS/Linux
```bash
source myenv/bin/activate
```


### Step 3: Install Required Packages

Use `pip` to install the necessary libraries:
# Install SpeechRecognition
```bash
pip install SpeechRecognition
```

# Install PyAudio
```bash
pip install pyaudio
```

> **Note:** If you're having trouble installing `PyAudio`, you may need to install it using a precompiled binary from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) (Windows only).

## Usage

1.  **Import Required Libraries**  
    First, import the `SpeechRecognition` library and initialize recognizer and microphone objects:

```bash
    `import speech_recognition as sr
    r = sr.Recognizer()
    m = sr.Microphone()
```
    
2.  **Adjust for Ambient Noise**  
    Use the microphone to capture a brief moment of ambient noise and adjust the energy threshold:

```bash
    with m as source:
        r.adjust_for_ambient_noise(source)`
```
    
3.  **Continuous Listening**  
    Implement a loop that continuously listens for speech input using the microphone:

```bash
    while True:
        with m as source:
            audio = r.listen(source)`
```
    
4.  **Convert Speech to Text**  
    Use Google's speech recognition API to convert the captured audio into text:

```bash
    try:
        value = r.recognize_google(audio)
        print(f"You said: {value}")`
```
    
5.  **Exit on Keyword**  
    If the recognized text contains the word "close", the program will exit:

```bash
    if value.lower() == "close":
        print("Closing the program...")
        break`
```
**Result:**




https://github.com/user-attachments/assets/28dbc1eb-0a24-4b63-8483-34d03a199457

